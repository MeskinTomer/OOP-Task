class Shape:
    def __init__(self, color: str = 'White', area: float = 1, perimeter: float = 1):
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
