f= open('bai1.txt','r')
n,m= (int(x) for x in f.readline().split())
b=[]
for line in f.readlines():
    list_str= line.split()
    b.append([int(num) for num in list_str])
print(n," ", m)
a=""
print  (b)
for i in range(n):
    for j in range(m):
        a=a+str(b[i][j])+" "
    print(a)
    a=""
d=[]
for i in range(n):
    print(i)
    d=[row[i] for row in b]
    print(d)