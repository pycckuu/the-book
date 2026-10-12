---
title: "Saturation without growth"
---

Watch a dissolved substrate disappear from a sealed, well-mixed liquid. Early on, abundant supply may keep a fixed capacity busy. As supply falls, the same capacity can spend more time waiting. One curve captures that change. What the curve means depends on what we measure.

## One shape, distinct observables

A single-enzyme mechanism can yield a Michaelis-Menten law after an appropriate reduction. Free substrate differs from substrate bound in the enzyme complex. Under the quasi-steady-state interpretation, $K_m=(k_{-1}+k_{\mathrm{cat}})/k_1$ and capacity is $k_{\mathrm{cat}}E_T$, where $E_T$ is total active enzyme. The binding dissociation constant is $K_d=k_{-1}/k_1$; equality requires an additional limiting regime. A half-maximal rate alone is not an affinity measurement. [^sk_enzyme_sources]

The empirical Monod growth shape is $\mu(S)=\mu_{\max}S/(K_s+S)$, with $\mu=d\ln X/dt$ for positive biomass $X$. Its observable is biomass-specific growth, in $\mathrm{s^{-1}}$, rather than volumetric substrate disappearance. Growth and uptake constants need not agree. [^sk_growth_sources] This module follows substrate depletion with fixed capacity; it does not simulate growing biomass.

## Declare the liquid and the ledger

The state $S$ is available dissolved substrate concentration per modeled liquid volume, in $\mathrm{mol\,m^{-3}}$. The positive half-saturation $K$ uses the same units. The capacity $q_{\max}$ has units $\mathrm{mol\,m^{-3}\,s^{-1}}$. Liquid volume $V_\ell$ is fixed, in $\mathrm{m^3}$. There is no porosity multiplier, inlet, outlet or transport in this batch. Fixed conditions and capacity exclude growth, enzyme regulation, inhibition and energy gating from the closure.

$$
\begin{gathered}
q(S)=q_{\max}\frac{S}{K+S},\qquad
\frac{dS}{dt}=-q(S),\qquad \frac{dZ}{dt}=q(S),\\
S(0)=S_0,\qquad Z(0)=0.
\end{gathered}
$$

$Z$ accumulates depleted substrate equivalents per liquid volume. Remaining amount $M=V_\ell S$ and cumulative depleted equivalents $B=V_\ell Z$, both in mol, obey

$$
M+B=M_0,\qquad M_0=V_\ell S_0.
$$

Here $B$ is a depletion ledger, not biomass. This accounting identity does not specify products, mineralization or elemental conservation. Those require a reaction stoichiometry and additional states. An enzyme assay of free-plus-bound substrate also needs its own observation map.

## Limits you can check on paper

For $S_0,K,q_{\max}>0$, integration gives

$$
S_0-S+K\ln(S_0/S)=q_{\max}t,\qquad
 t_f=\frac{S_0(1-f)+K\ln(1/f)}{q_{\max}},\quad 0<f<1.
$$

$t_f$ is the time to $S=fS_0$. Positive $K$ leaves a positive tail at every finite time: an exhaustion time must name a threshold. Zero initial substrate remains zero; zero capacity leaves the initial concentration unchanged. Fractional times for these branches are undefined, recorded as null with a reason.

At small $S/K$, $q\approx(q_{\max}/K)S$. This linear rate exceeds the exact rate by a relative fraction $S/K$. The constant-rate approximation $q\approx q_{\max}$ has relative excess $K/S$. A five-percent instantaneous rate criterion needs $S/K\leq0.05$ or $S/K\geq20$, respectively. These inequalities are not trajectory-error guarantees.

## A synthetic calculation, with a separate reference

All supplied parameters and observations are illustrative and synthetic. The accepted inputs are $V_\ell=10^{-3}\,\mathrm{m^3}$, $K=0.1\,\mathrm{mol\,m^{-3}}$ and $q_{\max}=10^{-5}\,\mathrm{mol\,m^{-3}\,s^{-1}}$, so $\tau=K/q_{\max}=10000\,\mathrm{s}$. The low and high learner cases start at $S_0/K=0.01$ and $100$. The transition case at $1$ supplies owner verification support. Each trajectory has its own fixed analytical $t_{0.01}$ window. The high case ends at $S=K$ analytically; it has not entered the five-percent linear domain.

Backward Euler uses the positive root of

$$
S_{n+1}+\Delta t\,q(S_{n+1})=S_n.
$$

The independent reference instead bisects $S_0e^y+Ky-S_0+q_{\max}t=0$ in $y=\ln(S/S_0)$, bracketed by $[-q_{\max}t/K,0]$. It checks both normalized residual and log-bracket width against $10^{-12}$. The reference is not a second time-stepping run or empirical validation.

The accepted default is $\Delta t=100\,\mathrm{s}$ for these cases and windows. Separate endpoint and snapshot error gates use $0.005S_0$; this does not promise that relative accuracy in a shrinking tail. Half-step comparisons use both endpoint grids and 401 snapshots on the fixed trajectory window, with labeled linear interpolation. Threshold times use a separate fixed event extension and retain crossing brackets or censoring. The [refinement table](../model/results/time-refinement.csv) preserves actual coarse failures at 400 s as well as passing controls. Positivity and accounting passed without clipping; a balanced ledger alone is not an accuracy test.

## Read the saved evidence

Start with the [single-law rate curve](../model/results/rate-curve.csv) and [threshold table](../model/results/thresholds.csv). The [saved-results archive](../model/saved-results.zip) contains complete `results/*-step-ledger.csv` files, batch concentration snapshots, auxiliary controls and verification records. Extract it before following the [model README](../model/README.md) for spreadsheet reconstruction. Each interval supplies its actual $\Delta t$, right-endpoint rate, increment $\Delta B=V_\ell\Delta t\,q(S_{n+1})$, and independently accumulated amount. Snapshot rates are instantaneous diagnostics; trapezoidal integration would change the accepted update ledger.

The [blank worksheet](../model/results/blank-step-worksheet.csv) and separate [open worked values](../model/results/OPEN-worked-step-values.csv) select rows from the complete ledgers. Gaps require intervening increments for cumulative sums. Blank numeric cells mean null, not zero.

Low-substrate rate observations mainly constrain $q_{\max}/K$; high-substrate observations mainly constrain capacity. Even with an appropriate enzyme interpretation, observing $k_{\mathrm{cat}}E_T$ does not separate its factors. These are conditional inference limits, not a fit. Numerical agreement tests this declared equation. It does not establish mat stability, environmental rates, enzyme-reduction accuracy, growth or learning outcomes.

[^sk_enzyme_sources]: Kashvi Srivastava et al., “Accuracy Versus Predominance: Reassessing the Validity of the Quasi-Steady-State Approximation,” *Bulletin of Mathematical Biology* 87 (2025): 73, doi:10.1007/s11538-025-01451-z; Kenneth A. Johnson and Roger S. Goody, “The Original Michaelis Constant: Translation of the 1913 Michaelis-Menten Paper,” *Biochemistry* 50 (2011): 8264--8269, doi:10.1021/bi201284u. [@Srivastava2025QSSA; @JohnsonGoody2011]

[^sk_growth_sources]: Jacques Monod, “The Growth of Bacterial Cultures,” *Annual Review of Microbiology* 3 (1949): 371--394, doi:10.1146/annurev.mi.03.100149.002103; Justus Wilhelm Fink et al., “Microbial population dynamics decouple growth response from environmental nutrient concentration,” *PNAS* 120 (2023): e2207295120, doi:10.1073/pnas.2207295120. [@Monod1949; @Fink2023Growth]
