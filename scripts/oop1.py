from abc import ABC, abstractmethod
import math
from math import radians


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, side_a, side_b):
        self._side_a = side_a
        self._side_b = side_b


    def area(self):
        return self._side_a * self._side_b


class Circle(Shape):
    def __init__(self, radius):
        self._radius = radius


    def area(self):
        return self._radius ** 2 * math.pi


instance1 = Rectangle(13, 12)
instance2 = Circle(13)

print(instance1.area())
print(instance2.area())