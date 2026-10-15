# Verified oxygen model

Python 3.9 or later, standard library only. From the language directory run `python3 model/oxygen_model.py --out my-run` with a fresh output directory. Without Python, inspect the archived profiles and verification report.

Use a new path or an existing empty directory. Nonempty destinations are rejected before computation or writes, with their contents preserved. The current code adds only this output guard; the executed model identity and original results remain historical in `../provenance.json`. Commands in the archived verification report describe the original run; choose a fresh output for the current command.

`model-contract.md` defines units, assumptions and boundaries. `verification-report.md` and `results/verification.json` document analytical, conservation, convergence and synthetic-fit checks. All parameters and fitting observations are illustrative. Numerical verification does not establish field validity. The separate optional measured-data exercise is in `../../optional-observed-data/`.
