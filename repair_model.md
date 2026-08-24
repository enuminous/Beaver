# Repair Model

## Repair proposal schema

```json
{
  "repair_id": "r17",
  "target": "module-B",
  "expected_gain": 0.35,
  "estimated_cost": 0.10,
  "reversible": true,
  "constraints": ["latency<0.8", "memory<0.9"]
}
```

## Evaluation stages

1. snapshot pre-repair state
2. apply candidate repair in sandbox
3. measure target improvement
4. measure collateral regressions
5. verify invariants
6. estimate utility
7. accept or reject
8. if accepted, preserve rollback state
9. monitor post-deployment drift

## Repair acceptance

A candidate repair may be accepted when:

`E > theta_E`

`C < theta_C`

`V >= theta_V`

and all hard constraints pass.

## Regression burden

`B_reg = number_of_new_failures + weighted_severity`

## Rollback test

A repair should be marked high-risk if:

`rollback_verified = false`

for a high-impact change.
