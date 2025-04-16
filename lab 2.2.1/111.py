import csv
import matplotlib.pyplot as plt
import numpy as np
import math

with open('113_6.csv', mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    selected_columns = [
        row['V (mV)']
        for row in reader
    ]

with open('113_6.csv', mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    selected_columns1 = [
        row['t (s)']
        for row in reader
    ]

selected_columns = list(map(float,selected_columns))
experimental = []
for i in selected_columns:
    experimental.append(math.log(i/selected_columns[0]))


selected_columns1 = list(map(float,selected_columns1))
time = []
for i in selected_columns1:
    time.append(round(i,1))


count = len(experimental)
x = time
y = experimental
# y2 = input('Введите y2:').split()
# y3 = input('Введите y3:').split()
# y4 = input('Введите y4:').split()
# y5 = input('Введите y5:').split()
X = []
Y = []
Y2 = []
Y3 = []
Y4 = []
Y5 = []
for i in x:
    X.append(float(i))
for q in y:
    Y.append(float(q))
# for q in y2:
#     Y2.append(float(q))
# for q in y3:
#     Y3.append(float(q))
# for q in y4:
#     Y4.append(float(q))
# for q in y5:
#     Y5.append(float(q))

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
a = round(a,4)
b = round(b,3)

Xmnk = X
Ymnk = []
for i in Xmnk:
    c = a*float(i)+ b
    Ymnk.append(c)

Y2mnk = []
for i in Xmnk:
    c = 1.55*float(i) -0
    Y2mnk.append(c)


Y3mnk = []
for i in Xmnk:
    c = 0.774*float(i)- 0.148
    Y3mnk.append(c)

Y4mnk = []
for i in Xmnk:
    c = 0.686*float(i)+0.243
    Y4mnk.append(c)

Y5mnk = []
for i in Xmnk:
    c = 0.576*float(i)+ 0.618
    Y5mnk.append(c)

fig = plt.figure(figsize=(8,5), dpi=100)
ax1 = fig.add_subplot(111)

plt.plot(Xmnk,Ymnk,'-' 'r', label='113.6')
# plt.plot(Xmnk,Y2mnk,'--' 'r', label='max')
# plt.plot(Xmnk,Y3mnk,'-' 'r', label='63')
# plt.plot(Xmnk,Y4mnk,'-' 'r', label='78')
# plt.plot(Xmnk,Y5mnk,',' 'r', label = '57')
plt.title('ln(U/U0)(t)', fontdict={'fontname': 'sans-serif', 'fontsize': 20})

ax1.scatter(X, Y, marker='.')
# ax1.scatter(X, Y2, marker='x')
# ax1.scatter(X, Y3, marker='x')
# ax1.scatter(X, Y4, marker='x')
# ax1.scatter(X, Y5, marker='x')

# plt.plot(X,Y, 'b', label='Def1')

# plt.plot(X,Y2, 'b', label='Def2')
# plt.plot(X,Y3, 'b', label='Def3')
# plt.plot(X,Y4, 'b', label='Def4')
# plt.plot(X,Y5, 'b', label='Def5')
# ax1.errorbar(X, Y, yerr=0.2, xerr = 0.1, color = 'k', linestyle = 'None')

plt.xlabel('t')
plt.ylabel('ln(U/U0)')



plt.xticks(np.arange(0, max(X), 20))
plt.yticks(np.arange(min(Y),max(Y) ,0.05))
# plt.ylabel('u(д-т)')

plt.grid()
# plt.xlim(0)
# plt.ylim(0)

plt.legend()

plt.savefig('mygraph.png', dpi=300)

plt.show()
print(a)