import math as m
x1 = (int(input("Nhap x1 ")))
x2 = (int(input("Nhap x2 ")))
y1 = (int(input("Nhap y1 ")))
y2 = (int(input("Nhap y2 ")))
D=m.sqrt(((x2-x1)**2)+((y2-y1)**2))
print(D)
M=abs(x2-x1)+abs(y2-y1)
print(M)
C=1-(((x1*x2)+(y1*y2))/((m.sqrt((x1**2)+(y1**2))*m.sqrt((x2**2)+(y2**2)))))
print (C)

