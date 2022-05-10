list=[1,3,36,3,6,4,6]
b=[]
i=0
while i<len(list):
    minimum=min(list)
    if minimum not in b:
        b.append(minimum)
    i+=1
print(b)