import math
n = int(input("Enter n: "))
a=[]
b=[]
i=1
b1=1
b2=0
position_in_a = 0
while i<=n:
    el = ((i - 1) ** 2 / 2 * i ** 2 - 1) + math.factorial(i) * math.sin(i)
    a.append(el)
    i+=1
print(a)
for i in range(len(a)):
    if a[i]<0:
        for i1 in range(i+1):
            b1*= float(a[i1])
        b.append(b1)
        b1 = 1
    else:
        for i2 in range(i+1):
            b2+= (i2+1)*abs(a[i2])
        b.append(b2)
        b2=0
print(b)

