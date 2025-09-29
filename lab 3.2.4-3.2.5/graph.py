import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# Исходные данные
R_values = np.array([408, 735, 1061, 1388, 1715, 2041])
theta_values = np.array([0.21, 0.32, 0.42, 0.50, 0.61, 0.69])

# Преобразование данных
x = 1 / (R_values ** 2)  # 1/R²
y = 1 / (theta_values ** 2)  # 1/θ²

# Вычисление коэффициентов линейной регрессии
slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)

# Создание линии регрессии
x_line = np.linspace(min(x), max(x), 100)
y_line = intercept + slope * x_line

# Построение графика
plt.figure(figsize=(10, 6))

# Точки данных
plt.scatter(x, y, color='blue', s=50, label='Экспериментальные точки', zorder=5)

# Линия регрессии
plt.plot(x_line, y_line, color='red', linewidth=2, 
         label=f'Линия регрессии: y = {intercept:.2f} + {slope:.0f}x')

# Настройка графика
plt.xlabel('1/R²', fontsize=12)
plt.ylabel('1/θ²', fontsize=12)
plt.title('Зависимость 1/θ² от 1/R²', fontsize=14)
plt.grid(True, alpha=0.3)
plt.legend(fontsize=10)

# Дополнительная информация на графике
plt.text(0.05, 0.95, f'Коэффициент корреляции R² = {r_value**2:.4f}', 
         transform=plt.gca().transAxes, fontsize=10,
         bbox=dict(boxstyle="round,pad=0.3", facecolor="white", alpha=0.8))

# Вывод преобразованных значений (для проверки)
print("Преобразованные данные:")
print("1/R²:", x)
print("1/θ²:", y)
print(f"\nПараметры регрессии:")
print(f"Наклон (slope): {slope:.0f}")
print(f"Пересечение (intercept): {intercept:.2f}")
print(f"Коэффициент детерминации R²: {r_value**2:.4f}")

plt.tight_layout()
plt.show()