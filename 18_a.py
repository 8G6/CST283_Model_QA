from math import pi

class Circle:
    def __init__(self,rad):
        self.rad = rad
    
    def area(self):
        print("Area is %.4f " % (self.rad**2*pi))
    
    def perimeter(self):
        print("Perimeter is %.4f" % (self.rad*pi*2))

circle = Circle(1)

circle.area()
circle.perimeter()
