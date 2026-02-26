import numpy as np
import matplotlib.pyplot as plt

# 1. Данные из таблицы
m = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
r = [1.23, 1.515, 1.745, 1.895, 2.11, 2.285, 2.45, 2.62, 2.795, 2.875, 3.03, 3.14]
r_prime = [1.06, 1.385, 1.615, 1.845, 2.095, 2.21, 2.37, 2.525, 2.715, 2.86, 2.98, 3.08]

# 2. Считаем квадраты
r2 = [x**2 for x in r]
rp2 = [x**2 for x in r_prime]

# 3. Аппроксимация (ищем наклон k)
# polyfit возвращает [k, b], нам нужен только первый элемент [0]
k_r2 = np.polyfit(m, r2, 1)[0]
k_rp2 = np.polyfit(m, rp2, 1)[0]

print(f"Наклон для r^2: {k_r2}")
print(f"Наклон для r'^2: {k_rp2}")

# 4. Строим график
plt.plot(m, r2, 'bo', label='r^2 points')       # Синие точки
plt.plot(m, rp2, 'ro', label="r'^2 points")     # Красные точки

# Рисуем линии тренда
# y = k*x + b. Найдем b, чтобы линия проходила через среднюю точку для красоты, 
# но проще просто соединить концы рассчитанной линии.
plt.plot(m, np.poly1d(np.polyfit(m, r2, 1))(m), 'b--', label=f'r^2 trend (k={k_r2:.2f})')
plt.plot(m, np.poly1d(np.polyfit(m, rp2, 1))(m), 'r--', label=f"r'^2 trend (k={k_rp2:.2f})")

plt.legend()
plt.grid(True)
plt.show()