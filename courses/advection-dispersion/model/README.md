# Advection, dispersion and aggregate loss reference packet

AD-NUMERICS-1. Source base b6f5fd80c963e8cd5b739e930893a0c7ec7c871a. Accepted scientific contract SHA256 d890ac5b46c239a9b64bfadf1cf4a1af5bdb2ec7e97a56f34deb3333166df75e. All coefficients, scenarios and observations are illustrative or synthetic. This packet supplies numerical verification and a proposed teaching default; final numerical/teaching acceptance belongs to Editor. Empirical validity, field calibration and learner outcomes are unestablished.

## Reproduce

Python 3 with the standard library is sufficient. Run from the unzipped packet directory:

```sh
python3 verify_advection.py --out reproduced-results
python3 readback_exports.py --results reproduced-results
```

This executes B01 through B08, independently refines the proposed core resolution, exports four core scenarios, tests the observation window, and generates the noiseless synthetic task and open answer tables. Nonzero exit means failed acceptance target or execution error; read verification.json and run-history. There is no downloaded calibration dataset or dependency install. Keep the supplied results directory as the pinned reference; use a new --out path for a readback run.

For one documented finite-column scenario:

```sh
python3 advection_model.py --out one-reactive-case --k 0.00001
```

This command exports the proposed default N=400, dt=100 s, observation window 600000 s. Its custom-report.json is a single-case report, not a rerun of all verification gates. Flags --n, --dt, --end, --L, --phi, --u, --D, --k, --C_ref and --Tp permit controlled changes. --D means the already combined D_L, not molecular diffusion added twice. The CLI accepts u=0 or D=0 for explicitly labeled mathematical auxiliary tests; they must not be presented as the default fed dispersive column. No independent outlet gradient is needed in the hyperbolic D=0 limit.

The verification program pins code and metric-definition hashes. SHA256SUMS.json pins the delivered payload; verify those hashes before comparing results. Floating-point bytes may differ on another Python/runtime platform, while the scientific tolerance tests remain the acceptance criterion. No platform-independent bitwise claim is made.

## Read the packet

model-interface.md defines concentration, flux, inventory, time support, half-cell inlet diagnostic and table units. metric-definitions.json was declared before resolution testing. results/verification.json contains measured errors, residuals, actual minima, refinement orders, proposed default resolution, scenarios and flags. verification-report.md explains conclusions and failed first attempt. contract-and-evidence contains the unchanged historically drafted but now accepted contract, analytical derivations, benchmark plan, literature ledger/access notes and Editor's acceptance receipt. They distinguish the finite steady, hyperbolic, periodic and closed problems.

The four core cases are conservative, reactive, faster-flow and more-dispersion. They use the same physical pulse duration. Faster flow doubles input dose; each recovery uses its own input. results/case-manifest.json pins coefficients, IC/BC, grid and window. Core profiles and face fluxes are sampled at fixed physical snapshot times; pulse budgets contain every update. All volumes and areas are explicit in model-interface.md. None of the CSVs is a field measurement.

no-python-readback.md explains calculations from the exported ledger and profiles. synthetic-inference-proposal.md defines the eight raw synthetic observations and three candidates; scores/residuals are separate openly available answer tables. Reading an answer table is not an independent model execution or an unaided learner attempt.

Only top-level advection_model.py, verify_advection.py and readback_exports.py are current executable sources. The latter does not execute the solver. run-history retains prior FAIL/PASS reports and exact attempted source copies for audit. The first periodic corner-assembly error is corrected in the current auxiliary checker. No failed benchmark was deleted, relaxed to hide failure, or silently clipped. The accepted oxygen package and Editor's shared source checkout were not changed or executed.

The original contract draft status lines are preserved for byte provenance. editor-scientific-contract-acceptance-r1.json is the subsequent authority for its implementation acceptance. Current numerical/default-resolution acceptance remains pending.
