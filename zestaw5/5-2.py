# Stworzyć plik fracs.py i zapisać w nim funkcje do działań na ułamkach.
# Ułamek będzie reprezentowany przez listę dwóch liczb całkowitych [licznik, mianownik].
# Napisać kod testujący moduł fracs. Nie należy korzystać z klasy Fraction z modułu fractions.
# Można wykorzystać funkcję fractions.gcd() [Py2, zwraca liczby dodatnie lub ujemne]
# lub math.gcd() [Py3, zwraca liczby nieujemne] implementującą algorytm Euklidesa.

#from fractions import gcd   # Py2
from math import gcd   # Py3

def add_frac(frac1, frac2): # frac1 + frac2
    numerator1, denominator1 = frac1
    numerator2, denominator2 = frac2

    numerator = numerator1 * denominator2 + numerator2 * denominator1
    denominator = denominator1 * denominator2
    return simplify([numerator, denominator])

def sub_frac(frac1, frac2): # frac1 - frac2
    numerator1, denominator1 = frac1
    numerator2, denominator2 = frac2

    numerator = numerator1 * denominator2 - numerator2 * denominator1
    denominator = denominator1 * denominator2
    return simplify([numerator, denominator])

def mul_frac(frac1, frac2): # frac1 * frac2
    numerator1, denominator1 = frac1
    numerator2, denominator2 = frac2

    numerator = numerator1 * numerator2
    denominator = denominator1 * denominator2
    return simplify([numerator, denominator])

def div_frac(frac1, frac2): # frac1 / frac2
    if is_zero(frac2): raise ZeroDivisionError

    numerator1, denominator1 = frac1
    numerator2, denominator2 = frac2

    numerator = numerator1 * denominator2
    denominator = denominator1 * numerator2
    return simplify([numerator, denominator])

def is_positive(frac): # bool, czy dodatni
    return frac2float(frac) > 0

def is_zero(frac): # bool, typu [0, x]
    return frac[0] == 0

def cmp_frac(frac1, frac2): # -1 | 0 | +1
    numerator1, denominator1 = frac1
    numerator2, denominator2 = frac2

    val1 = numerator1 * denominator2
    val2 = numerator2 * denominator1
    if val1 < val2: return -1
    elif val1 == val2: return 0
    else: return 1

def frac2float(frac): # konwersja do float
    numerator, denominator = frac
    return numerator / denominator

def simplify(frac):
    numerator, denominator = frac
    divisor = gcd(numerator, denominator)
    return [numerator // divisor, denominator // divisor]

# f1 = [-1, 2]      # -1/2
# f2 = [1, -2]      # -1/2 (niejednoznaczność)
# f3 = [0, 1]       # zero
# f4 = [0, 2]       # zero (niejednoznaczność)
# f5 = [3, 1]       # 3
# f6 = [6, 2]       # 3 (niejednoznaczność)

import unittest

class TestFractions(unittest.TestCase):

    # --- add_frac ---
    def test_add_frac_basic(self):
        self.assertEqual(add_frac([1, 2], [1, 3]), [5, 6])
    def test_add_frac_with_negatives(self):
        self.assertEqual(add_frac([-1, 2], [3, 4]), [1, 4])
    def test_add_frac_with_zero(self):
        self.assertEqual(add_frac([0, 1], [2, 3]), [2, 3])
    def test_add_frac_reduction(self):
        self.assertEqual(add_frac([2, 4], [1, 4]), [3, 4])

    # --- sub_frac ---
    def test_sub_frac_basic(self):
        self.assertEqual(sub_frac([3, 4], [1, 2]), [1, 4])
    def test_sub_frac_negative_result(self):
        self.assertEqual(sub_frac([1, 3], [3, 4]), [-5, 12])

    # --- mul_frac ---
    def test_mul_frac_basic(self):
        self.assertEqual(mul_frac([2, 3], [3, 4]), [1, 2])
    def test_mul_frac_with_zero(self):
        self.assertEqual(mul_frac([0, 5], [2, 3]), [0, 1])
    def test_mul_frac_with_negatives(self):
        self.assertEqual(mul_frac([-1, 2], [-2, 3]), [1, 3])

    # --- div_frac ---
    def test_div_frac_basic(self):
        self.assertEqual(div_frac([3, 4], [2, 3]), [9, 8])
    def test_div_frac_negative(self):
        self.assertEqual(div_frac([-1, 2], [1, 4]), [-2, 1])
    def test_div_frac_zero_numerator(self):
        self.assertEqual(div_frac([0, 1], [3, 5]), [0, 1])
    def test_div_frac_by_zero_denominator(self):
        with self.assertRaises(ZeroDivisionError):
            div_frac([1, 2], [0, 1])

    # --- is_positive ---
    def test_is_positive_true(self):
        self.assertTrue(is_positive([3, 4]))
    def test_is_positive_false_negative_numerator(self):
        self.assertFalse(is_positive([-3, 4]))
    def test_is_positive_false_negative_denominator(self):
        self.assertFalse(is_positive([3, -4]))
    def test_is_positive_zero(self):
        self.assertFalse(is_positive([0, 5]))

    # --- is_zero ---
    def test_is_zero_true(self):
        self.assertTrue(is_zero([0, 5]))
    def test_is_zero_false(self):
        self.assertFalse(is_zero([1, 5]))
    def test_is_zero_negative_zero(self):
        self.assertTrue(is_zero([0, -3]))

    # --- cmp_frac ---
    def test_cmp_frac_equal(self):
        self.assertEqual(cmp_frac([1, 2], [2, 4]), 0)
    def test_cmp_frac_less(self):
        self.assertEqual(cmp_frac([1, 3], [1, 2]), -1)
    def test_cmp_frac_greater(self):
        self.assertEqual(cmp_frac([3, 2], [4, 3]), 1)

    # --- frac2float ---
    def test_frac2float_basic(self):
        self.assertAlmostEqual(frac2float([1, 2]), 0.5, places=9)
    def test_frac2float_negative(self):
        self.assertAlmostEqual(frac2float([-3, 4]), -0.75, places=9)
    def test_frac2float_zero(self):
        self.assertEqual(frac2float([0, 5]), 0.0)

    def tearDown(self):
        self.zero = None

if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie testy