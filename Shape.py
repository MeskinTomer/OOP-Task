class Shape:
    # Initializer
    def __init__(self, color: str = 'White', area: float = 1, perimeter: float = 1):
        # Asserts
        assert isinstance(color, str), "Color must be a string"
        assert isinstance(area, (int, float)) and area > 0, "Area must be a positive number"
        assert isinstance(perimeter, (int, float)) and perimeter > 0, "Perimeter must be a positive number"

        # The color of the shape
        self.color = color
        # The area of the shape
        self.area = area
        # The perimeter of the shape
        self.perimeter = perimeter

    # Methods
    def set_color(self, color: str) -> None:
        """
        Sets the color of the object
        :param color: The color to be set
        :type: str
        :return: None
        """
        assert isinstance(color, str), "Color must be a string"
        self.color = color

    def get_color(self) -> str:
        """
        Returns the color of the object
        :return: The shape's color
        :rtype: str
        """
        return self.color

    def get_area(self) -> float:
        """
        Returns the area of the object
        :return: The shape's area
        :rtype: float
        """
        return self.area

    def get_perimeter(self) -> float:
        """
        Returns the perimeter of the object
        :return: The shape's perimeter
        :rtype: float
        """
        return self.perimeter

    def __str__(self):
        """
        String override
        :return: The intended form of string
        :rtype: str
        """
        return f'Color: {self.color}, Area: {self.area}, Perimeter: {self.perimeter}'
