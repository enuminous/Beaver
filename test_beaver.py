import unittest
from beaver import BeaverEvaluator

class TestBeaver(unittest.TestCase):
    def test_good_repair_accepted(self):
        state = {"loss":1.0,"latency":0.2}
        def repair(s):
            s["loss"] = 0.5
            s["latency"] = 0.22
            return s
        ev = BeaverEvaluator("loss", {"latency":(0,1)}, max_collateral=0.1)
        self.assertTrue(ev.evaluate(state, repair).accepted)

    def test_bad_collateral_rejected(self):
        state = {"loss":1.0,"latency":0.2}
        def repair(s):
            s["loss"] = 0.2
            s["latency"] = 0.8
            return s
        ev = BeaverEvaluator("loss", {"latency":(0,1)}, max_collateral=0.1)
        self.assertFalse(ev.evaluate(state, repair).accepted)

    def test_bound_violation_rejected(self):
        state = {"loss":1.0,"latency":0.2}
        def repair(s):
            s["loss"] = 0.3
            s["latency"] = 1.2
            return s
        ev = BeaverEvaluator("loss", {"latency":(0,1)}, max_collateral=2)
        self.assertFalse(ev.evaluate(state, repair).accepted)

if __name__ == "__main__":
    unittest.main()
