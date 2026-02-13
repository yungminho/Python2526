import unittest
from fracs import Frac

class TestFracs(unittest.TestCase):

    def setUp(self):
        self.frac1 = Frac(1,2)
        self.frac2 = Frac(3,3)

    def test_str(self):
        self.assertEqual(str(self.frac1), "1/2")
        self.assertEqual(str(self.frac2), "1")

    def test_repr(self):
        self.assertEqual(repr(self.frac1), "Frac(1, 2)")
        self.assertEqual(repr(self.frac2), "Frac(1, 1)")

    def test_eq(self):
        self.assertEqual(self.frac1 == self.frac2, False)

    def test_ne(self):
        self.assertEqual(self.frac1 != self.frac2, True)

    def test_lt(self):
        self.assertEqual(self.frac1 < self.frac2, True)

    def test_gt(self):
        self.assertEqual(self.frac1 > self.frac2, False)

    def test_le(self):
        self.assertEqual(self.frac1 <= self.frac2, True)

    def test_ge(self):
        self.assertEqual(self.frac1 >= self.frac2, False)

    def test_add(self):
        self.assertEqual(self.frac1 + self.frac2, Frac(9, 6))

    def test_radd(self):
        self.assertEqual(3.5 + self.frac1, Frac(4, 1))

    def test_sub(self):
        self.assertEqual(self.frac1 - self.frac2, Frac(-1, 2))

    def test_rsub(self):
        self.assertEqual(self.frac2 - self.frac1, Frac(1, 2))

    def test_mul(self):
        self.assertEqual(self.frac1 * self.frac2, Frac(1, 2))

    def test_rmul(self):
        self.assertEqual(3 * self.frac1, Frac(3, 2))

    def test_truediv(self):
        self.assertEqual(self.frac1 / self.frac2, Frac(1, 2))

    def test_rtruediv(self):
        self.assertEqual(1.0 / self.frac1, Frac(2, 1))

    def test_pos(self):
        self.assertEqual(+self.frac1, self.frac1)
        self.assertEqual(+Frac(-1, 2), self.frac1)

    def test_neg(self):
        self.assertEqual(-self.frac1, Frac(-1, 2))

    def test_invert(self):
        self.assertEqual(~self.frac1, Frac(2, 1))

    def test_float(self):
        self.assertEqual(float(self.frac1), 0.5)

    def test_hash(self):
        self.assertEqual(hash(self.frac1), hash(Frac(2, 4)))

    def tearDown(self):
        self.frac1 = None
        self.frac2 = None

if __name__ == '__main__':
    unittest.main()