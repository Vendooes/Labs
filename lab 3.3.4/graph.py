import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

# Данные из второй таблицы: I (A) -> B (mTl)
I_B_data = np.array([0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6])
B_data = np.array([21.1, 110.7, 189.6, 294.4, 402.1, 503.9, 598.3])

def get_B(I_M):
    if I_M <= 0.6:
        return np.interp(I_M, I_B_data, B_data)
    else:
        slope = (B_data[-1] - B_data[-2]) / (I_B_data[-1] - I_B_data[-2])
        return B_data[-1] + slope * (I_M - I_B_data[-1])

# Данные из таблиц 2–8 (7 таблиц)
tables = [
    {
        "I": 200e-3,
        "U0": -2.09,
        "IM": [0, 0.15, 0.3, 0.45, 0.6, 0.75, 0.9],
        "U": [-2.09, -1.99, -1.12, -0.42, 0.13, 0.67, 1.02]
    },
    {
        "I": 300e-3,
        "U0": -3.15,
        "IM": [0, 0.15, 0.3, 0.45, 0.6, 0.75, 0.9],
        "U": [-4, -2.67, -1.46, -0.56, 0.18, 0.9, 1.35]
    },
    {
        "I": 400e-3,
        "U0": -4.12,
        "IM": [0, 0.15, 0.3, 0.45, 0.6, 0.75, 0.9],
        "U": [-5.01, -3.35, -1.85, -0.69, 0.23, 1.05, 1.77]
    },
    {
        "I": 500e-3,
        "U0": -5.29,
        "IM": [0, 0.15, 0.3, 0.45, 0.6, 0.75, 0.9],
        "U": [-6.02, -3.96, -2.19, -0.82, 0.27, 1.25, 2.07]
    },
    {
        "I": 600e-3,
        "U0": -6.95,
        "IM": [0, 0.15, 0.3, 0.45, 0.6, 0.75, 0.9],
        "U": [-7.09, -4.67, -2.59, -1.02, 0.29, 1.43, 2.51]
    },
    {
        "I": 700e-3,
        "U0": -7.4,
        "IM": [0, 0.15, 0.3, 0.45, 0.6, 0.75, 0.9],
        "U": [-8.02, -5.34, -2.96, -1.04, 0.35, 1.64, 2.77]
    },
    {
        "I": 800e-3,
        "U0": -8.44,
        "IM": [0, 0.15, 0.3, 0.45, 0.6, 0.75, 0.9],
        "U": [-8.44, -5.57, -3.15, -1.09, 0.38, 1.72, 2.91]  # Замените, если есть реальные данные!
    }
]

# Линейная функция для аппроксимации
def linear_func(x, a, b):
    return a * x + b

# Список для хранения k(I)
k_values = []
I_values = []

for table in tables:
    IM = np.array(table["IM"])
    U = np.array(table["U"])
    U0 = table["U0"]
    epsilon_Hall = U - U0
    B = np.array([get_B(im) for im in IM])

    # Аппроксимация линейной функцией
    popt, pcov = curve_fit(linear_func, B, epsilon_Hall)
    a, b = popt  # a — угловой коэффициент k = dε/dB
    k_values.append(a)
    I_values.append(table["I"])  # I в Амперах

# Преобразуем в массивы
I_arr = np.array(I_values)
k_arr = np.array(k_values)

# Аппроксимация k(I): k = a*I + b
popt_k_I, pcov_k_I = curve_fit(linear_func, I_arr, k_arr)
a_k_I, b_k_I = popt_k_I

# R² для k(I)
residuals_k_I = k_arr - linear_func(I_arr, a_k_I, b_k_I)
ss_res_k_I = np.sum(residuals_k_I**2)
ss_tot_k_I = np.sum((k_arr - np.mean(k_arr))**2)
r_squared_k_I = 1 - (ss_res_k_I / ss_tot_k_I)

# Построение графика k(I)
plt.figure(figsize=(10, 6))
plt.plot(I_arr * 1000, k_arr, 'o', label='Экспериментальные точки', markersize=8, color='blue')
plt.plot(I_arr * 1000, linear_func(I_arr, a_k_I, b_k_I), '-', linewidth=2, color='red', label=f'Аппроксимация: k = {a_k_I:.6f}·I + {b_k_I:.6f}')

plt.xlabel('Сила тока I, мА')
plt.ylabel(r'Угловой коэффициент $k = \frac{d\varepsilon_{Холла}}{dB}$, мВ/мТл')
plt.title('Зависимость чувствительности датчика Холла от тока')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# Вывод результатов
print("\n" + "="*60)
print("   АППРОКСИМАЦИЯ ЗАВИСИМОСТИ k(I)")
print("="*60)
print(f"{'Угловой коэффициент a (мВ/мТл·А):':<35} {a_k_I:.6f}")
print(f"{'Сдвиг b (мВ/мТл):':<35} {b_k_I:.6f}")
print(f"{'Коэффициент детерминации R²:':<35} {r_squared_k_I:.6f}")
print("-"*60)
print("Формула аппроксимации: k = {:.6f} * I + {:.6f}".format(a_k_I, b_k_I))