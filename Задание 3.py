from random import randint
a=[0]*10
k1=0
k2=1
s1=0
s2=0
for i in range(10):
    a[i]=randint(-10,10)
print(a)
k1=a[k1]
k2=a[k2]
for i in range(10):
    if a[i]>0:
        a[i]-=k1
    if a[i]<0:
        a[i]+=k2
print(a)
