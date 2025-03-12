import math as m
def snt(n):
    for i in range(2,(int)(m.sqrt(n))+1):
        if(n%i==0):
            return False
    return n>=2

def doixung(a):
    a = str(x)
    c=""
    for i in a:
        c= str(i) + c
    print(a,c)
    if a == c:
        return True
    else: 
        return False
    

x = (int(input("Nhap x ")))
while len(str(x))>7 :
    x = (int(input("Nhap x "))) 
# print(doixung(x))
if snt(x) :
    if doixung(x):
        print(" co doi xung ")
    else:
        print(" khong doi xung ")
    print(" co la so nguyen to ")
else: 
    if doixung(x):
        print(" co doi xung ")
    else:
        print(" khong doi xung ")
    print(" khong la so nguyen to ")


