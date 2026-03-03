from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * (self.radius ** 2)

class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def calculate_area(self):
        return self.length * self.breadth

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def calculate_area(self):
        return 0.5 * self.base * self.height


def main():
    shape_type = input("Enter the shape type (Circle, Rectangle, Triangle): ")

    if shape_type.lower() == "circle":
        radius = float(input("Enter the radius: "))
        obj = Circle(radius)
        area = obj.calculate_area()
        print("The area of the Circle is:", format(area, '.2f'))

    elif shape_type.lower() == "rectangle":
        length = float(input("Enter the length: "))
        breadth = float(input("Enter the breadth: "))
        obj = Rectangle(length, breadth)
        area = obj.calculate_area()
        print("The area of the Rectangle is:", format(area, '.2f'))

    elif shape_type.lower() == "triangle":
        base = float(input("Enter the base: "))
        height = float(input("Enter the height: "))
        obj = Triangle(base, height)
        area = obj.calculate_area()
        print("The area of the Triangle is:", format(area, '.2f'))

if __name__ == "__main__":
    main()
