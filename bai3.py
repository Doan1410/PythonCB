import math as m
a = (int(input("Nhap a ")))
b = (int(input("Nhap b ")))
c = (int(input("Nhap c ")))
print("Phuong trinh co dang ",a,"x^2 + ",b,"x +",c," =0")
delta = b*b-4*a*c
if delta < 0:
    print("PHuong trinh vo nghiem")
if delta == 0:
    print("Phuong trinh co nghiem kep x1=x2=",(-b)/2*a)
if delta >0:
    print("Phuong trinh co 2 nghiem  x1= ",(-b+m.sqrt(delta))/(2*a)," x2 = ", (-b-m.sqrt(delta))/(2*a))
