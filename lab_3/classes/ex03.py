import ex02

class Rectangle(ex02.Shape):
    def __init__(self, l, w):
        ex02.Shape.__init__(self)
        self.l = l
        self.w = w
    def area(self):
        return self.l*self.w

r = Rectangle(4, 5)
# print(r.area())
