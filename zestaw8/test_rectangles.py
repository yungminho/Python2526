import pytest
from points import Point
from rectangle import Rectangle

def test_rectangle_creation():
    rect = Rectangle(0, 0, 4, 3)
    assert rect.pt1 == Point(0, 0)
    assert rect.pt2 == Point(4, 3)

    with pytest.raises(ValueError):
        Rectangle(4, 3, 0, 0)

def test_from_points():
    p1 = Point(0, 0)
    p2 = Point(4, 3)
    rect = Rectangle.from_points((p1, p2))
    assert rect.pt1 == p1
    assert rect.pt2 == p2

def test_virtual_attributes():
    rect = Rectangle(1, 2, 5, 6)
    assert rect.top == 6
    assert rect.bottom == 2
    assert rect.left == 1
    assert rect.right == 5
    assert rect.width == 4
    assert rect.height == 4

def test_corners():
    rect = Rectangle(1, 2, 5, 6)
    assert rect.topleft == Point(1, 6)
    assert rect.bottomleft == Point(1, 2)
    assert rect.topright == Point(5, 6)
    assert rect.bottomright == Point(5, 2)

def test_center():
    rect = Rectangle(0, 0, 4, 4)
    assert rect.center == Point(2, 2)

def test_area():
    rect = Rectangle(0, 0, 4, 3)
    assert rect.area() == 12

def test_move():
    rect = Rectangle(0, 0, 4, 3)
    rect.move(1, 1)
    assert rect.pt1 == Point(1, 1)
    assert rect.pt2 == Point(5, 4)
