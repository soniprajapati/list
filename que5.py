input_list = [1, 2, 2, 5, 8, 4, 4, 8]
i=0
b=[]
count=0
while i<len(input_list):
    if i not in b:
        b.append(input_list[i])
        count=count+1
        print(b)
    i+=1
print(count)


a="soni manu aarti"
b=a.split(",")
print(b)