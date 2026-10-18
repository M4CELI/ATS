import math
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def calculate_area(self) -> float: ...

    @abstractmethod
    def calculate_volume(self) -> float: ...


class Cube(Shape):
    def __init__(self, side: float):
        self.side = side

    def calculate_area(self) -> float:
        return 6 * self.side * self.side

    def calculate_volume(self) -> float:
        return self.side ** 3


class Rectangle(Shape):
    def __init__(self, length: float, width: float):
        self.length = length
        self.width = width

    def calculate_area(self) -> float:
        return self.length * self.width

    def calculate_volume(self) -> float:
        return 0


class Cylinder(Shape):
    def __init__(self, radius: float, height: float):
        self.radius = radius
        self.height = height

    def calculate_area(self) -> float:
        return 2 * math.pi * self.radius * (self.radius + self.height)

    def calculate_volume(self) -> float:
        return math.pi * self.radius ** 2 * self.height


class Sphere(Shape):
    def __init__(self, radius: float):
        self.radius = radius

    def calculate_area(self) -> float:
        return 4 * math.pi * self.radius ** 2

    def calculate_volume(self) -> float:
        return (4.0 / 3.0) * math.pi * self.radius ** 3