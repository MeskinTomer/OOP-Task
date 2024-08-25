from Shape import Shape


class Rectangle(Shape):
    def __init__(self, color: str, side_1: float, side_2: float):
        area = side_1 * side_2
        perimeter = (side_1 + side_2) * 2
        super().__init__(color, area, perimeter)
        