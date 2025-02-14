a = input().split()
c = int(a[0])
b = a[1::]
for i in range(1,c+1):
    if str(''.join(b)).find(str(i)) == -1:
        print(i)

