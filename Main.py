from Shape import Shape
from Rectangle import Rectangle
from Square import Square
from Circle import Circle
from ShapeWarehouse import ShapeWarehouse


def main():
    my_container = ShapeWarehouse(['Green', 'Blue', 'Red', 'Yellow'], [1, 2, 3, 4, 5])
    my_container.generate(100)
    print("total area:", my_container.sum_areas())
    print("total perimeter:", my_container.sum_perimeters())
    print("colors:", my_container.count_colors())


if __name__ == '__main__':
    main()
