from random import randint
a=[0]*10
k=0
s=-20001
for i in range(10):
    a[i]=randint(-10000,10000)
print(a)
for i in range(9):
    if a[i]%3==0 or a[i+1]%3==0:
        k+=1
        if a[i]+a[i+1]>=s:
            s=a[i]+a[i+1]
print(k,s)
