from Shape import Shape
from Rectangle import Rectangle
from Square import Square
from Circle import Circle


def main():
    rec = Rectangle('Green', 5, 3)
    print(rec.get_color(), rec.get_area(), rec.get_perimeter())
    squ = Square('Green', 5)
    print(squ.get_color(), squ.get_area(), squ.get_perimeter())
    cir = Circle('Green', 3)
    print(cir.get_color(), cir.get_area(), cir.get_perimeter())


if __name__ == '__main__':
    main()
