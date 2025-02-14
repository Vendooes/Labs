a = input().split()
k = int(a[0])
s = a[1]
l = []
n = []
for i in s:
    l.append(i)
    if len(l) == k:
        l2 = list(reversed(l))
        n.append(''.join(l2))
        l.clear()
print(''.join(n))