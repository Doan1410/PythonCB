from typing import Protocol

class KhenThuong(Protocol):
    def khen(self)-> None:
        ...
class Sv(KhenThuong):
    def __init__(self,gpa, hoten) :
        self.gpa=gpa
        self.hoten=hoten

    def khen(self) -> None:
        if self.gpa>=3.2:
            print("Khen SV ",self.hoten)

class Gv(KhenThuong):
    def __init__(self,nckh,hoten) :
        self.nckh=nckh
        self.hoten=hoten


    def khen(self) -> None:
        if self.nckh>=2:
            print("Khen GV",self.hoten)

class Ql(KhenThuong):
    def __init__(self,tot,hoten) :
        self.tot=tot
        self.hoten=hoten


    def khen(self) -> None:
        if self.tot == True:
            print("Khen QL",self.hoten)

a= Sv(3.2,"Dat")
b= Sv(2.9, "Thang")
c= Gv(4,"Son")
e=Ql(True,"Quyen")
d=[a,b,c,e]
for i in d:
    i.khen()