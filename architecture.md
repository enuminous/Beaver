# BEAVER Architecture

## Pipeline

1. State Snapshotter
2. Repair Proposal Engine
3. Sandbox Executor
4. Constraint Checker
5. Target Effect Evaluator
6. Regression Analyzer
7. Dependency Impact Scanner
8. Rollback Verifier
9. Repair Ledger
10. Post-Repair Monitor

## Inputs

- current system state
- target defect
- candidate repair
- hard constraints
- regression tests
- downstream dependencies

## Outputs

```json
{
  "repair_effectiveness": 0.42,
  "collateral_impact": 0.05,
  "verification_score": 1.0,
  "rollback_verified": true,
  "bounded": true,
  "accepted": true
}
```

## Design principle

BEAVER separates:

**Can this change improve the target?**

from:

**Is this change safe enough to deploy?**

Those are different questions.

## Integration

JELLYFISH can identify downstream systems requiring regression checks.

ELEPHANT can preserve repair history and prior rollback states.

MAGPIE can audit evidence supporting repair claims.

WOLF can monitor post-repair latent degradation.
