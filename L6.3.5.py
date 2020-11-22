import math
n=2
a = []
b = []
i = 0
while i<n:
    el=float(input("Enter an element for a[{0}]= ".format(i)))
    a.append(el)
    e=float(input("Enter an element for b[{0}]= ".format(i)))
    b.append(e)
    i+=1
print(a)
print(b)
product = a[0]*b[0]+a[1]*b[1]
print(product)
module1 = math.sqrt((a[0])**2+(a[1])**2)
module2 = math.sqrt((b[0])**2+(b[1])**2)
print(module1)
print(module2)
cos = product/(module1*module2)
print("Cos = {0}".format(cos))

