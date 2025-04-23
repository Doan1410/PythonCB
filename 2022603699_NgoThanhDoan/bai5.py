def get_column(matrix, col_index):
    return [row[col_index] for row in matrix]
f = open('Image.data','r')
f2 = open('image2.txt','w')
n,m= (int(x) for x in f.readline().split())
b=[]
for line in f.readlines():
    list_str=line.split()
    b.append([float(x) for x in list_str])
c=""
d=[]
print(n," ", m)
a=""
for i in range(n):
    for j in range(m):
        a=a+str(round((b[i][j]),3))+"  "
    print(a)
    a=""
for i in range(m):
    e= get_column(b,int(i))  
    d.append(sum(e)/n)

for i in range(n):
    for j in range(m):
        if b[i][j]==0:
            b[i][j]= d[j]
        f2.write(str(round((b[i][j]),3)))
        f2.write('  ')
    f2.write('\n')
f3=open('t1.txt','w')
f3.write(f' 100 {m}\n')

for i in range(100):
    for j in range(m):
        if b[i][j]==0:
            b[i][j]= d[j]
        f3.write(str(round((b[i][j]),3)))
        f3.write('  ')
    f3.write('\n')
f4=open('t2.txt','w')
f4.write(f'{n-100} {m}\n')
for i in range(100,n-100):
    for j in range(m):
        if b[i][j]==0:
            b[i][j]= d[j]
        f4.write(str(round((b[i][j]),3)))
        f4.write('  ')
    f4.write('\n')

