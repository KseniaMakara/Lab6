import math
n = int(input("Enter n: "))
a=[]
b=[]
c=[]
i=1
e=1
s=0
while i<=n:
    el = ((i - 1) ** 2 / 2 * i ** 2 - 1) + math.factorial(i) * math.sin(i)
    a.append(el)
    i+=1
print(a)
for el in a:
    b=[el for el in a if el<0]
print(b)
for el in b:
    e*=el
print("e ={0}".format(e))
for el in a:
    c=[el for el in a if el>=0]
print(c)
for el in c:
    while i<n:
        k=i
        el=abs(c[k])*i
        s = s + el
        i+=1
    print("s = {0}".format(s))

