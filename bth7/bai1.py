class Person:
    def __init__(self,hoten,ngaysinh,quequan) :
        self.hoten= hoten
        self.ngaysinh=ngaysinh
        self.quequan=quequan
        
    
class Kysu(Person):
    def __init__(self, hoten, ngaysinh, quequan,nganhhoc,namtotnghiep):
        super().__init__(hoten, ngaysinh, quequan)
        self.nganhhoc=nganhhoc
        self.namtotnghiep=namtotnghiep

    def khoitao(self):
        a = Kysu("Ngo Thanh Doan","14/10/2004","Quang Ninh","KTPM","2023")
        return a
        
    def display(self):
        print("Ho ten:", self.hoten, " Ngay sinh: ",self.ngaysinh, " Que quan: ",self.quequan, " Nganh hoc: ", self.nganhhoc, " Nam tot nghiep: ",self.namtotnghiep)

a = Kysu("","","","","")

a1 = Kysu("Ngo Thanh Doan 2","14/10/2004","Quang Ninh","KTPM","2023")

# a = a.khoitao()
a.display()
a11 =[a,a1]
for a in a11:
    a.display()