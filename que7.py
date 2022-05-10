mixed_list = [34.67, 12, -94.89, "Python", 0, "C#"]
list=[]
for x in mixed_list:
    if type(x)==int:
        list.append(x)
print(list)
    