from Shape import Shape
from Rectangle import Rectangle
from Square import Square
from Circle import Circle
from ShapeWarehouse import ShapeWarehouse

def main():
    rec = Rectangle('Green', 5, 3)
    print(rec)
    squ = Square('Green', 5)
    print(squ)
    cir = Circle('Green', 3)
    print(cir)

    shapes = ShapeWarehouse(['Green', 'Blue', 'Red', 'Yellow'], [1, 2, 3, 4, 5])
    shapes.generate(3)


if __name__ == '__main__':
    main()
