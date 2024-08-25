from Shape import Shape
from math import pi


class Circle(Shape):
    def __init__(self, color: str, radius: float):
        area = radius ** 2 * pi
        perimeter = 2 * pi * radius
        super().__init__(color, area, perimeter)
