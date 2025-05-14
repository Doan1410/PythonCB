class TamThucBacHai:
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c

    def __str__(self):
        return f"{self.a}x^2 + {self.b}x + {self.c}"
    
    def __neg__(self):
        return TamThucBacHai(-self.a,-self.b,-self.c)

    def __add__ (self,other):
        return TamThucBacHai(self.a +other.a , self.b + other.b, self.c +other.c)
    
    def __sub__(self,other):
        return TamThucBacHai(self.a -other.a , self.b - other.b, self.c -other.c)

a = TamThucBacHai(2,3,1)
b=TamThucBacHai(6,2,7)
tong = a+b
hieu = a-b
print(tong)
print(hieu)