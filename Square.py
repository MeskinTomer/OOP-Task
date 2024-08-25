from Shape import Shape


class Square(Shape):
    def __init__(self, color: str, side: float):
        area = side ** 2
        perimeter = side * 4
        super().__init__(color, area, perimeter)
