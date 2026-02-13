from math import gcd

class Frac:
    """Klasa reprezentująca ułamki."""

    def __init__(self, x=0, y=1):
        if y == 0: raise ValueError('Mianownik nie może być zerem')
        self.x = x
        self.y = y
        self.simplify()

    def __str__(self):
        return f'{self.x}' if self.y == 1 else f'{self.x}/{self.y}'

    def __repr__(self):
        return f'Frac({self.x}, {self.y})'

    def __eq__(self, other):
        other = self.ensure_frac(other)
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return not self == other

    def __lt__(self, other):
        other = self.ensure_frac(other)
        return self.x * other.y < self.y * other.x

    def __le__(self, other):
        return self < other or self == other

    def __gt__(self, other):
        other = self.ensure_frac(other)
        return self.x * other.y > self.y * other.x

    def __ge__(self, other):
        return self > other or self == other

    def __add__(self, other):
        other = self.ensure_frac(other)
        return Frac(self.x * other.y + self.y * other.x, self.y * other.y)

    __radd__ = __add__

    def __sub__(self, other):
        other = self.ensure_frac(other)
        return Frac(self.x * other.y - self.y * other.x, self.y * other.y)

    def __rsub__(self, other):
        other = self.ensure_frac(self)
        return other - self

    def __mul__(self, other):
        other = self.ensure_frac(other)
        return Frac(self.x * other.x, self.y * other.y)

    __rmul__ = __mul__

    def __truediv__(self, other):
        other = self.ensure_frac(other)
        if other.x == 0: raise ZeroDivisionError
        return Frac(self.x * other.y, self.y * other.x)

    def __rtruediv__(self, other):
        other = self.ensure_frac(other)
        return other / self

    # operatory jednoargumentowe
    def __pos__(self):
        if self.x >= 0: return self
        if self.x < 0: return Frac(-1 * self.x, self.y)

    def __neg__(self):
        return Frac(-self.x, self.y)

    def __invert__(self):
        if self.x == 0: raise ZeroDivisionError
        return Frac(self.y, self.x)

    def __float__(self):
        return self.x / self.y

    def __hash__(self):
        return hash((self.x, self.y))

    def simplify(self):
        """Uproszczenie ułamka."""
        divisor = gcd(self.x, self.y)
        self.x //= divisor
        self.y //= divisor
        if self.y < 0:
            self.x = -self.x
            self.y = -self.y

    def ensure_frac(self, value):
        if isinstance(value, Frac):
            return value
        elif isinstance(value, int):
            return Frac(value)
        elif isinstance(value, float):
            numerator, denominator = value.as_integer_ratio()
            return Frac(numerator, denominator)
        else:
            raise TypeError("Nie można skonwertować na ułamek.")