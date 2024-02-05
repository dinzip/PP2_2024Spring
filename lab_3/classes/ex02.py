class Shape:
    def __init__(self):
        self.a = 0
    def area(self):
        print(self.a)

class Square(Shape):
    def __init__(self, length):
        Shape.__init__(self)
        self.length = length
        self.a = self.length**2

x1 = Shape()
x2 = Square(4)
# x1.area()
# x2.area()