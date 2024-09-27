q = input().split()
a = int(q[0])
b = int(q[1])

l = []
for d in range (1,a*b*100):
    if a%int(d)==0 and b%int(d)==0:
        l.append(d)
m = max(l)

x = 0
y = 0
def find(x,y):
    z =[]
    for x in range(-a*b*10,a*b*10):
        for y in range(-a*b*10,a*b*10):
            if a*x + b*y == m:
                z.append(abs(x))
                z.append(abs(y))
                s1 = sum(z)
                return s1
            if find(x+1,y+1) < find(x,y):
                return find(x+1,y+1)
                    




print(find(x,y))
