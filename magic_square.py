a=[[8, 3, 4],[1, 5, 9],[6, 7, 2]]
i=0
n1=0
n2=0
n3=0
c1=0
c2=0
c3=0
d1=0
d2=0
while i<len(a):
    n1=n1+a[0][i]
    n2=n2+a[i][i]
    n3=n3+a[2][i]
    c1=c1+a[i][0]
    c2=c2+a[i][1]
    c3=c3+a[i][2]
    d1=d1+a[i][i]
    d2=d2+a[i][i-i]
    i=i+1
if n1 ==n2 and n2 ==n3 and n1==c1 and c1 ==c2 and c2==c3 and c1 ==d1 and d1==d2 :
    print("a is magic square")
else:
    ("a is not a magic square")