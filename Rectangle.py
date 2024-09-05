from Shape import Shape


class Rectangle(Shape):
    # Initializer
    def __init__(self, color: str, side_1: float, side_2: float):
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
        area = self.get_area() + other.get_area()
        perimeter = self.get_perimeter() + other.get_perimeter()
        return Shape(area=area, perimeter=perimeter)
