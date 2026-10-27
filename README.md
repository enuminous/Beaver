# BEAVER — EFMW Zoo #29

<!-- ENUMINOUS-UNIFIED-NAV:START -->
## Repository navigation

**eNuminous network:** [All public repositories](https://github.com/enuminous/EFMW/blob/main/REPOSITORY_NAVIGATION.md) · [EFMW](https://github.com/enuminous/EFMW) · [102 equations](https://github.com/enuminous/Monolithic_102_EFMW) · [Frozen Lean](https://github.com/enuminous/Monolithic-102-Zoo-Lean4) · [Zoo](https://github.com/enuminous/Tortoise) · [Papers](https://github.com/enuminous/papers) · [Quantum geometry](https://github.com/enuminous/Base888-Quantum-Geometry)

**This project:** [Repository home](https://github.com/enuminous/Beaver) · [Subject index](https://github.com/enuminous/EFMW/blob/main/REPOSITORY_NAVIGATION.md#zoo-index-and-agents)

<details open>
<summary><strong>On this page</strong></summary>

- [Core question](#core-question)
- [Primary outputs](#primary-outputs)
- [Repository contents](#repository-contents)
- [Quick start](#quick-start)
- [Zoo position](#zoo-position)


</details>

**Related repositories:** [Tortoise](https://github.com/enuminous/Tortoise) · [Monolithic-Zoo-Lean4](https://github.com/enuminous/Monolithic-Zoo-Lean4) · [Monolithic-102-Zoo-Lean4](https://github.com/enuminous/Monolithic-102-Zoo-Lean4) · [Mantis](https://github.com/enuminous/Mantis) · [Jellyfish](https://github.com/enuminous/Jellyfish) · [Bison](https://github.com/enuminous/Bison) · [Chameleon](https://github.com/enuminous/Chameleon)

> **Evidence boundary:** A link between projects is navigation, not an assertion of proven equivalence, experimental validation, or shared authorship. See each repository’s own status and review notes.
<!-- ENUMINOUS-UNIFIED-NAV:END -->


**Bounded Environmental Adaptation, Verification and Error Repair**

BEAVER is an experimental EFMW-inspired framework for evaluating whether a system can adapt to damage or changing conditions while keeping repairs bounded, testable, reversible, and less harmful than the defect they are intended to fix.

## Core question

> Can the system repair itself without creating a larger failure somewhere else?

BEAVER focuses on safe adaptation rather than unconstrained optimization.

## Primary outputs

- repair effectiveness
- collateral-impact score
- rollback readiness
- verification completeness
- boundedness compliance
- regression burden
- recovery confidence

## Repository contents

- `theory.md`
- `architecture.md`
- `repair_model.md`
- `limitations.md`
- `beaver.py`
- `benchmark.py`
- `ablations.py`
- `test_beaver.py`
- `example.py`
- `paper.md`
- `CITATION.cff`
- `LICENSE`

## Quick start

```bash
python example.py
python benchmark.py
python ablations.py
python -m unittest test_beaver.py
```

## Zoo position

JELLYFISH #28 maps how local degradation spreads.

**BEAVER #29 asks whether the system can intervene on that damage safely, verify the repair, and reverse it if needed.**
