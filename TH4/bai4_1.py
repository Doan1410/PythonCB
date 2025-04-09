n =int(input("nhap n "))
a= tuple(input(f"nhap {i} ") for i in range(1,n+1))
print(a)
d=[]
b=0
for i in a:
    d.append(int(i))
    b+=int(i)
c=tuple(d)
print(c)
print(b/n)