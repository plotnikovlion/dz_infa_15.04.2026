from random import randint
a=[0]*10
b=[]
c=[]
d=[]
for i in range(10):
    a[i]=randint(-100,100)
    if a[i]>0:
        b.append(a[i])
    elif a[i]==0:
        c.append(0)
    else:
        d.append(a[i])
print(b+d+c)
