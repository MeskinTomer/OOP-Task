from Rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, color: str, side: float):
        super().__init__(color, side, side)
