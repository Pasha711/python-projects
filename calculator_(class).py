class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width  = width

    def Square(self):
        return self.length * self.width

    def Perimeter(self):
        return 2*(self.length + self.width)


rect = Rectangle(3, 5)
print('Square of Rectangle    =',rect.Square())
print('Perimeter of Rectangle =',rect.Perimeter())
