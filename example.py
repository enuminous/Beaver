from beaver import BeaverEvaluator

state = {
    "error_rate": 0.40,
    "latency": 0.30,
    "memory_load": 0.50
}

def repair(s):
    s["error_rate"] = 0.12
    s["latency"] = 0.34
    s["memory_load"] = 0.53
    return s

evaluator = BeaverEvaluator(
    target_metric="error_rate",
    hard_bounds={
        "latency": (0.0,0.8),
        "memory_load": (0.0,0.9)
    },
    max_collateral=0.12
)

result = evaluator.evaluate(
    state,
    repair,
    verifiers=[
        lambda s: s["error_rate"] < 0.2,
        lambda s: s["latency"] < 0.8
    ]
)

print(result)
