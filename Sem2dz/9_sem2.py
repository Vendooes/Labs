with open("D:\\Python code\\Sem2dz\\input.txt") as f:
    c = f.readline().strip().split()
k = 0
for char in ' '.join(c):
    if char.isupper():
        k +=1
print('Кол-во предложений',k)
f.close()