class Shape:
    def __init__(self, color: str, area: float, perimeter: float):
        self.color = color
        self.area = area
        self.perimeter = perimeter

    def set_color(self, color: str) -> None:
        self.color = color

    def get_color(self) -> str:
        return self.color

    def get_area(self) -> float:
        return self.area

    def get_perimeter(self) -> float:
        return self.perimeter
