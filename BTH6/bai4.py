import math
class Poitn:
    def __init__(self,x,y):
        self.x=x
        self.y= y

class Circle:
    def __init__(self,centre, radius):
        self.centre= centre
        self.radius= radius
    


    def Area(self):
        return self.radius**2*math.pi

    def Premeter(self):
        return self.radius*2*math.pi

    def testBelongs(self,a):
        distance= math.sqrt( (self.centre.x-a.x)**2+(self.centre.y-a.y)**2)
        if distance > self.radius:
            print("Khong thuoc duong tron")
        else:
            print("Co thuoc duong tron")

a = Poitn(9,8)
b=Poitn(10,12)
d=Poitn(12,123)
c =Circle(a,7)
print(c.Area())
print(c.Premeter())
print(c.testBelongs(b))
print(c.testBelongs(d))



