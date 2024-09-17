import math

class Figure:
    sides_count = 0

    def __init__(self, color, *sides, filled=False):
        self.__color = color
        self.filled = filled
        if self.__is_valid_sides(*sides):
            self.__sides = list(sides)
        else:
            self.__sides = [1] * self.sides_count

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        return all(isinstance(value, int) and 0 <= value <= 255 for value in (r, g, b))

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = (r, g, b)

    def __is_valid_sides(self, *sides):
        return (len(sides) == self.sides_count and
                all(isinstance(side, int) and side > 0 for side in sides))

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)

class Circle(Figure):
    sides_count = 1

    def __init__(self, color, circumference, filled=False):
        super().__init__(color, circumference, filled=filled)
        self.__radius = circumference / (2 * math.pi)

    def get_square(self):
        return math.pi * self.__radius ** 2

    def __len__(self):
        return int(2 * math.pi * self.__radius)

class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, height, *sides, filled=False):
        super().__init__(color, *sides, filled=filled)
        self.height = height

    def get_square(self):
        a, b, c = self.get_sides()
        p = (a + b + c) / 2
        return math.sqrt(p * (p - a) * (p - b) * (p - c))

class Cube(Figure):
    sides_count = 12

    def __init__(self, color, side, filled=False):
        super().__init__(color, *[side] * 12, filled=filled)

    def get_volume(self):
        side = self.get_sides()[0]
        return side ** 3

circle1 = Circle((200, 200, 100), 10)
cube1 = Cube((222, 35, 130), 6)

circle1.set_color(55, 66, 77)
print(circle1.get_color())

cube1.set_color(300, 70, 15)
print(cube1.get_color())

cube1.set_sides(5, 3, 12, 4, 5)
print(cube1.get_sides())

circle1.set_sides(15)
print(circle1.get_sides())
print(len(circle1))
print(cube1.get_volume())
