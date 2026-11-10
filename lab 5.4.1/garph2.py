import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Настройка шрифта для формул (как в LaTeX)
plt.rcParams['text.usetex'] = False
plt.rcParams['mathtext.fontset'] = 'cm'

# 1. Данные из таблицы
P = np.array([745, 700, 675, 650, 625, 600, 575, 552, 527, 500, 475])
N = np.array([3608, 2931, 2632, 2170, 1677, 1392, 850, 537, 242, 37, 5])

# Новые значения для оси X: P0 - P
P0 = 760
X = P0 - P
X = X[::-1]  # Переворачиваем массивы, чтобы X шел по возрастанию
N = N[::-1]

sigma_X = np.full_like(X, 7.5, dtype=float)
sigma_N = np.sqrt(N)

# 2. Функции
def logistic_func(X, B1, B2, X0, dX):
    return (B1 - B2) / (1 + np.exp((X - X0) / dX)) + B2

def derivative_func(X, B1, B2, X0, dX):
    exp_term = np.exp((X - X0) / dX)
    return -(B1 - B2) / dX * exp_term / (1 + exp_term)**2

# 3. Аппроксимация
p0 = [3800, 0, 135, 40] 
popt, pcov = curve_fit(logistic_func, X, N, p0=p0, sigma=sigma_N, absolute_sigma=True)
B1_fit, B2_fit, X0_fit, dX_fit = popt

# 4. Вычисление
X_cp = X0_fit  
X_a = X0_fit + 2 * dX_fit * (B1_fit + B2_fit) / (B1_fit - B2_fit)

# 5. Подготовка данных
X_smooth = np.linspace(0, 300, 300)
N_smooth = logistic_func(X_smooth, *popt)
dNdX_smooth_abs = np.abs(derivative_func(X_smooth, *popt))

# 6. Построение графика
fig, ax1 = plt.subplots(figsize=(10, 7))

# --- Левая ось Y (N) ---
color_n = 'tab:red'
# ИСПРАВЛЕНО: используем $ везде
ax1.set_xlabel(r'Разность давлений, $P_0 - P$, торр', fontsize=13)
ax1.set_ylabel(r'Количество импульсов, $N$', color=color_n, fontsize=13)
ax1.tick_params(axis='y', labelcolor=color_n)

# Точки с погрешностями
err1 = ax1.errorbar(X, N, yerr=sigma_N, xerr=sigma_X, fmt='o', color='black', 
                    ecolor='gray', capsize=3, label=r'Данные $N(P_0 - P)$')
line1, = ax1.plot(X_smooth, N_smooth, color=color_n, linewidth=2, label=r'Аппроксимация $f(P_0 - P)$')

# Касательная
slope = derivative_func(X_cp, *popt)
X_tangent = np.array([X_cp, X_a]) 
N_tangent = slope * (X_tangent - X_cp) + logistic_func(X_cp, *popt)
line2, = ax1.plot(X_tangent, N_tangent, 'g--', linewidth=2, label='Касательная')

# Вертикальная линия X_cp и точка X_a
line3 = ax1.axvline(X_cp, color='purple', linestyle=':', label=rf'$(P_{{cp}}) = {X_cp:.1f}$ торр')
line4, = ax1.plot(X_a, 0, 'g*', markersize=12, label=rf'$(P_a) = {X_a:.1f}$ торр')

# --- Правая ось Y (|dN/dX|) ---
ax2 = ax1.twinx()  
color_d = 'tab:blue'
ax2.set_ylabel(r'Скорость счета, $|\frac{dN}{dX}|$', color=color_d, fontsize=13)
ax2.tick_params(axis='y', labelcolor=color_d)

line5, = ax2.plot(X_smooth, dNdX_smooth_abs, color=color_d, linewidth=2, label=r'Производная $|\frac{dN}{dX}|$')

# --- Масштаб осей ---
ax1.set_xlim(0, 300)
ax1.set_ylim(0, np.max(N) * 1.1)             
ax2.set_ylim(0, np.max(dNdX_smooth_abs) * 1.1) 

# 7. Легенда
lines = [err1, line1, line2, line3, line4, line5]
labels = [l.get_label() for l in lines]
ax1.legend(lines, labels, loc='center right', bbox_to_anchor=(0.98, 0.5), 
           framealpha=0.95, fontsize=11)

# Заголовок
plt.title(r'Зависимость $N$ от $(P_0 - P)$', fontsize=15, pad=15)

ax1.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()