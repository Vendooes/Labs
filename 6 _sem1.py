a = str(input())
b = []
for i in range (0,9):
    if a.count(str(i)) == 1:
        b.append(str(i))
print(''.join(b))