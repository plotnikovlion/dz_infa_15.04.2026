from random import randint
a=[0]*10
for i in range(10):
    a[i]=randint(1,100)
    while a[i]%10==0:
        a[i]=randint(1,100)
print(a)
for i in range(10):
    if (a[i]%10)%2==0 and (a[i]%(a[i]%10))==0:
        a[i]=0
print(a)
