n = int(input("Enter number of elements: "))
a=[]
b=[]
i=0
while i<n:
    el = float(input("Enter an element for a[{0}]= ".format(i)))
    a.append(el)
    i += 1
print(a)
for el in a:
    if el<0:
        b.append(el)
        m=max(b)
print(b)
print("max = {0}".format(m))




