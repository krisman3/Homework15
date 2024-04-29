### Homework 15
# Task 1 and 2

class Shape:
    def area(self):
        pass
    
    def __int__(self):
        return self.area()
    
    def __str__(self):
        return "Shape:\n"


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def __str__(self):
        return f"Rectangle: Width{self.width}, Height:{self.height}"


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius**2
    
    def __str__(self):
        return f"Circle: Radius={self.radius}"


class RightTriangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height
    
    def __str__(self):
        return f"Right Triangle: Base = {self.base}, Height = {self.height}"
    
    
class Trapezoid(Shape): 
    def __init__(self, base1, base2, height):
        self.base1 = base1
        self.base2 = base2
        self.height = height

    def area(self):
        return 0.5 * (self.base1 + self.base2) * self.height

    def __str__(self):
        return f"Trapezoid: Base1 = {self.base1}, Base2 = {self.base2}, Height = {self.height}"
