class PhieuNhap:
    def __init__(self,maphieu,ngaylap,mancc,tenncc,diachi):
        self.maphieu=maphieu
        self.ngaylap= ngaylap
        self.mancc=mancc
        self.tenncc= tenncc
        self.diachi= diachi
        self.hangs = []

    def addHang(self,hang):
        self.hangs.append(hang)

    def show(self):
        tongtien=0
        print(" Ma phieu :",self.maphieu ,"| Ngay lap :", self.ngaylap,"\n","Ma NCC: ",self.mancc,"  | Ten NCC :",self.tenncc,"\n","Dia chi ",self.diachi)
        for hang in self.hangs:
            hang.display()
            tongtien+=hang.thanhtien
        print("Tong tien ", tongtien)


class Hang:
    def __init__(self, tenhang,dongia,soluong):
        self.tenhang=tenhang
        self.dongia=dongia
        self.soluong=soluong
        self.thanhtien=self.dongia*self.soluong

    def display(self):
        print("Ten hang: ", self.tenhang," Don gia : ",self.dongia," So luong ", self.soluong, " Thanh tien ",self.thanhtien)

a1= Hang("tivi",30,2)
a2 = Hang("Quat",1.20,3)
a3= Hang("Mobi",5,10)

b= PhieuNhap("PH001","1/1/2007","NCC01","LG-Electronic","Khu cong nghiep Nhu Quynh A")
b.addHang(a1)
b.addHang(a2)
b.addHang(a3)
b.show()



