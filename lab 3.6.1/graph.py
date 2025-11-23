import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Данные (6 гармоник)
a_phi = np.array([96, 46, 33, 24, 18, 15])
a_0 = np.array([232, 232, 229, 223, 218, 211])
x = np.array([1.000, 0.500, 0.333, 0.250, 0.200, 0.167])  # 1/ν

# Расчёт K_n
K_n = a_phi / a_0

# Степенная аппроксимация: K = A * x^B
def power_law(x, A, B):
    return A * np.power(x, B)

# Подбор параметров
p0 = [0.4, 1.0]  # Начальные приближения
params, _ = curve_fit(power_law, x, K_n, p0=p0, maxfev=10000)
A_fit, B_fit = params

# Расчёт RMSE
K_pred = power_law(x, A_fit, B_fit)
rmse = np.sqrt(np.mean((K_n - K_pred)**2))

# Визуализация
plt.figure(figsize=(10, 6))
plt.plot(x, K_n, 'o', label='Экспериментальные данные', markersize=8, color='blue')
x_fit = np.linspace(0.16, 1.02, 100)
plt.plot(x_fit, power_law(x_fit, A_fit, B_fit), 
         '-', label=f'Аппроксимация: $K = {A_fit:.3f} \cdot x^{{{B_fit:.3f}}}$\nRMSE = {rmse:.5f}', 
         linewidth=2, color='red')
plt.xlabel('$1/\\nu$', fontsize=12)
plt.ylabel('$K_n$', fontsize=12)
plt.title('Зависимость $K_n$ от $1/\\nu$', fontsize=14)
plt.legend()
plt.grid(linestyle='--', alpha=0.7)
plt.gca().invert_xaxis()  # Инверсия оси X для естественного отображения частот
plt.tight_layout()
plt.show()

# Вывод результатов
print(f"Аппроксимирующая функция: K = {A_fit:.4f} * x^{B_fit:.4f}")
print(f"RMSE: {rmse:.6f}")
print("\nЗначения K_n:")
for i, (xi, ki) in enumerate(zip(x, K_n), 1):
    print(f"1/ν = {xi:.3f}, K_{i} = {ki:.4f}")