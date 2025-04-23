f= open('DATA54.txt','r')
n,m= (int(x) for x in f.readline().split())
b=[]
for line in f.readlines():
    list_str= line.split()
    b.append([float(num) for num in list_str])
print(n," ", m)
a=""
for i in range(n):
    for j in range(m):
        a=a+str(b[i][j])+"  "
    print(a)
    a=""