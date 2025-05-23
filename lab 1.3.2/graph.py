import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
fig = plt.figure(figsize = (16,9)) # создали рисунок/Figure Fig пропорциями 16:9
ax1 = fig.add_subplot(111) # допустим, больше 1 графика нам не надо

x_measured = [0.14, 0.28, 0.56, 0.84, 0.98, 1.12]
y_measured = [0.505, 0.975, 1.99, 3.05, 3.42,4.00]

#используем встроенный линейный интерполятор чтобы посчитать значения прямой МНК в точках, на которых будем строить нашу прямую
#Поскольку мы хотим прямую, нам достаточно двух точек -- начало и конец прямой
# ВАЖНО! np.interp требует, чтобы список "экспериментальные точки" шли по возрастанию x
# ВАЖНО-2! np.interp это не полноценная МНК! 
# Для получения коэффициентов МНК и построения прямой МНК нужно пользоваться np.polyfit(x, y, 1) (см. дальше)
x = [0.14, 1.12]
y = np.interp(x, x_measured, y_measured)

# ставим точки функцией scatter, точки будем ставить крестиком
ax1.scatter(x_measured, y_measured, marker='x')

# поставим кресты погрешностей, linestyle = None, чтобы кресты не соединялись прямыми
ax1.errorbar(x_measured, y_measured, yerr=0.2, xerr = 0.1, color = 'k', linestyle = 'None')

#построим красную прямую МНК
ax1.plot(x,y, 'r')

ax1.grid() # делаем сетку
# Подпишем оси
plt.xlabel('M, H/м')
plt.ylabel('фи ')
plt.title('График заисимости фи(М)', fontdict={'fontname': 'sans-serif', 'fontsize': 20})
plt.show()
# для готового графика для лабы по общефизу не хватает только названия, подписанных осей и легенды, но это вы уже умеете
# успехов!