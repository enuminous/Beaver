from beaver import BeaverEvaluator
from benchmark import risky_repair

state = {"defect_loss":1.0,"latency":0.40,"memory":0.45}

if __name__ == "__main__":
    full = BeaverEvaluator(
        "defect_loss",
        hard_bounds={"latency":(0,0.8),"memory":(0,0.9)},
        max_collateral=0.15,
        min_effectiveness=0.1
    )
    no_collateral = BeaverEvaluator(
        "defect_loss",
        hard_bounds={"latency":(0,2),"memory":(0,2)},
        max_collateral=10.0,
        min_effectiveness=0.1
    )
    print("full accepts risky repair:", full.evaluate(state, risky_repair).accepted)
    print("ablated accepts risky repair:", no_collateral.evaluate(state, risky_repair).accepted)
