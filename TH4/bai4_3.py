a= {
    'Doan' : 4,
    'Doan1' : 5,
    'Doan2' : 1,
    'Doan3' : 2
}
b=0
for k,v in a.items():
    if v <=3.5 or v >= 2.5:
        b+=1
a.update({"doan2":5})
for k,v in a.copy().items():
    if v<2:
        del a[k]
print(a)
