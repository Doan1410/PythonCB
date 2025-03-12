a = (int(input("Nhap a ")))
b = ""
d = ("don vi","chuc","tram","ngan")
n=0
while a>=1:
    c = a%10
    a = a//10
    b = str(c)+ " " + d[n]+ " " +b 
    n+=1
print(b)
