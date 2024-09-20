a = [ i for i in input()]
for i in range (0, len(a)-1, 1):
    a[i], a[len(a)-1] = a[len(a)-1], a[i]
print(''.join(a))