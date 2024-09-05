from Shape import Shape


class Rectangle(Shape):
    # Initializer
    def __init__(self, color: str, side_1: float, side_2: float):
        # Assert side lengths are positive
        assert isinstance(side_1, (int, float)) and side_1 > 0, "side_1 must be a positive number"
        assert isinstance(side_2, (int, float)) and side_2 > 0, "side_2 must be a positive number"

        # The area of the Rectangle
        area = side_1 * side_2
        # The perimeter of the Rectangle
        perimeter = (side_1 + side_2) * 2
        # The initializer for the super class
        super().__init__(color, area, perimeter)

    # Methods
    def __add__(self, other):
        """
        Overrides the add function for 2 "Rectangle" objects
        :param other: The other object to be added
        :type: Rectangle
        :return: The sum object
        :rtype: Rectangle
        """

        # Asserts the 'other' instance is a Rectangle
        assert isinstance(other, Rectangle), "Can only add another Rectangle"

        area = self.get_area() + other.get_area()
        perimeter = self.get_perimeter() + other.get_perimeter()
        return Shape(area=area, perimeter=perimeter)
