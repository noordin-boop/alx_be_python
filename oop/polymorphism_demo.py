# polymorphism_demo.py
import math

class Shape:
    def area(self):
        """Raise NotImplementedError to enforce overriding in subclasses."""
        raise NotImplementedError("Subclasses must override the area() method")

class Rectangle(Shape):
    def __init__(self, length: float, width: float):
        """Initialize a Rectangle instance."""
        self.length = length
        self.width = width

    def area(self):
        """Calculate the area of the rectangle."""
        return self.length * self.width

class Circle(Shape):
    def __init__(self, radius: float):
        """Initialize a Circle instance."""
        self.radius = radius

    def area(self):
        """Calculate the area of the circle."""
        return math.pi * (self.radius ** 2)
