from points import Point

class Rectangle:
    """Klasa reprezentująca prostokąt na płaszczyźnie."""

    def __init__(self, x1, y1, x2, y2):
        if x1 > x2 or y1 > y2: raise ValueError("Niepoprawne współrzędne")
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)

    def __str__(self):
        return f'[{self.pt1}, {self.pt2}]'

    def __repr__(self):
        return f'Rectangle({self.pt1.x}, {self.pt1.y}, {self.pt2.x}, {self.pt2.y})'

    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return self.pt1 == other.pt1 and self.pt2 == other.pt2
        return False

    def __ne__(self, other):
        return not self == other

    def area(self):
        return self.width * self.height

    def move(self, x, y):
        self.pt1 = Point(self.pt1.x + x, self.pt1.y + y)
        self.pt2 = Point(self.pt2.x + x, self.pt2.y + y)

    @classmethod
    def from_points(cls, points):
        if len(points) < 2: raise ValueError('Dwa punkty są wymagane do utworzenia prostokąta')
        p1, p2 = points
        return cls(p1.x, p1.y, p2.x, p2.y)

    @property
    def top(self):
        return self.pt2.y

    @property
    def bottom(self):
        return self.pt1.y

    @property
    def left(self):
        return self.pt1.x

    @property
    def right(self):
        return self.pt2.x

    @property
    def width(self):
        return self.pt2.x - self.pt1.x

    @property
    def height(self):
        return self.pt2.y - self.pt1.y

    @property
    def center(self):
        center_x = (self.pt1.x + self.pt2.x) / 2
        center_y = (self.pt1.y + self.pt2.y) / 2
        return Point(center_x, center_y)

    @property
    def topleft(self):
        return Point(self.pt1.x, self.pt2.y)

    @property
    def bottomleft(self):
        return self.pt1

    @property
    def topright(self):
        return self.pt2

    @property
    def bottomright(self):
        return Point(self.pt2.x, self.pt1.y)



