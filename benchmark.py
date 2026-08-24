from beaver import BeaverEvaluator

def safe_repair(s):
    s["defect_loss"] *= 0.35
    s["latency"] += 0.03
    s["memory"] += 0.02
    return s

def risky_repair(s):
    s["defect_loss"] *= 0.10
    s["latency"] += 0.45
    s["memory"] += 0.35
    return s

def run():
    state = {"defect_loss":1.0,"latency":0.40,"memory":0.45}
    ev = BeaverEvaluator(
        "defect_loss",
        hard_bounds={"latency":(0,0.8),"memory":(0,0.9)},
        max_collateral=0.15,
        min_effectiveness=0.1
    )
    verifier = [lambda s: s["latency"] < 0.8, lambda s: s["memory"] < 0.9]
    safe = ev.evaluate(state, safe_repair, verifier)
    risky = ev.evaluate(state, risky_repair, verifier)
    return safe, risky

if __name__ == "__main__":
    safe,risky = run()
    print("safe:", safe)
    print("risky:", risky)
