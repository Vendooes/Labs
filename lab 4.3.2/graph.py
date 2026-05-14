import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Исходные данные
nu = np.array([1.080, 1.936, 3.219])          # частота, MTu
Lambda_vals = np.array([1.41, 0.77, 0.48])    # Λ, мм
Lambda_err = np.array([0.19, 0.09, 0.07])      # погрешность Λ, мм

# Вычисление 1/ν
inv_nu = 1 / nu                               # 1/ν (1/MTu)

# Линейная модель: Λ = a + b * (1/ν)
def linear_model(x, a, b):
    return a + b * x

# Взвешенная аппроксимация (веса = 1/σ²)
popt, pcov = curve_fit(linear_model, inv_nu, Lambda_vals,
                       sigma=Lambda_err, absolute_sigma=True)
a, b = popt
a_err, b_err = np.sqrt(np.diag(pcov))

print("Результаты линейной аппроксимации Λ = a + b·(1/ν):")
print(f"a (свободный член) = {a:.3f} ± {a_err:.3f} мм")
print(f"b (коэффициент наклона) = {b:.3f} ± {b_err:.3f} мм·MTu")

# Построение графика
x_fit = np.linspace(0.3, 0.95, 100)
y_fit = linear_model(x_fit, a, b)

plt.figure(figsize=(8, 5))
plt.errorbar(inv_nu, Lambda_vals, yerr=Lambda_err,
             fmt='o', capsize=5, capthick=1, ecolor='red',
             color='blue', markersize=8, label='Экспериментальные данные')
plt.plot(x_fit, y_fit, 'g--', linewidth=2,
         label=f'Аппроксимация: Λ = {a:.3f} + 1559·(1/ν)')
plt.xlabel('1/ν (1/MTu)')
plt.ylabel('Λ (мм)')
plt.title('Зависимость Λ от 1/ν (с линейной аппроксимацией)')
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()
plt.tight_layout()
plt.show()