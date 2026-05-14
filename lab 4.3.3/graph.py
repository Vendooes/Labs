import numpy as np
import matplotlib.pyplot as plt

# Исходные данные
D = np.array([4.0, 2.20, 1.24])  # мм
d = np.array([13, 25, 50])        # мкм

# Вычисляем 1/D
inv_D = 1 / D  # мм^(-1)

# Линейная аппроксимация d от 1/D
# Используем polyfit для нахождения коэффициентов прямой y = kx + b
coefficients = np.polyfit(inv_D, d, 1)
k = coefficients[0]  # угловой коэффициент
b = coefficients[1]  # свободный член

# Создаем массив для линии аппроксимации
inv_D_fit = np.linspace(min(inv_D) * 0.9, max(inv_D) * 1.1, 100)
d_fit = k * inv_D_fit + b

# Вычисляем коэффициент детерминации R²
d_pred = k * inv_D + b
ss_res = np.sum((d - d_pred) ** 2)
ss_tot = np.sum((d - np.mean(d)) ** 2)
r_squared = 1 - (ss_res / ss_tot)

# Создаем график
plt.figure(figsize=(10, 6))
plt.scatter(inv_D, d, color='red', s=100, label='Экспериментальные данные', zorder=5)
plt.plot(inv_D_fit, d_fit, 'b-', linewidth=2, label=f'Аппроксимация: d = {k:.2f}·(1/D) + {b:.2f}')

# Добавляем подписи и заголовок
plt.xlabel('1/D, мм$^{-1}$', fontsize=12)
plt.ylabel('d, мкм', fontsize=12)
plt.title('Зависимость d от 1/D', fontsize=14, fontweight='bold')
plt.legend(fontsize=10)
plt.grid(True, alpha=0.3)

# Добавляем информацию о качестве аппроксимации
plt.text(0.05, 0.95, f'R² = {r_squared:.4f}', transform=plt.gca().transAxes, 
         fontsize=10, verticalalignment='top', bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

# Подписываем точки
for i, (x, y) in enumerate(zip(inv_D, d)):
    plt.annotate(f'{i+1}', (x, y), xytext=(5, 5), textcoords='offset points')

plt.tight_layout()
plt.show()

# Выводим результаты
print("Результаты аппроксимации:")
print(f"Уравнение: d = {k:.2f}·(1/D) + {b:.2f}")
print(f"Коэффициент детерминации R² = {r_squared:.4f}")
print(f"\nИсходные данные:")
print(f"1/D: {inv_D}")
print(f"d:   {d}")