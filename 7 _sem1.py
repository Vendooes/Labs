a = input()
w = []

for i in range (9,0,-1):
    b = a.count(str(i))
    c = a.count(str(i-1))
    if b<c and b!=0:
        w.append(i-1)

print(w[-1])
