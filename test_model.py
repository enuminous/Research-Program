import math
import unittest
from MODEL import simulate, fieldspace_counts

class TestModel(unittest.TestCase):
    def test_counts(self):
        self.assertEqual(fieldspace_counts(), (165,45,9))
    def test_zero_drive_zero_initial(self):
        self.assertTrue(all(c == 0 for _, c, _ in simulate(alpha=0)))
    def test_nonzero_drive(self):
        self.assertGreater(max(abs(c) for _, c, _ in simulate(alpha=0.7)), 0.1)
    def test_damping(self):
        r=simulate(alpha=0,c0=1.0)
        self.assertLess(abs(r[-1][1]), abs(r[0][1]))
    def test_finite(self):
        self.assertTrue(all(math.isfinite(c) for _,c,_ in simulate(alpha=0.7)))

if __name__ == '__main__': unittest.main()
