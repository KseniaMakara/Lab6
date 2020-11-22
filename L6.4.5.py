n=int(input("Enter n = "))
c=[]
c1=[]
a=float(input("Enter a= "))
b=float(input("Enter b= "))
i = 0
for i in range(n):
    el = float(input('c[{0}]='.format(i)))
    c.append(el)
print("c = {0} ".format(c))
c1=list(c)
for el in c:
    if a<=abs(el)<=b:
        c1.remove(el)
print("c1 = {0}".format(c1))
if len(c1)<len(c):
    c1.extend([0]*(len(c)-len(c1)))
    print("c1 = {0}".format(c1))





