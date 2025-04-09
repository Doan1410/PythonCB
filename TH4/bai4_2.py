
n =int(input("nhap n "))
a= set(input(f"nhap {i} ") for i in range(1,n+1))
b= set(input(f"nhap {j} ") for j in range(1,n+1))

if a | b ==set():
    print("Ko co ai")
else: 
    print("sinh vien dki o 2 ban ",a | b)
if a & b ==set():
    print("Ko co ai")
else: 
    print("sinh vien chi dki ca 2",a & b)
if a - b ==set():
    print("Ko co ai")
else: 
    print("sinh vien chi dki ban 1 ko dki ban 2",a - b)
