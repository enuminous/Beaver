# Limitations and Falsification

BEAVER is an experimental repair-safety framework.

## Limitations

- Safe repair depends on the completeness of test coverage.
- Unknown downstream effects may remain invisible.
- Rollback may not restore external side effects.
- Constraint sets may be incomplete.
- Cost functions may encode poor priorities.
- Sandbox behavior may differ from deployment behavior.

## Falsification criteria

BEAVER's central hypothesis is weakened if:

1. Standard regression testing plus rollback matches performance.
2. Collateral-impact modeling does not reduce failures.
3. Repair lineage has no measurable value.
4. Boundedness checks add no safety benefit.
5. Improvements vanish on held-out repair tasks.
6. The framework accepts repairs that consistently increase total harm.

## Claim boundary

BEAVER evaluates candidate repairs under specified constraints and tests. It cannot guarantee safety outside observed or modeled conditions.
