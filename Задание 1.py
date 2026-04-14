n=int(input())
b=[]
s=0
c=0
for i in range(n):
    a=int(input())
    c = a
    while a!=0:
        b.append(a%8)
        a=a//8
    b.reverse()
    if b[-2]==3 and b[-1]==2:
        s=s+c
    b=[]
print(s)
