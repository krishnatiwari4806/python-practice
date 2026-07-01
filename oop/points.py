class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def distance(self, other):
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5

    def distance_from_origin(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5


class Line:

    def __init__(self, A, B, C):
        self.A = A
        self.B = B
        self.C = C

    def __str__(self):
        return f"{self.A}x + {self.B}y + {self.C} = 0"

    def point_on_line(self, point):
        if self.A * point.x + self.B * point.y + self.C == 0:
            return "Point lies on the line"
        else:
            return "Point does not lie on the line"


# Object Creation
p1 = Point(1, 2)
p2 = Point(4, 6)

l1 = Line(1, 1, -3)

print(p1)
print(p2)

print(p1.distance(p2))

print(p1.distance_from_origin())

print(l1)

print(l1.point_on_line(p1))