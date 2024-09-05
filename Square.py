from Rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, color: str, side: float):
        # Assert that side is a positive number
        assert isinstance(side, (int, float)) and side > 0, "Side length must be a positive number"

        # The initializer for the super class
        super().__init__(color, side, side)
