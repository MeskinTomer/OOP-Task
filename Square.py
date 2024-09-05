from Rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, color: str, side: float):
        # The initializer for the super class
        super().__init__(color, side, side)
