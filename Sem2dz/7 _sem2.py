a = input().split()
w = []
b = a.count(a[0])
w.append(a[0])
for q in a:
    if b<a.count(q):
        w.clear()
        w.append(q)
        b = a.count(q)
print(''.join(w))
