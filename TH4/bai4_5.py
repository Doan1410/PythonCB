a ={
    "n": 1500,
    "CLUSTERS" :3,
    "ITER" :1000,
    "METHOD":"DCA CLUSTERING",
    "MEASURE": "EUCLIDEAN",
    "YEARS": 9,
    "MAX": 200,
}
print(a)
a["MEASURE"] ="MANHATAN"
print(a["METHOD"])
a.update({"LOSS FUNCTION":"SOFT MAX"})
print(a)
del a["YEARS"]
S = str(input("Nhap S: "))
for k,v in a.items():
    if S==v:
        print(f"S co trung vs thong so {k}")
    else:
        S=int(S)
        if S==v:
            print(f"S co trung vs thong so {k}")
b=list(a.keys())
# c=set(b)
print(b)
# print(c)

