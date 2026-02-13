import math

class Point:
    """Klasa reprezentująca punkty na płaszczyźnie."""

    def __init__(self, x, y):  # konstuktor
        self.x = x
        self.y = y

    def __str__(self):         # zwraca string "(x, y)"
        return f"({self.x}, {self.y})"

    def __repr__(self):        # zwraca string "Point(x, y)"
        return f"Point({self.x}, {self.y})"

    def __eq__(self, other):   # obsługa point1 == point2
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        return False

    def __ne__(self, other):        # obsługa point1 != point2
        return not self == other

    # Punkty jako wektory 2D.
    def __add__(self, other):  # v1 + v2
        if isinstance(other, Point):
            return Point(self.x + other.x, self.y + other.y)
        return NotImplemented

    def __sub__(self, other):  # v1 - v2
        if isinstance(other, Point):
            return Point(self.x - other.x, self.y - other.y)
        return NotImplemented

    def __mul__(self, other):  # v1 * v2, iloczyn skalarny, zwraca liczbę
        if isinstance(other, Point):
            return self.x * other.x + self.y * other.y
        return NotImplemented

    def cross(self, other):         # v1 x v2, iloczyn wektorowy 2D, zwraca liczbę
        if isinstance(other, Point):
            return self.x * other.y - self.y * other.x
        return NotImplemented

    def length(self):          # długość wektora
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def __hash__(self):
        return hash((self.x, self.y))   # bazujemy na tuple, immutable points

# Kod testujący moduł.

import unittest

class TestPoint(unittest.TestCase):

    def setUp(self):
        self.point1 = Point(1, 2)
        self.point2 = Point(3, 4)
        self.point3 = Point(-1, -2)

    def test_str(self):
        self.assertEqual(str(self.point1), "(1, 2)")

    def test_repr(self):
        self.assertEqual(repr(self.point1), "Point(1, 2)")

    def test_eq(self):
        self.assertEqual(self.point1 == self.point2, False)
        self.assertEqual(self.point1 == Point(1, 2), True)

    def test_ne(self):
        self.assertEqual(self.point1 != self.point2, True)
        self.assertEqual(self.point1 != Point(1, 2), False)

    def test_add(self):
        self.assertEqual(self.point1 + self.point2, Point(4, 6))

    def test_sub(self):
        self.assertEqual(self.point1 - self.point2, Point(-2, -2))

    def test_mul(self):
        self.assertEqual(self.point3 * self.point2, -11)

    def test_cross(self):
        self.assertEqual(self.point3.cross(self.point2), 2)

    def test_length(self):
        self.assertEqual(self.point1.length(), math.sqrt(5))
        self.assertEqual(self.point3.length(), math.sqrt(5))

    def test_hash(self):
        self.assertEqual(hash(self.point1), hash((1, 2)))
        self.assertEqual(hash(self.point2), hash((3, 4)))
        self.assertEqual(hash(self.point3), hash((-1, -2)))

    def tearDown(self):
        self.zero = None


if __name__ == '__main__':
    unittest.main()