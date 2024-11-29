import matplotlib.pyplot as plt
import numpy as np

count = int(input('Введите кол-во измерений: '))
x = input('Введите x:').split()
y = input('Введите y:').split()
X = []
Y = []
for i in x:
    X.append(float(i))
for q in y:
    Y.append(float(q))


sumx = sum(float(i) for i in X)
sumy = sum(float(i) for i in Y)
sqrx = 0
prxy = 0
for i in x:
    sqrx +=float(i)**2
for i in range(0,count):
    prxy+=float(x[i])*float(y[i])
matrix = np.zeros((2,2))
matrix[0,0] = sqrx
matrix[0,1] = sumx
matrix[1,0] = sumx
matrix[1,1] = count
det0 = np.linalg.det(matrix)
matrix[0,0] = prxy
matrix[1,0] = sumy
deta= np.linalg.det(matrix)
a = deta/det0
matrix[0,0] = sqrx
matrix[1,0] = sumx
matrix[0,1] = prxy
matrix[1,1] = sumy
detb= np.linalg.det(matrix)
b = detb/det0 
a = round(a,3)
b = round(b,3)

Xmnk = X
Ymnk = []
for i in Xmnk:
    c = a*float(i)+ b
    Ymnk.append(c)

fig = plt.figure(figsize=(8,5), dpi=100)
ax1 = fig.add_subplot(111)

plt.plot(Xmnk,Ymnk, 'r', label='MNK')

plt.title('Our First Graph!', fontdict={'fontname': 'sans-serif', 'fontsize': 20})

ax1.scatter(X, Y, marker='x')
# ax1.errorbar(X, Y, yerr=0.2, xerr = 0.1, color = 'k', linestyle = 'None')

plt.xlabel('X Axis')
plt.ylabel('Y Axis')

plt.xticks(X)
plt.yticks(Y)

plt.grid()
plt.xlim(0)
plt.ylim(0)

plt.legend()

plt.savefig('mygraph.png', dpi=300)

plt.show()