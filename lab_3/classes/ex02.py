class Shape:
    def __init__(self):
        self.Area = 0
    def area(self):
        return self.Area

class Square(Shape):
    def __init__(self, length):
        Shape.__init__(self)
        self.length = length
    def area(self):
        return self.length**2

x1 = Shape()
x2 = Square(4)
# print(x1.area())
# print(x2.area())