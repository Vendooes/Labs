#Программа находит функцию наилучшей прямой
import numpy as np
count = int(input('Введите кол-во измерений: '))
x = input('Введите x: ').split()
y = input('Введите y: ').split()
sumx = sum(float(i) for i in x)
sumy = sum(float(i) for i in y)
sqrx = 0
prxy = 0
for i in x:
    sqrx +=int(i)**2
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
print(f'Получим функцию: y = {round(a,3)}x + {round(b,3)}')
