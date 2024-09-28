a = input().split()
n = int(a[0])
b = int(a[1])
c = int(a[2])
l = []
if b == 10:
    while n > c:
        u = n%c
        l.append(str(u))
        n = n//c
    l.append(str(n))
    l.reverse()
    print(''.join(l))
elif c ==10:
    s = 0
    k = len(str(n))
    for i in str(n):
        s+= int(i)*(b**int(k-1))
        k = k-1
    print(s)
else:
    s = 0
    k = len(str(n))
    for i in str(n):
        s+= int(i)*(b**int(k-1))
        k = k-1
    while s > c:
        u = s%c
        l.append(str(u))
        s = s//c
    l.append(str(s))
    l.reverse()
    print(''.join(l))