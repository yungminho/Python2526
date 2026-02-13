# W pliku fracs.py zdefiniować klasę Frac wraz z potrzebnymi metodami.
# Ułamek jest reprezentowany przez parę liczb całkowitych.
# Napisać kod testujący moduł fracs.

#from fractions import gcd   # Py2
from math import gcd, floor  # Py3

class Frac:
    """Klasa reprezentująca ułamek."""

    def __init__(self, x=0, y=1):
        self.x = x
        self.y = y

    def __simplify(self):
        numerator, denominator = self.x, self.y
        divisor = gcd(numerator, denominator)
        numerator //= divisor
        denominator //= divisor
        if denominator < 0:
            numerator = -numerator
            denominator = -denominator
        return Frac(numerator, denominator)

    def __str__(self):          # zwraca "x/y" lub "x" dla y=1
        return f"{self.x}/{self.y}" if self.y != 1 else str(self.x)

    def __repr__(self):        # zwraca "Frac(x, y)"
        return f"Frac({self.x}, {self.y})"

    #def __cmp__(self, other): pass  # cmp(frac1, frac2)    # Py2

    def __eq__(self, other):         # Py2.7 i Py3
        if isinstance(other, int):
            other = Frac(other, 1)
        elif not isinstance(other, Frac):
            return NotImplemented

        s = self.__simplify()
        o = other.__simplify()
        return s.x == o.x and s.y == o.y

    def __ne__(self, other):
        if isinstance(other, int):
            other = Frac(other, 1)
        elif not isinstance(other, Frac):
            return NotImplemented

        s = self.__simplify()
        o = other.__simplify()
        return s.x != o.x or s.y != o.y

    def __lt__(self, other):
        if isinstance(other, int):
            other = Frac(other, 1)
        elif not isinstance(other, Frac):
            return NotImplemented

        s = self.__simplify()
        o = other.__simplify()
        return s.x * o.y < o.x * s.y

    def __le__(self, other):
        if isinstance(other, int):
            other = Frac(other, 1)
        elif not isinstance(other, Frac):
            return NotImplemented

        return self == other or self < other

    def __gt__(self, other):
        if isinstance(other, int):
            other = Frac(other, 1)
        elif not isinstance(other, Frac):
            return NotImplemented

        return other < self

    def __ge__(self, other):
        if isinstance(other, int):
            other = Frac(other, 1)
        elif not isinstance(other, Frac):
            return NotImplemented

        return self == other or self > other

    def __add__(self, other):  # frac1 + frac2
        if isinstance(other, int):
            other = Frac(other, 1)
        elif not isinstance(other, Frac):
            return NotImplemented

        numerator1, denominator1 = self.x, self.y
        numerator2, denominator2 = other.x, other.y

        numerator = numerator1 * denominator2 + numerator2 * denominator1
        denominator = denominator1 * denominator2
        return Frac(numerator, denominator).__simplify()

    def __sub__(self, other):  # frac1 - frac2
        if isinstance(other, int):
            other = Frac(other, 1)
        elif not isinstance(other, Frac):
            return NotImplemented

        numerator1, denominator1 = self.x, self.y
        numerator2, denominator2 = other.x, other.y

        numerator = numerator1 * denominator2 - numerator2 * denominator1
        denominator = denominator1 * denominator2
        return Frac(numerator, denominator).__simplify()

    def __mul__(self, other):  # frac1 * frac2
        if isinstance(other, int):
            other = Frac(other, 1)
        elif not isinstance(other, Frac):
            return NotImplemented

        numerator1, denominator1 = self.x, self.y
        numerator2, denominator2 = other.x, other.y

        numerator = numerator1 * numerator2
        denominator = denominator1 * denominator2
        return Frac(numerator, denominator).__simplify()

    # def __div__(self, other):  # frac1 / frac2, Py2

    def __truediv__(self, other):  # frac1 / frac2, Py3
        if isinstance(other, int):
            other = Frac(other, 1)
        elif not isinstance(other, Frac):
            return NotImplemented

        if other.x== 0: raise ZeroDivisionError

        numerator1, denominator1 = self.x, self.y
        numerator2, denominator2 = other.x, other.y

        numerator = numerator1 * denominator2
        denominator = denominator1 * numerator2
        return Frac(numerator, denominator).__simplify()

    def __floordiv__(self, other):  # frac1 // frac2, opcjonalnie
        if isinstance(other, int):
            other = Frac(other, 1)
        elif not isinstance(other, Frac):
            return NotImplemented

        return floor(float(self) / float(other))

    def __mod__(self, other):  # frac1 % frac2, opcjonalnie
        if isinstance(other, int):
            other = Frac(other, 1)
        elif not isinstance(other, Frac):
            return NotImplemented

        q = (self.x * other.y) // (self.y * other.x)
        r = Frac(self.x * other.y - q * self.y * other.x,
                 self.y * other.y)
        return r.__simplify()

    # operatory jednoargumentowe
    def __pos__(self):  # +frac = (+1)*frac
        return self

    def __neg__(self):  # -frac = (-1)*frac
        return Frac(-self.x, self.y)

    def __invert__(self):  # odwrotnosc: ~frac
        return Frac(self.y, self.x)

    def __float__(self):       # float(frac)
        return self.x / self.y

    def __hash__(self):
        #return hash(float(self))   # immutable fracs
        # w Pythonie set([2]) == set([2.0])
        # chcemy set([2]) == set([Frac(2)])
        s = self.__simplify()
        return hash((s.x, s.y)) if s.y != 1 else hash(s.x)

# Kod testujący moduł.

import unittest

class TestFrac(unittest.TestCase):
    def test_repr_and_str(self):
        self.assertEqual(str(Frac(3, 4)), "3/4")
        self.assertEqual(str(Frac(5, 1)), "5")
        self.assertEqual(repr(Frac(3, 4)), "Frac(3, 4)")

    def test_equality(self):
        self.assertTrue(Frac(1, 2) == Frac(2, 4))
        self.assertFalse(Frac(1, 2) == Frac(2, 3))
        self.assertTrue(Frac(2, 4) != Frac(2, 3))

    def test_comparisons(self):
        self.assertTrue(Frac(1, 2) < Frac(3, 4))
        self.assertTrue(Frac(2, 3) > Frac(1, 3))
        self.assertTrue(Frac(4, 6) <= Frac(2, 3))
        self.assertTrue(Frac(1, 2) >= Frac(1, 4))

    def test_add(self):
        self.assertEqual(Frac(1, 2) + Frac(1, 3), Frac(5, 6))
        self.assertEqual(Frac(3, 4) + Frac(1, 4), Frac(1, 1))

    def test_sub(self):
        self.assertEqual(Frac(1, 2) - Frac(1, 3), Frac(1, 6))
        self.assertEqual(Frac(3, 4) - Frac(1, 4), Frac(1, 2))

    def test_mul(self):
        self.assertEqual(Frac(2, 3) * Frac(3, 4), Frac(1, 2))
        self.assertEqual(Frac(5, 6) * Frac(6, 5), Frac(1, 1))

    def test_div(self):
        self.assertEqual(Frac(1, 2) / Frac(1, 4), Frac(2, 1))
        with self.assertRaises(ZeroDivisionError):
            Frac(1, 2) / Frac(0, 1)

    def test_floordiv(self):
        self.assertEqual(Frac(7, 2) // Frac(3, 2), 2)
        self.assertEqual(Frac(1, 3) // Frac(2, 3), 0)

    def test_mod(self):
        self.assertEqual(Frac(7, 3) % Frac(2, 3), Frac(1, 3))
        self.assertEqual(Frac(5, 4) % Frac(1, 2), Frac(1, 4))

    def test_unary_ops(self):
        self.assertEqual(+Frac(3, 4), Frac(3, 4))
        self.assertEqual(-Frac(3, 4), Frac(-3, 4))
        self.assertEqual(~Frac(2, 3), Frac(3, 2))

    def test_float(self):
        self.assertAlmostEqual(float(Frac(1, 2)), 0.5)
        self.assertAlmostEqual(float(Frac(2, 4)), 0.5)

    def test_hash(self):
        self.assertEqual(hash(Frac(1, 2)), hash(Frac(2, 4)))
        s = {Frac(1, 2), Frac(2, 4), Frac(3, 6)}
        self.assertEqual(len(s), 1)

    def tearDown(self):
        self.zero = None

if __name__ == "__main__":
    unittest.main()