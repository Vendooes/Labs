import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# 1. Ввод данных из таблицы
U = np.array([30.00, 25.00, 20.00, 17.00, 15.00, 12.50, 10.00, 5.00, 2.00, 1.00, 0.50])
delta_eff = np.array([0.27, 0.27, 0.28, 0.28, 0.28, 0.27, 0.25, 0.25, 0.17, 0.16, 0.00])

# 2. Функция для аппроксимации (со второго скриншота)
def delta_fit_func(U_0, delta_m, U_m, s):
    return delta_m * (U_0 / U_m)**s * np.exp(s * (1 - U_0 / U_m))

# Начальные приближения параметров (p0) и границы (bounds), 
# чтобы фит не улетел в отрицательные значения
p0 = [0.28, 15.0, 1.0]
bounds = ([0.0, 0.1, 0.01], [1.0, 100.0, 10.0])

# 3. Выполнение аппроксимации
try:
    popt, pcov = curve_fit(delta_fit_func, U, delta_eff, p0=p0, bounds=bounds, maxfev=10000)
    delta_m_opt, U_m_opt, s_opt = popt
except RuntimeError:
    print("Не удалось подобрать параметры. Попробуйте изменить начальные значения p0.")
    exit()

# Значения функции в экспериментальных точках для расчета погрешности
delta_fit_vals = delta_fit_func(U, *popt)

# 4. Расчет погрешностей для каждой точки
# Погрешность аппроксимации (используем СКО остатков как общую ошибку модели)
residuals = delta_eff - delta_fit_vals
delta_res = np.std(residuals) 

# Приборная погрешность (по условию от 0.9e-5 до 3.5e-5 начиная с U=1 кВ)
sigma_pr = np.zeros_like(U)
for i, u_val in enumerate(U):
    if u_val >= 1.0:
        sigma_pr[i] = 3.5e-5  # Берем верхнюю границу диапазона
    else:
        sigma_pr[i] = 0.0     # Для U < 1 не задано, оставим 0

# Итоговая погрешность по формуле с третьего скриншота
delta_i_total = np.sqrt(delta_res**2 + sigma_pr**2)

# 5. Построение графика
plt.figure(figsize=(10, 6), dpi=120)

# Экспериментальные точки с крестами погрешностей (только вертикальные)
plt.errorbar(U, delta_eff, yerr=delta_i_total, fmt='o', color='blue', 
             ecolor='black', capsize=5, markersize=6, 
             label='Экспериментальные данные с погрешностью')

# Гладкая линия аппроксимации
U_smooth = np.linspace(min(U), max(U), 300)
delta_smooth = delta_fit_func(U_smooth, *popt)
plt.plot(U_smooth, delta_smooth, 'r-', linewidth=2,
         label=f'Аппроксимация:\ndelta_m = {delta_m_opt:.3f}, U_m = {U_m_opt:.2f} кВ, s = {s_opt:.3f}')

# Оформление графика
plt.title('Зависимость эффективного коэффициента электронной эмиссии от ускоряющего напряжения', fontsize=13)
plt.xlabel('Ускоряющее напряжение U, кВ', fontsize=12)
plt.ylabel('Эффективный коэффициент delta_eff', fontsize=12)
plt.grid(True, which='both', linestyle='--', alpha=0.6)
plt.legend(fontsize=11, loc='best')

# Немного расширим границы по Y, чтобы кресты не обрезались
plt.ylim(-0.03, 0.35)
plt.xlim(0, 32)

plt.tight_layout()
plt.show()

# Вывод параметров в консоль
print(f"Параметры аппроксимации:")
print(f"delta_m = {delta_m_opt:.4f}")
print(f"U_m = {U_m_opt:.4f} кВ")
print(f"s = {s_opt:.4f}")
print(f"Погрешность аппроксимации (СКО): {delta_res:.4f}")