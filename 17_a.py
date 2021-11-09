class RECTANGLE:
    def __init__(self,height,width,corner_x,corner_y):
        self.height   = height
        self.width    = width
        self.corner_x = corner_x
        self.corner_y = corner_y

    def find_center(self):
        center_x = self.corner_x + (self.width / 2 )
        center_y = self.corner_y + (self.height/ 2 )
        print("the center of the rectange is (",center_x,',',center_y,')')

    def area(self):
        Area = self.height * self.width
        print('The arae is ',Area,"unit square")

    def perimeter(self):
        Peri = 2 * (self.height + self.width)
        print("Perimeter is ",Peri,"units")

instance = RECTANGLE(10,20,0,0)
instance.find_center()
instance.area()
instance.perimeter()