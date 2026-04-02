# import matplotlib.pyplot as plt
# import numpy as np

# # ============================================================
# # ДАННЫЕ ИЗ ТАБЛИЦЫ
# # ============================================================
# # Первая строка (U1, мВ) * 1000
# voltage = [0, 2000, 5000, 10000, 15000, 20000, 30000, 40000, 
#            50000, 100000, 150000, 200000, 400000]

# # Нижняя строка (I, мкА)
# current = [-6.29, -4.88, -2.31, 1.34, 4.93, 8.19, 13.8, 18.6, 
#            23.09, 42.7, 59.7, 70.8, 95.4]
# # ============================================================

# # Настройка стиля графика
# plt.figure(figsize=(12, 7))
# plt.plot(voltage, current, 'o-', color='blue', linewidth=2, 
#          markersize=8, label='I(U)', markerfacecolor='white', 
#          markeredgecolor='blue', markeredgewidth=2)

# # Оформление осей и заголовка
# plt.title('Зависимость силы тока от напряжения', fontsize=16, 
#           fontweight='bold', pad=15)
# plt.xlabel('Напряжение U (мВ × 1000)', fontsize=13)
# plt.ylabel('Ток I (мкА)', fontsize=13)

# # Добавление сетки
# plt.grid(True, linestyle='--', alpha=0.7, linewidth=0.8)

# # Добавление легенды
# plt.legend(fontsize=11, loc='best')

# # Добавление подписей к точкам (опционально)
# for i, (v, c) in enumerate(zip(voltage, current)):
#     plt.annotate(f'{c}', xy=(v, c), xytext=(5, 5), 
#                  textcoords='offset points', fontsize=8, alpha=0.7)

# # Отображение графика
# plt.tight_layout()
# plt.show()


# import matplotlib.pyplot as plt
# import numpy as np

# # Данные из таблицы
# frequency = np.array([0.1, 0.2, 0.5, 1, 2, 5, 10, 20])  # Частота, Гц
# u_ratio = np.array([3.0816327, 4.3, 5.857142857, 5.28, 5.4897959, 3.34, 1.5510204, 0.54])  # Uвых/Uвх

# # Создание графика
# plt.figure(figsize=(10, 6))
# plt.plot(frequency, u_ratio, 'o-', linewidth=2, markersize=8, color='blue')

# # Настройка графика
# plt.xlabel('Частота f, Гц', fontsize=12)
# plt.ylabel('Коэффициент передачи Uвых/Uвх', fontsize=12)
# plt.title('Амплитудно-частотная характеристика (АЧХ)', fontsize=14, fontweight='bold')
# plt.grid(True, alpha=0.3)

# # Установка масштаба по оси X (логарифмический лучше для такого диапазона)
# plt.xscale('log')

# # Добавление значений на график
# for i, (f, u) in enumerate(zip(frequency, u_ratio)):
#     plt.annotate(f'{u:.2f}', (f, u), textcoords="offset points", 
#                  xytext=(0,10), ha='center', fontsize=9)

# plt.tight_layout()
# plt.show()

# # Вывод таблицы данных
# print("Таблица данных:")
# print("-" * 40)
# print(f"{'Частота (Гц)':<15} {'Uвых/Uвх':<15}")
# print("-" * 40)
# for f, u in zip(frequency, u_ratio):
#     print(f"{f:<15.1f} {u:<15.4f}")
# print("-" * 40)

# # Нахождение резонансной частоты (максимального коэффициента передачи)
# max_index = np.argmax(u_ratio)
# print(f"\nМаксимальный коэффициент передачи: {u_ratio[max_index]:.4f}")
# print(f"При частоте: {frequency[max_index]} Гц")



import matplotlib.pyplot as plt
import numpy as np

# Данные
frequency = np.array([0.1, 0.2, 0.5, 1, 2, 5, 10, 20])
u_ratio = np.array([3.08, 4.3, 5.86, 5.28, 5.49, 3.34, 1.55, 0.54])

plt.figure(figsize=(10, 6))
plt.loglog(frequency, u_ratio, 'bo-', linewidth=2, markersize=8)

# ПРАВИЛЬНАЯ настройка меток для логарифмического масштаба:
# 1. Исключаем 0, используем степени 10 или значения из данных
plt.xticks([0.1, 0.2, 0.5, 1, 2, 5, 10, 20])  # Только положительные числа
plt.yticks([0.5, 1, 2, 3, 4, 5, 6])            # Только положительные числа

# Включаем сетку для наглядности
plt.grid(True, which='both', linestyle='--', alpha=0.6)

plt.xlabel('Частота f, Гц')
plt.ylabel('Uвых/Uвх')
plt.title('Двойной логарифмический масштаб')
plt.tight_layout()
plt.show()
