with open("D:\\Python code\\Sem1dz\\input.txt") as f:
    c = f.readline().strip().split()
    o = f.readlines()[-1]
q = 0
if o == '+':
    for i in c:
        q+=int(i)
    with open("D:\\Python code\\Sem1dz\\output.txt", 'w') as f2:
        f2.write(str(q))
    f2.close()
elif o == '-':
    q=int(c[0])-int(c[1]) 
    for i in c[2::]:
        q = q- int(i) 
    with open("D:\\Python code\\Sem1dz\\output.txt", 'w') as f2:
        f2.write(str(q))
    f2.close()
elif o == '*':
    z = 1
    for i in c:
        z*=int(i)
    with open("D:\\Python code\\Sem1dz\\output.txt", 'w') as f2:
        f2.write(str(z))
    f2.close()
f.close()