S = str(input("Nhap S: "))
Q = str(input("Nhap Q: "))
if S.find(Q) != -1:
    print("Q co la day con cua S")
else:
    print("Q khong la day con cua S")
P=str(S+" "+Q)
P=P.replace("Ha","Ba")
a=P.split(' ')
b={k: a.count(k) for k in a}
print(b)

