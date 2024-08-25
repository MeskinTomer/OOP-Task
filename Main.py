from Shape import Shape
from Rectangle import Rectangle


def main():
    rec = Rectangle('Green', 5, 3)
    print(rec.get_color(), rec.get_area(), rec.get_perimeter())


if __name__ == '__main__':
    main()
