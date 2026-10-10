#!/usr/bin/env python3
"""Single-species synthetic advection/dispersion/loss, standard library only.

Finite column: resident C, Darcy flux phi*u, total flux phi*(u*C-D*C_x).
Flux inlet, zero dispersive exit, initially empty; FV upwind + backward Euler.
Run documented production/verification exports with verify_advection.py.
No clipping. Auxiliary periodic, hyperbolic and closed tests are separate.
"""
import argparse
import csv
import json
import math
from pathlib import Path

DEFAULT = dict(L=1., phi=.30, u=1e-5, D=1e-6, k=0., C_ref=1., Tp=20000.)


def validate(p, n, dt=None, end=None):
    if type(n) is not int or n < 2:
        raise ValueError('Require integer N>=2')
    if any(not math.isfinite(p[q]) for q in DEFAULT):
        raise ValueError('All parameters must be finite')
    if p['L'] <= 0 or not 0 < p['phi'] <= 1 or any(p[q] < 0 for q in ('u', 'D', 'k', 'C_ref')) or p['Tp'] <= 0:
        raise ValueError('Require L,Tp>0, 0<phi<=1 and u,D,k,C_ref>=0')
    for q in (dt, end):
        if q is not None and (not math.isfinite(q) or q <= 0):
            raise ValueError('Require finite positive time step/end')


def factor(lo, diag, up):
    """Thomas factors for the accepted positive, dominant tridiagonal matrix."""
    piv, mult = diag[:], []
    for i in range(1, len(piv)):
        if piv[i-1] <= 0:
            raise ArithmeticError('Nonpositive matrix pivot')
        v = lo[i-1]/piv[i-1]
        mult.append(v)
        piv[i] -= v*up[i-1]
    if piv[-1] <= 0:
        raise ArithmeticError('Nonpositive matrix pivot')
    return piv, mult, up


def solve(fac, rhs):
    piv, mult, up = fac
    y = rhs[:]
    for i in range(1, len(y)):
        y[i] -= mult[i-1]*y[i-1]
    y[-1] /= piv[-1]
    for i in range(len(y)-2, -1, -1):
        y[i] = (y[i]-up[i]*y[i+1])/piv[i]
    return y


def coefficients(p, n):
    validate(p, n)
    h = p['L']/n
    a, b = p['u']/h, p['D']/h**2
    diag = [a+2*b+p['k']]*n
    diag[0] = diag[-1] = a+b+p['k']
    return h, [-a-b]*(n-1), diag, [-b]*(n-1)


def linear_residual(lo, diag, up, c, rhs):
    worst, scale = 0., 0.
    for i, (d, v, r) in enumerate(zip(diag, c, rhs)):
        terms = [d*v, -r]
        if i:
            terms.append(lo[i-1]*c[i-1])
        if i+1 < len(c):
            terms.append(up[i]*c[i+1])
        worst = max(worst, abs(math.fsum(terms)))
        scale = max(scale, math.fsum(map(abs,terms)))
    return worst/max(scale,1e-300)


def steady(p, n):
    h, lo, diag, up = coefficients(p, n)
    if p['u'] <= 0:
        raise ValueError('Finite fed steady reference requires u>0')
    rhs = [p['u']*p['C_ref']/h]+[0.]*(n-1)
    c = solve(factor(lo, diag, up), rhs)
    return c, linear_residual(lo, diag, up, c, rhs)


def steady_coefficients(p):
    if p['u'] <= 0 or p['D'] <= 0:
        raise ValueError('Finite continuum roots require positive u,D')
    u, D, k, L = (p[q] for q in ('u', 'D', 'k', 'L'))
    s = math.sqrt(u*u+4*D*k)
    rp, rm = (u+s)/(2*D), -2*k/(u+s)
    ratio = -rm*math.exp(rm*L)/rp
    a = u*p['C_ref']/((u-D*rm)+(u-D*rp)*math.exp(-rp*L)*ratio)
    return a, a*ratio, rm, rp


def exp_average(r, left, right, shift=0.):
    if r == 0:
        return 1.
    # Keep every evaluated exponential argument <=0 for both bounded roots.
    if r < 0:
        return math.exp(r*(left-shift))*math.expm1(r*(right-left))/(r*(right-left))
    return math.exp(r*(right-shift))*(-math.expm1(-r*(right-left)))/(r*(right-left))


def steady_average(p, left, right):
    a, b, rm, rp = steady_coefficients(p)
    return a*exp_average(rm,left,right)+b*exp_average(rp,left,right,p['L'])


def steady_point(p, x):
    a, b, rm, rp = steady_coefficients(p)
    return a*math.exp(rm*x)+b*math.exp(rp*(x-p['L']))


def feed_average(p, left, right):
    return p['C_ref']*max(0.,min(right,p['Tp'])-max(left,0.))/(right-left)


def face_fluxes(p, c, feed):
    h, phi, u, D = p['L']/len(c), p['phi'], p['u'], p['D']
    # Inlet split is a declared half-cell diagnostic trace, not another BC.
    trace = (u*feed+2*D*c[0]/h)/(u+2*D/h) if u+2*D/h else c[0]
    adv = [phi*u*trace]
    disp = [phi*u*feed-adv[0]]
    for i in range(len(c)-1):
        adv.append(phi*u*c[i])
        disp.append(-phi*D*(c[i+1]-c[i])/h)
    adv.append(phi*u*c[-1]); disp.append(0.)
    total = [a+b for a,b in zip(adv,disp)]
    total[0] = phi*u*feed
    return adv, disp, total, trace


def spatial_metrics(p, c):
    h = p['L']/len(c)
    amount = math.fsum(c)
    if amount == 0:
        return dict(centroid_m=None, width_m=None)
    mean = math.fsum(v*(i+.5)*h for i,v in enumerate(c))/amount
    var = math.fsum(v*(((i+.5)*h-mean)**2+h*h/12) for i,v in enumerate(c))/amount
    return dict(centroid_m=mean,width_m=math.sqrt(var))


def pulse(p, n=400, dt=100., end=400000., initial=None,
          snapshot_times=(0.,20000.,50000.,100000.,150000.,200000.,400000.),
          writer=None):
    validate(p, n, dt, end)
    h, lo0, diag0, up0 = coefficients(p,n)
    c = [0.]*n if initial is None else list(initial)
    if len(c)!=n or any(not math.isfinite(v) or v<0 for v in c):
        raise ValueError('Require finite nonnegative initial cell averages')
    snapshots = {0.:c[:]} if 0. in snapshot_times else {}
    stops = sorted(set([t for t in snapshot_times if 0<t<=end]+[end]))
    t, target_index = 0., 0
    M0 = p['phi']*h*math.fsum(c)
    scale = max(p['phi']*p['L']*p['C_ref'],M0)
    I=O=B=0.
    min_c, max_c = min(c), max(c)
    negative_count = 0
    worst_step=worst_cum=worst_lin=0.
    interval_rows=[]
    cached={}
    if writer:
        writer.profile(0.,c)
    while t < end:
        step = min(dt,end-t,stops[target_index]-t)
        if step not in cached:
            lo, diag, up = [step*v for v in lo0], [1+step*v for v in diag0], [step*v for v in up0]
            cached[step] = (lo,diag,up,factor(lo,diag,up))
        lo,diag,up,fac = cached[step]
        feed = feed_average(p,t,t+step)
        rhs = c[:]; rhs[0] += step*p['u']*feed/h
        previous = p['phi']*h*math.fsum(c)
        c = solve(fac,rhs)
        current = p['phi']*h*math.fsum(c)
        lin = linear_residual(lo,diag,up,c,rhs)
        low, high = min(c), max(c)
        min_c, max_c = min(min_c,low),max(max_c,high)
        negative_count += sum(v<0 for v in c)
        dI=step*p['phi']*p['u']*feed
        dO=step*p['phi']*p['u']*c[-1]
        dB=step*p['k']*current
        I+=dI; O+=dO; B+=dB
        residual=math.fsum([current,-previous,-dI,dO,dB])
        cumulative=math.fsum([current,-M0,-I,O,B])
        worst_step=max(worst_step,abs(residual)); worst_cum=max(worst_cum,abs(cumulative)); worst_lin=max(worst_lin,lin)
        row=dict(t_left_s=t,t_right_s=t+step,C_in_interval_average=feed,C_out_right_endpoint=c[-1],
                 F_in_interval_average=p['phi']*p['u']*feed,F_out_right_endpoint=p['phi']*p['u']*c[-1],
                 M_previous=previous,M_next=current,delta_I=dI,delta_O=dO,delta_B=dB,
                 I=I,O=O,B=B,step_residual=residual,cumulative_residual=cumulative,
                 step_residual_scaled=abs(residual)/scale if scale else None,
                 cumulative_residual_scaled=abs(cumulative)/scale if scale else None,
                 linear_residual_scaled=lin,C_min_actual=low,C_max_actual=high)
        interval_rows.append(row)
        t += step
        if t == stops[target_index]:
            snapshots[t]=c[:]
            if writer:
                writer.profile(t,c); writer.faces(t-step,t,c,feed)
            target_index += 1
        if writer:
            writer.budget(row)
    report=dict(initial_inventory=M0,final_inventory=current,input=I,export=O,disappeared=B,
                min_C=min_c,max_C=max_c,negative_value_count=negative_count,nonzero_amount_scale=scale,
                max_step_residual=worst_step,max_cumulative_residual=worst_cum,
                max_step_residual_scaled=worst_step/scale if scale else None,
                max_cumulative_residual_scaled=worst_cum/scale if scale else None,max_linear_residual_scaled=worst_lin,
                grid_n=n,dt_s=dt,end_s=end,step_count=len(interval_rows),boundary='finite_flux_inlet_open_exit')
    return dict(c=c,snapshots=snapshots,rows=interval_rows,report=report)


def outlet_metrics(result):
    rows=result['rows']; report=result['report']
    out=report['export']; dose=report['input']
    peak_row=max(rows,key=lambda r:r['C_out_right_endpoint'])
    metrics=dict(peak_C=peak_row['C_out_right_endpoint'],peak_time_s=peak_row['t_right_s'],
                 input_mol_m2=dose,export_fraction=out/dose if dose else None,
                 loss_fraction=report['disappeared']/dose if dose else None,
                 storage_fraction=report['final_inventory']/dose if dose else None,
                 quantile_normalization='mass exported within reported observation window')
    for q in (.1,.5,.9):
        value=None; acc=0.
        if out>0:
            target=q*out
            for r in rows:
                w=r['delta_O']
                if w>0 and acc+w>=target:
                    value=r['t_left_s']+(r['t_right_s']-r['t_left_s'])*(target-acc)/w
                    break
                acc+=w
        metrics['t'+str(int(q*100))+'_s']=value
    if out>0:
        mean=math.fsum(r['delta_O']*(r['t_left_s']+r['t_right_s'])/2 for r in rows)/out
        var=math.fsum(r['delta_O']*((r['t_left_s']-mean)**2+(r['t_left_s']-mean)*(r['t_right_s']-mean)+(r['t_right_s']-mean)**2)/3 for r in rows)/out
        metrics.update(mean_time_s=mean,width_time_s=math.sqrt(var))
    else:
        metrics.update(mean_time_s=None,width_time_s=None)
    return metrics


class Export:
    """Streaming bounded student tables; all fluxes/amounts per bulk area."""
    def __init__(self,out,case,p):
        self.case,self.p=case,p
        self.files=[]
        self.writers={}
        for name,columns in {
            'profiles':['case_id','t_s','cell_id','x_left_m','x_right_m','C_cell_average_mol_m3_water'],
            'face-fluxes':['case_id','t_left_s','t_right_s','face_id','x_face_m','F_adv_mol_m2_s','F_disp_mol_m2_s','F_total_mol_m2_s','support','inlet_trace_mol_m3_water'],
            'pulse-budget':['case_id','t_left_s','t_right_s','C_in_interval_average','C_out_right_endpoint','F_in_interval_average','F_out_right_endpoint','M_previous','M_next','delta_I','delta_O','delta_B','I','O','B','step_residual','cumulative_residual','step_residual_scaled','cumulative_residual_scaled','linear_residual_scaled','C_min_actual','C_max_actual']
        }.items():
            f=(out/(case+'-'+name+'.csv')).open('w',newline=''); self.files.append(f)
            w=csv.writer(f); w.writerow(columns); self.writers[name]=w

    def profile(self,t,c):
        h=self.p['L']/len(c)
        self.writers['profiles'].writerows((self.case,t,i,i*h,(i+1)*h,v) for i,v in enumerate(c))

    def faces(self,left,right,c,feed):
        adv,disp,total,trace=face_fluxes(self.p,c,feed); h=self.p['L']/len(c)
        self.writers['face-fluxes'].writerows((self.case,left,right,i,i*h,a,d,f,
            'inlet: exact interval-average total; half-cell diagnostic split' if i==0 else 'right-endpoint FV flux',trace if i==0 else '')
            for i,(a,d,f) in enumerate(zip(adv,disp,total)))

    def budget(self,row):
        self.writers['pulse-budget'].writerow([self.case]+list(row.values()))

    def close(self):
        for f in self.files: f.close()


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out',type=Path,required=True)
    parser.add_argument('--n',type=int,default=400); parser.add_argument('--dt',type=float,default=100.)
    parser.add_argument('--end',type=float,default=400000.)
    for q in DEFAULT: parser.add_argument('--'+q,type=float,default=DEFAULT[q])
    a=parser.parse_args(); p={q:getattr(a,q) for q in DEFAULT}
    validate(p,a.n,a.dt,a.end); a.out.mkdir(parents=True,exist_ok=True)
    writer=Export(a.out,'custom',p)
    try: result=pulse(p,a.n,a.dt,a.end,writer=writer)
    finally: writer.close()
    (a.out/'custom-report.json').write_text(json.dumps(dict(parameters=p,report=result['report'],metrics=outlet_metrics(result)),indent=2)+'\n')


if __name__=='__main__': main()
