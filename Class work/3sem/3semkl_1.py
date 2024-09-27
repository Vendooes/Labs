a = input().split()
d = a[1]
c = int(a[0])
l = []
z = 0
c = 3
#i = int(len(d))/int(c)
for i in range (int(int(len(d))/int(c))):
    f = d[z:c]
    w = f[::-1]
    l.append(w)
    z += 3
    c += 3
print(''.join(l))


