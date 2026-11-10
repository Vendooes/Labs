import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Настройка шрифта для формул (как в LaTeX)
plt.rcParams['text.usetex'] = False
plt.rcParams['mathtext.fontset'] = 'cm'

# 1. Данные
x = np.array([10, 11, 12, 13, 14, 15, 15.5, 15.75, 16, 16.25, 16.5, 16.75, 17, 17.25, 17.5, 17.75, 18, 18.75, 19.5, 20.25])
N = np.array([905, 1031, 1000, 998, 919, 874, 827, 844, 713, 697, 550, 451, 256, 195, 108, 62, 38, 43, 34, 24])

sigma_x = np.full_like(x, 0.5, dtype=float)
sigma_N = np.sqrt(N)

# 2. Функции
def logistic_func(x, A, x0, B):
    return A / (1 + np.exp((x - x0) / B))

def derivative_func(x, A, x0, B):
    exp_term = np.exp((x - x0) / B)
    return -(A / B) * exp_term / (1 + exp_term)**2

# 3. Аппроксимация
p0 = [1000, 16.5, 0.4] 
popt, pcov = curve_fit(logistic_func, x, N, p0=p0, sigma=sigma_N, absolute_sigma=True)
A_fit, x0_fit, B_fit = popt

# 4. Пробеги
R_cp = x0_fit            
R_a = x0_fit + 2 * B_fit 

# 5. Подготовка данных
x_smooth = np.linspace(9.5, 21, 200)
N_smooth = logistic_func(x_smooth, *popt)
dNdx_smooth_abs = np.abs(derivative_func(x_smooth, *popt))

# 6. Построение
fig, ax1 = plt.subplots(figsize=(10, 7))

# --- Левая ось Y (N) ---
color_n = 'tab:red'
ax1.set_xlabel(r'Глубина проникновения, $x$, мм', fontsize=13)
ax1.set_ylabel(r'Количество импульсов, $N$', color=color_n, fontsize=13)
ax1.tick_params(axis='y', labelcolor=color_n)

err1 = ax1.errorbar(x, N, yerr=sigma_N, xerr=sigma_x, fmt='o', color='black', 
                    ecolor='gray', capsize=3, label=r'Данные $N(x)$')
line1, = ax1.plot(x_smooth, N_smooth, color=color_n, linewidth=2, label=r'Аппроксимация $f(x)$')

# Касательная
slope = derivative_func(R_cp, *popt)
x_tangent = np.array([R_cp - 1.0, R_a]) 
y_tangent = slope * (x_tangent - R_cp) + (A_fit / 2)
line2, = ax1.plot(x_tangent, y_tangent, 'g--', linewidth=2, label='Касательная')

line3 = ax1.axvline(R_cp, color='purple', linestyle=':', label=rf'$R_{{cp}} = {R_cp:.2f}$ мм')
line4, = ax1.plot(R_a, 0, 'g*', markersize=12, label=rf'$R_a = {R_a:.2f}$ мм')

# --- Правая ось Y (|dN/dx|) ---
ax2 = ax1.twinx()  
color_d = 'tab:blue'
ax2.set_ylabel(r'Плотность остановок, $|\frac{dN}{dx}|$', color=color_d, fontsize=13)
ax2.tick_params(axis='y', labelcolor=color_d)

line5, = ax2.plot(x_smooth, dNdx_smooth_abs, color=color_d, linewidth=2, label=r'Производная $|\frac{dN}{dx}|$')

# --- Масштаб осей ---
ax1.set_xlim(9.5, 21)
ax1.set_ylim(0, np.max(N) * 1.1)             
ax2.set_ylim(0, np.max(dNdx_smooth_abs) * 1.1) 

# 7. Легенда
lines = [err1, line1, line2, line3, line4, line5]
labels = [l.get_label() for l in lines]
ax1.legend(lines, labels, loc='center left', bbox_to_anchor=(0.02, 0.5), 
           framealpha=0.95, fontsize=11)

# Заголовок
plt.title(r'Зависимость $N(x)$ и $|\frac{dN}{dx}|$ от глубины проникновения', fontsize=15, pad=15)

ax1.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()