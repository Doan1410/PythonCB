x = (int(input("Nhap x ")))
n = (int(input("Nhap n ")))
S=0
if n%2==0:
    tmp=2
    S= 2016*x
    while tmp <= n:
        print(tmp)
        S+=((x**tmp)/(3**tmp-1))
        tmp+=1
        
print(S)