import random
from Rectangle import Rectangle
from Square import Square
from Circle import Circle


class ShapeWarehouse:
    def __init__(self, colors: list, lengths: list):
        self.colors = colors
        self.lengths = lengths
        self.shapes = []

    def create_shape(self):
        shapes = ['Rectangle', 'Square', 'Circle']
        shape = random.choice(shapes)
        if shape == 'Rectangle':
            temp = Rectangle(random.choice(self.colors), random.choice(self.lengths), random.choice(self.lengths))
        elif shape == 'Square':
            temp = Square(random.choice(self.colors), random.choice(self.lengths))
        else:
            temp = Square(random.choice(self.colors), random.choice(self.lengths))
        return temp

    def generate(self, x: int):
        for i in range(x):
            temp = self.create_shape()
            self.shapes.append(temp)

    def sum_areas(self):
        sum_area = float(0)
        for shape in self.shapes:
            sum_area += shape.get_area()
        return sum_area

    def sum_perimeters(self):
        sum_perimeter = float(0)
        for shape in self.shapes:
            sum_perimeter += shape.get_perimeter()
        return sum_perimeter

    def count_colors(self):
        count_colors = {color: 0 for color in self.colors}
        for shape in self.shapes:
            count_colors[shape.get_color()] += 1
        return count_colors
