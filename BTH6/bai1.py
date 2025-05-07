import math
class Square:
    def __init__(self,dai,rong):
        self.dai=dai
        self.rong=rong
    
    def Premeter(self):
        return (self.dai+self.rong)*2
    def Area(self):
        return self.dai*self.rong
    def display(self):
        print("Chieu dai ", self.dai)
        print("Chieu rong ", self.rong)
        print("Chu vi ", self.Premeter())
        print("Dien tich ", self.Area())

a = Square(3,2)
print(a.Area())
print(a.Premeter())    
a.display()

