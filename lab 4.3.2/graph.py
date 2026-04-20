import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# Данные из таблицы
nu = np.array([1.28, 1.2235, 1.5673, 2.0148, 2.1216, 4.4834])  # MHz
Lambda = np.array([1.41, 1.17, 0.91, 0.69, 0.64, 0.37])  # mm

# Вычисляем 1/nu
inv_nu = 1 / nu

# Линейная аппроксимация (метод наименьших квадратов)
slope, intercept, r_value, p_value, std_err = stats.linregress(inv_nu, Lambda)

# Создаем массив для линии аппроксимации
x_fit = np.linspace(min(inv_nu), max(inv_nu), 100)
y_fit = slope * x_fit + intercept

# Вывод результатов
print(f"Уравнение прямой: Λ = {slope:.4f} × (1/ν) + {intercept:.4f}")
print(f"Угол наклона (slope): {slope:.4f} мм·МГц")
print(f"Коэффициент корреляции R²: {r_value**2:.6f}")
print(f"Стандартная ошибка: {std_err:.4f}")

# Построение графика
plt.figure(figsize=(10, 6))
plt.scatter(inv_nu, Lambda, color='red', s=100, label='Экспериментальные данные', zorder=5)
plt.plot(x_fit, y_fit, 'b-', linewidth=2, label=f'Аппроксимация: Λ = {slope:.3f}×(1/ν) + {intercept:.3f}')

# Добавление подписей для точек
for i, (x, y) in enumerate(zip(inv_nu, Lambda)):
    plt.annotate(f'{nu[i]}', (x, y), xytext=(5, 5), textcoords='offset points', fontsize=8)

plt.xlabel('1/ν (МГц⁻¹)', fontsize=12)
plt.ylabel('Λ (мм)', fontsize=12)
plt.title('Зависимость Λ от 1/ν', fontsize=14, fontweight='bold')
plt.legend(fontsize=10)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

# Дополнительная информация
print("\nТаблица значений:")
print(f"{'ν (МГц)':<10} {'1/ν (МГц⁻¹)':<15} {'Λ (мм)':<10}")
print("-" * 35)
for i in range(len(nu)):
    print(f"{nu[i]:<10.4f} {inv_nu[i]:<15.4f} {Lambda[i]:<10.2f}")