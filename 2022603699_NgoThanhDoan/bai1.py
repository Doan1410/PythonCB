file1 = open('bai1.txt','w',encoding='utf-8')
n= int(input("Nhap n : "))
m= int(input("Nhap m : "))
file1.write(f'{n} {m}\n')
for i in range(n):
    for j in range(m):
        file1.write(' ')
        file1.write(input(f'Nhap b {i+1} {j+1} :'))
        file1.write(' ')
    file1.write('\n')
file1.close()