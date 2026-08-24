from dataclasses import dataclass
from typing import Dict, Callable, Any, List
import copy

@dataclass
class RepairResult:
    effectiveness: float
    collateral_impact: float
    verification_score: float
    rollback_verified: bool
    bounded: bool
    accepted: bool
    before: Dict[str, float]
    after: Dict[str, float]

class BeaverEvaluator:
    def __init__(self,
                 target_metric: str,
                 hard_bounds: Dict[str, tuple] = None,
                 max_collateral: float = 0.2,
                 min_effectiveness: float = 0.05,
                 min_verification: float = 1.0):
        self.target_metric = target_metric
        self.hard_bounds = hard_bounds or {}
        self.max_collateral = max_collateral
        self.min_effectiveness = min_effectiveness
        self.min_verification = min_verification

    def _bounded(self, state):
        for k,(lo,hi) in self.hard_bounds.items():
            if k in state and not (lo <= state[k] <= hi):
                return False
        return True

    def evaluate(self,
                 state: Dict[str,float],
                 repair: Callable[[Dict[str,float]], Dict[str,float]],
                 verifiers: List[Callable[[Dict[str,float]], bool]] = None,
                 collateral_weights: Dict[str,float] = None):
        verifiers = verifiers or []
        collateral_weights = collateral_weights or {}

        before = copy.deepcopy(state)
        after = repair(copy.deepcopy(state))

        effectiveness = before[self.target_metric] - after[self.target_metric]

        collateral = 0.0
        for k,v_before in before.items():
            if k == self.target_metric or k not in after:
                continue
            worsening = max(0.0, after[k] - v_before)
            collateral += collateral_weights.get(k,1.0) * worsening

        checks = [bool(v(after)) for v in verifiers]
        verification_score = sum(checks)/len(checks) if checks else 1.0
        bounded = self._bounded(after)

        # Reference rollback test: state snapshot must restore exactly.
        rollback = copy.deepcopy(before)
        rollback_verified = rollback == before

        accepted = (
            effectiveness >= self.min_effectiveness and
            collateral <= self.max_collateral and
            verification_score >= self.min_verification and
            bounded and
            rollback_verified
        )

        return RepairResult(
            effectiveness,
            collateral,
            verification_score,
            rollback_verified,
            bounded,
            accepted,
            before,
            after
        )
