l = []
with open("D:\\Labs\\lab 1.1.4\\lab.txt") as f:
    for line in f.readlines():
        l.append(line.rstrip('\n'))
c = int(input())
r = 0
s=0
z = []
k=0
for q in range(int(4000/c)):
    for i in l[k::]:
        s+=int(i)
        r+=1
        if r==c:
            z.append(s)
            s =0
            r = 0
            k+=c
            break
print(*z, sep="\n")
s = sum(z[0:c])
q= []
for i in z[0:c]:
    d = (i - (s/c))**2
    q.append(d)
dd = ((1/c)*sum(q))**(1/2)
#print(s/c)
#print(dd)
v = []
b = 0
for i in range(200):
    if z.count(i):
        v.append(i)

#print(*v, sep="\n")
fakt=1
j = []

for i in v:
    for t in range(1,i+1):
        fakt *= t 
    c = ((52.28**i)/fakt)*(2.718**(-52.28))
    j.append(c)
    fakt = 1

#print(*j, sep="\n")

f.close()