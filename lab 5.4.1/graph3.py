import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Настройка шрифта для формул (как в LaTeX)
plt.rcParams['text.usetex'] = False
plt.rcParams['mathtext.fontset'] = 'cm'

# 1. Данные из таблицы
P = np.array([745, 700, 675, 650, 625, 600, 575, 552, 527, 500, 475, 450, 425, 400, 380, 365, 350, 325, 300, 275, 250, 225, 200, 175, 150, 125, 100, 75, 50, 0])
I = np.array([7, 68, 100, 138, 166, 199, 240, 272, 308, 354, 393, 432, 470, 515, 548, 572, 601, 653, 686, 731, 758, 787, 792, 790, 789, 781, 770, 768, 760, 755])

# Пересчет оси X: P0 - P
P0 = 760
X = P0 - P

sigma_X = np.full_like(X, 7.5, dtype=float)
sigma_I = np.full_like(I, 7, dtype=float)

# 2. Функции
def logistic_func(X, B1, B2, X0, dX):
    return (B1 - B2) / (1 + np.exp((X - X0) / dX)) + B2

# 3. Аппроксимация
p0 = [0, 790, 450, 50] 
popt, pcov = curve_fit(logistic_func, X, I, p0=p0, sigma=sigma_I, absolute_sigma=True)
B1, B2, X0, dX = popt

# 4. Геометрический поиск P_a
# Уравнение касательной в точке перегиба X0: 
# I = k * (X - X0) + (B1 + B2) / 2, где k - производная в точке X0
k = (B2 - B1) / (4 * dX) 

# Пересечение касательной с верхней горизонтальной полкой (I = B2)
# B2 = k * (X_a - X0) + (B1 + B2) / 2
# Отсюда: X_a = X0 + (B2 - B1) / (2k) = X0 + 2 * dX
X_a = X0 + 2 * dX
P_a = P0 - X_a  # Возвращаемся к истинному давлению

# Вывод результатов в консоль
print(f"Параметры аппроксимации: B1={B1:.2f}, B2={B2:.2f}, X0={X0:.2f}, dX={dX:.2f}")
print(f"Точка пересечения на оси X: (P_a) = {X_a:.2f} торр")
print(f"Экстраполированное давление: P_a = {P_a:.2f} торр")

# 5. Подготовка линий для графика
X_smooth = np.linspace(-10, 800, 300)
I_smooth = logistic_func(X_smooth, *popt)

# Линия касательной (продолженная до пересечения с полкой)
X_tan_plot = np.linspace(X0 - 100, X_a + 50, 100)
I_tan_plot = k * (X_tan_plot - X0) + (B1 + B2) / 2

# 6. Построение графика
fig, ax = plt.subplots(figsize=(10, 7))

# Данные с погрешностями
ax.errorbar(X, I, yerr=sigma_I, xerr=sigma_X, fmt='o', color='black', 
            ecolor='gray', capsize=3, label=r'Данные $I(P_0 - P)$')

# Кривая аппроксимации
ax.plot(X_smooth, I_smooth, color='tab:red', linewidth=2, label=r'Аппроксимация $f(P_0 - P)$')

# Верхняя горизонтальная полка
ax.axhline(B2, color='gray', linestyle='--', linewidth=1.5, label='Верхний горизонтальный участок')

# Наклонный участок (касательная)
ax.plot(X_tan_plot, I_tan_plot, 'g--', linewidth=2, label='Наклонный участок (касательная)')

# Точка пересечения и перпендикуляр к оси X
ax.plot(X_a, B2, 'ko', markersize=8)
# Рисуем фиолетовую пунктирную линию вниз до оси X
ax.axvline(X_a, color='purple', linestyle=':', linewidth=2, 
           label=rf'$(P_a) = {X_a:.1f}$ торр')

# Добавляем стрелочку от точки пересечения к оси
ax.annotate('', xy=(X_a, 0), xytext=(X_a, B2), 
            arrowprops=dict(arrowstyle='<->', color='purple', lw=1.5))

# Настройки осей
ax.set_xlabel(r'Разность давлений, $P_0 - P$, торр', fontsize=13)
ax.set_ylabel(r'Ионизационный ток, $I$, пА', fontsize=13)
ax.set_xlim(-10, 800)
ax.set_ylim(0, np.max(I) * 1.1)
ax.grid(True, linestyle='--', alpha=0.5)

# Легенда
ax.legend(loc='center right', fontsize=11, framealpha=0.95)

# Заголовок
plt.title(r'Зависимость I(P0 - P)', fontsize=15, pad=15)

plt.tight_layout()
plt.show()