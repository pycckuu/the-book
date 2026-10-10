# Decisions and open questions for contract acceptance

The proposed package is bounded to a single dissolved species with prescribed steady flow, a finite-column flux inlet and a zero dispersive-gradient/advective outlet. It does not extend the biology or rewrite the oxygen module.

Q01, recommended contract choice: use this finite column as the bridge to groundwater, not label it a whole aquifer or a sealed sediment column. The proposed boundary flux gives a known injected dose. If Editor instead wants an imposed resident concentration reservoir, the inlet and analytical/accounting references need explicit revision before implementation. No user decision is needed unless the intended story changes.

Q02, provisional coefficient choice: accept or adjust the candidate mathematical scales and the Pe=10 conservative/reactive pair before publishing numerical examples. They are not fitted parameters or field values. No particular tracer chemical is named; naming one later would require evidence for its non-sorption/reactivity assumptions.

Q03, reference and scheme choice: accept a transparent first-order upwind FV/backward-Euler baseline, with its numerical spreading exposed and verified, plus the finite steady and auxiliary smooth checks. Higher-order/adaptive/multidomain methods are outside this sequel. If the required observable accuracy makes the baseline impractical after implementation, return that evidence to Editor rather than silently change the contract.

Q04, empirical comparison: no raw independent concentration dataset is selected. The default next gate can use explicitly synthetic scenarios and a literature critique. Any empirical calibration/validation requires its own frozen data provenance, sampling-mode definition and uncertainty; source abstracts do not constitute model validation data.

Q05, unresolved scientific attribution: parent disappearance can result from several mechanisms; a single first-order fit cannot uniquely establish microbial degradation, products or water safety. A one-region model also cannot infer immobile storage or microbial transport parameters. These limits remain even after perfect numerical verification.

Q06, unchanged prior issue: oxygen archive/publication calculation lineage remains unresolved and belongs to the earlier observational task. No successor numerical or chemical interpretation of those workbooks is made here.

Deliverables go to BOOK Editor in Chief for this scientific gate. Teaching workload, Russian translation, manuscript placement and final rendered integration remain their assigned owners' decisions. Answers remain open under the user's current instruction. No publication or next merge authority is inferred from the completed oxygen PR.
