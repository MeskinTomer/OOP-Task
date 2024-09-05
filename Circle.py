from Shape import Shape
from math import pi


class Circle(Shape):
    def __init__(self, color: str, radius: float):
        # The area of the Rectangle
        area = radius ** 2 * pi
        # The perimeter of the Rectangle
        perimeter = 2 * pi * radius
        # The initializer for the super class
        super().__init__(color, area, perimeter)
