a=int(input("enter number:"))
i=0
sum=0
# num=0
while a>0:
    sum=a%10
    a=a//10
    # print(sum,end="")
    num=(sum%10)**2
    sum=sum//10
    print(num,end="")