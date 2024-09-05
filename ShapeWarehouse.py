import random
from Rectangle import Rectangle
from Square import Square
from Circle import Circle
from Shape import Shape


class ShapeWarehouse:
    # Initializer
    def __init__(self, colors: list, lengths: list):
        # Assert that lengths contain only positive numbers
        assert all(isinstance(length, (int, float)) and length > 0 for length in
                   lengths), "All lengths must be positive numbers"

        # The colors list
        self.colors = colors
        # The lengths list
        self.lengths = lengths
        # The shapes list of the object
        self.shapes = []

    # Methods
    def __create_shape(self) -> Shape:
        """
        Creates a shape using the lists of the object
        :return: the created shape
        :rtype: Shape
        """
        shapes = ['Rectangle', 'Square', 'Circle']
        shape = random.choice(shapes)
        if shape == 'Rectangle':
            temp = Rectangle(random.choice(self.colors), random.choice(self.lengths), random.choice(self.lengths))
        elif shape == 'Square':
            temp = Square(random.choice(self.colors), random.choice(self.lengths))
        else:
            temp = Circle(random.choice(self.colors), random.choice(self.lengths))
        return temp

    def generate(self, x: int) -> None:
        """
        Generates x amount of shapes using the create_shape method and
        inserts them into the object's shapes list
        :param x: The amount of shapes to be created
        :type: int
        :return: None
        """
        for i in range(x):
            temp = self.__create_shape()
            self.shapes.append(temp)

    def sum_areas(self) -> float:
        """
        Calculates and returns the sum of the areas of the shapes in
        the shapes list of the object
        :return: The sum
        :rtype: float
        """
        sum_area = float(0)
        for shape in self.shapes:
            sum_area += shape.get_area()
        return sum_area

    def sum_perimeters(self) -> float:
        """
        Calculates and returns the sum of the perimeters of the shapes in
        the shapes list of the object
        :return: The sum
        :rtype: float
        """
        sum_perimeter = float(0)
        for shape in self.shapes:
            sum_perimeter += shape.get_perimeter()
        return sum_perimeter

    def count_colors(self):
        """
        Creates a dictionary that contains counts of the colors of the shapes
        in the shapes list of the object
        :return: The dictionary
        :rtype: dict
        """
        count_colors = {color: 0 for color in self.colors}
        for shape in self.shapes:
            count_colors[shape.get_color()] += 1
        return count_colors
