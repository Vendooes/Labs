import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# Данные из таблицы
inv_U = np.array([6.25e-4, 6.02e-4, 5.78e-4, 5.65e-4, 5.52e-4, 
                  5.32e-4, 5.21e-4, 5.15e-4, 5.05e-4, 4.72e-4, 4.48e-4])
ln_I_U2 = np.array([-28.17, -27.55, -26.94, -26.47, -26.11, 
                    -25.68, -25.54, -25.27, -25.09, -24.64, -24.07])

# Линейная аппроксимация
slope, intercept, r_value, p_value, std_err = stats.linregress(inv_U, ln_I_U2)

# Создание линии аппроксимации
x_fit = np.linspace(min(inv_U), max(inv_U), 100)
y_fit = slope * x_fit + intercept

# Построение графика
plt.figure(figsize=(10, 6))
plt.scatter(inv_U, ln_I_U2, color='red', label='Экспериментальные данные', zorder=5)
plt.plot(x_fit, y_fit, 'b-', label=f'Аппроксимация: y = {slope:.2f}x + {intercept:.2f}', linewidth=2)
plt.xlabel('1/U, В⁻¹', fontsize=12)
plt.ylabel('ln(I/U²)', fontsize=12)
plt.title('Зависимость ln(I/U²) от 1/U', fontsize=14, fontweight='bold')
plt.legend(fontsize=10)
plt.grid(True, alpha=0.3)

# Добавление информации о коэффициенте наклона на график
textstr = f'Коэффициент наклона: {slope:.2f}\nR² = {r_value**2:.4f}'
plt.text(0.05, 0.95, textstr, transform=plt.gca().transAxes, 
         fontsize=10, verticalalignment='top',
         bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

plt.tight_layout()
plt.show()

# Вывод результатов
print("="*50)
print("РЕЗУЛЬТАТЫ АППРОКСИМАЦИИ:")
print("="*50)
print(f"Коэффициент наклона (slope): {slope:.2f}")
print(f"Свободный член (intercept): {intercept:.2f}")
print(f"Коэффициент корреляции R: {r_value:.4f}")
print(f"Коэффициент детерминации R²: {r_value**2:.4f}")
print(f"Стандартная ошибка: {std_err:.2f}")
print("="*50)