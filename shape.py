class Shape:
    def __init__(self, color):
        self.__color = color

    def calculate_area(self):
        raise NotImplementedError("Subclasses must implement this method.")

    def calculate_perimeter(self):
        raise NotImplementedError("Subclasses must implement this method.")

    def get_color(self):
        return self.__color

    def set_color(self, color):
        self.__color = color

class Rectangle(Shape):
    def __init__(self, color, length, width):
        super().__init__(color)
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

    def calculate_perimeter(self):
        return 2 * (self.length + self.width)

class Triangle(Shape):
    def __init__(self, color, side1, side2, side3):
        super().__init__(color)
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def calculate_area(self):
        s = self.calculate_perimeter() / 2
        return math.sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3))

    def calculate_perimeter(self):
        return self.side1 + self.side2 + self.side3
import math

class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius

    def calculate_area(self):
        return math.pi * (self.radius ** 2)

    def calculate_perimeter(self):
        return 2 * math.pi * self.radius


def main():
    shapes = [
        Rectangle(color="Blue", length=27, width=5),
        Triangle(color="Green", side1=6, side2=4, side3=5),
        Circle(color="Orange", radius=9)
    ]

    for shape in shapes:
        print(f"Shape: {type(shape).__name__}")
        print(f"Color: {shape.get_color()}")
        print(f"Area: {shape.calculate_area():.2f}")
        print(f"Perimeter: {shape.calculate_perimeter():.2f}")
        print("-" * 30)

if __name__ == "__main__":
    main()

