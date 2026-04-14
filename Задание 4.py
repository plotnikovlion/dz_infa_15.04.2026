from random import randint
a=[0]*10
b=[0]*10
p=0
for i in range(10):
    a[i]=randint(0,10)
    b[i]=randint(0,10)
print(a)
print(b)
for i in range(10):
    p+=(a[i]*b[i])
print(p)
