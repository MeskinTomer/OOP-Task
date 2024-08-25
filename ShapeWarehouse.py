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
