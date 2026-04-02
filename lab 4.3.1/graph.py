# import numpy as np
# import matplotlib.pyplot as plt
# from scipy import stats

# # Данные из таблицы
# n = np.array([1, 2, 3, 4])          # Число полос
# D = np.array([85.6, 86.6, 87.6, 88.0]) # Расстояние (координата) в см

# # Параметры
# lambda_m = 578e-9  # Длина волны в метрах (578 нм)

# # Выбираем координаты для линеаризации: X = 1 / (n + 1)
# X = 1 / (n + 1)
# Y = D

# # Линейная аппроксимация Y = k * X + b_intercept
# slope, intercept, r_value, p_value, std_err = stats.linregress(X, Y)

# # Расчет теоретических значений для графика
# Y_fit = slope * X + intercept

# # Расчет хи-квадрат
# # Предполагаем погрешность измерения координаты ~0.1 см (стандартная для таких работ)
# sigma_y = 0.1 
# chi2 = np.sum((Y - Y_fit)**2 / sigma_y**2)
# dof = len(n) - 2  # Число степеней свободы
# reduced_chi2 = chi2 / dof

# # Расчет ширины щели b
# # Формула: slope = - b^2 / (4 * lambda)
# # b = sqrt(-slope * 4 * lambda)
# # Внимание: slope в см, нужно перевести в метры
# slope_m = slope * 0.01 
# b_m = np.sqrt(-slope_m * 4 * lambda_m)
# b_mm = b_m * 1000 # в мм

# # Погрешность b (через погрешность наклона)
# # db/b = 0.5 * dk/k
# err_b_m = 0.5 * b_m * (std_err * 0.01 / abs(slope_m))
# err_b_mm = err_b_m * 1000

# print(f"Наклон графика (k): {slope:.4f} см")
# print(f"Свободный член (D0): {intercept:.4f} см")
# print(f"Коэффициент корреляции R^2: {r_value**2:.6f}")
# print(f"Хи-квадрат (chi2): {chi2:.4f} (при погрешности {sigma_y} см)")
# print(f"Ширина щели b: {b_mm:.4f} +/- {err_b_mm:.4f} мм")

# # Построение графика
# plt.figure(figsize=(8, 6))
# plt.plot(X, Y, 'o', label='Экспериментальные точки', markersize=10)
# plt.plot(X, Y_fit, 'r-', label=f'Аппроксимация: D = {slope:.2f}/(n+1) + {intercept:.2f}')
# plt.xlabel(r'$1 / (n + 1)$', fontsize=12)
# plt.ylabel('Координата микроскопа D (см)', fontsize=12)
# plt.title('Зависимость координаты от обратного числа зон Френеля', fontsize=14)
# plt.grid(True, linestyle='--', alpha=0.7)
# plt.legend()
# plt.tight_layout()
# plt.show()


import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
from scipy import stats

# =============================================================================
# 1. Чтение данных из файла
# =============================================================================
data = np.loadtxt('D:\Labs\lab 4.3.1\Фраунт.txt')

# Предполагаем структуру: столбцы представляют разные каналы/измерения
# Столбец 4 (индекс 3) - координата положения
# Столбцы 0, 1, 2 - интенсивности разных каналов

position = data[:, 3]  # Координата x (пиксели или условные единицы)
intensity_ch0 = data[:, 0]  # Канал 0
intensity_ch1 = data[:, 1]  # Канал 1
intensity_ch2 = data[:, 2]  # Канал 2

# =============================================================================
# 2. Построение дифракционной картины
# =============================================================================
plt.figure(figsize=(12, 8))

plt.subplot(2, 1, 1)
plt.plot(position, intensity_ch0, 'b-', linewidth=1, label='Канал 0', alpha=0.7)
plt.plot(position, intensity_ch1, 'g-', linewidth=1, label='Канал 1', alpha=0.7)
plt.plot(position, intensity_ch2, 'k-', linewidth=1, label='Канал 2', alpha=0.7)
plt.xlabel('Позиция x (усл. ед.)', fontsize=12)
plt.ylabel('Интенсивность I (усл. ед.)', fontsize=12)
plt.title('Дифракционная картина Фраунгофера на щели', fontsize=14)
plt.legend()
plt.grid(True, linestyle='--', alpha=0.5)
plt.xlim(0, 1200)

# =============================================================================
# 3. Поиск экстремумов (минимумов) для определения положений
# =============================================================================
# Для определения ширины щели используем положения МИНИМУМОВ
# Инвертируем сигнал для поиска минимумов через find_peaks

# Выбираем один канал для анализа (например, канал 2 - чёрный)
intensity = intensity_ch2

# Находим минимумы (инвертируем интенсивность)
inverted_intensity = -intensity
peaks, properties = find_peaks(inverted_intensity, 
                                prominence=10,  # Минимальная выраженность минимума
                                distance=50)     # Минимальное расстояние между минимумами

# Исключаем центральный максимум (область вокруг максимума интенсивности)
central_max_idx = np.argmax(intensity)
central_region = (position > position[central_max_idx] - 100) & (position < position[central_max_idx] + 100)

# Фильтруем минимумы, исключая центральную область
valid_minima = []
valid_minima_positions = []
for idx in peaks:
    if not central_region[idx]:
        valid_minima.append(idx)
        valid_minima_positions.append(position[idx])

valid_minima = np.array(valid_minima)
valid_minima_positions = np.array(valid_minima_positions)

# Сортируем минимумы по позиции
sort_idx = np.argsort(valid_minima_positions)
valid_minima_positions = valid_minima_positions[sort_idx]

# Присваиваем номера порядков (m = 1, 2, 3, ...)
# Минимумы с обеих сторон от центра нумеруем отдельно
center_pos = position[central_max_idx]

left_minima = valid_minima_positions[valid_minima_positions < center_pos]
right_minima = valid_minima_positions[valid_minima_positions > center_pos]

# Нумеруем минимумы
m_left = np.arange(1, len(left_minima) + 1)
m_right = np.arange(1, len(right_minima) + 1)

# =============================================================================
# 4. График зависимости положения экстремумов от номера m
# =============================================================================
plt.subplot(2, 1, 2)

# Объединяем данные для симметричной обработки
m_all = np.concatenate([m_left, m_right])
x_all = np.concatenate([left_minima, right_minima])

# Для линейной зависимости используем абсолютные расстояния от центра
x_from_center = np.abs(x_all - center_pos)

plt.plot(m_all, x_from_center, 'ro', markersize=8, label='Экспериментальные точки')

# =============================================================================
# 5. Линейная аппроксимация
# =============================================================================
# x_m = k * m, где k = λL/d
slope, intercept, r_value, p_value, std_err = stats.linregress(m_all, x_from_center)

m_fit = np.linspace(1, max(m_all), 100)
x_fit = slope * m_fit + intercept

plt.plot(m_fit, x_fit, 'b-', linewidth=2, label=f'Аппроксимация: x = {slope:.2f}·m + {intercept:.2f}')

plt.xlabel('Порядок минимума m', fontsize=12)
plt.ylabel('|x - x₀| (усл. ед.)', fontsize=12)
plt.title('Зависимость положения минимумов от порядка', fontsize=14)
plt.legend()
plt.grid(True, linestyle='--', alpha=0.5)

plt.tight_layout()
plt.savefig('diffraction_analysis.png', dpi=300)
plt.show()

# =============================================================================
# 6. Расчёт ширины щели d₂
# =============================================================================
print('=' * 60)
print('РЕЗУЛЬТАТЫ АНАЛИЗА')
print('=' * 60)

print(f'\nКоличество найденных минимумов слева: {len(left_minima)}')
print(f'Количество найденных минимумов справа: {len(right_minima)}')
print(f'Положение центрального максимума: x₀ = {center_pos:.2f}')

print(f'\n--- Параметры линейной аппроксимации ---')
print(f'Наклон графика (k): {slope:.4f} усл. ед.')
print(f'Свободный член: {intercept:.4f} усл. ед.')
print(f'Коэффициент корреляции R²: {r_value**2:.6f}')
print(f'Стандартная ошибка наклона: {std_err:.4f}')

# Для расчёта ширины щели нужны дополнительные параметры
# k = λL/d  =>  d = λL/k

# Предполагаемые параметры эксперимента (типичные для лабораторной работы)
lambda_m = 632.8e-9  # Длина волны He-Ne лазера, м
L_m = 1.0  # Расстояние от щели до экрана, м

# Если координата в пикселях, нужен масштаб (мм/пиксель)
pixel_scale = 0.01  # мм/пиксель (примерное значение, нужно уточнить)

# Перевод наклона в метры
slope_m = slope * pixel_scale * 1e-3  # м

# Расчёт ширины щели
d_m = (lambda_m * L_m) / slope_m
d_mm = d_m * 1000  # мм

# Погрешность
err_d_mm = d_mm * (std_err / slope)

print(f'\n--- Расчёт ширины щели d₂ ---')
print(f'Длина волны λ: {lambda_m*1e9:.1f} нм')
print(f'Расстояние до экрана L: {L_m:.2f} м')
print(f'Масштаб детектора: {pixel_scale*1000:.2f} мм/пиксель')
print(f'\nШирина щели d₂: {d_mm:.4f} ± {err_d_mm:.4f} мм')

# =============================================================================
# 7. Таблица положений минимумов
# =============================================================================
print(f'\n--- Положения минимумов ---')
print(f'{"m":<5} {"x_left":<12} {"x_right":<12} {"|x-x₀|":<12}')
print('-' * 45)

max_m = max(len(left_minima), len(right_minima))
for m in range(1, max_m + 1):
    x_l = left_minima[m-1] if m <= len(left_minima) else '-'
    x_r = right_minima[m-1] if m <= len(right_minima) else '-'
    if m <= len(left_minima):
        dist_l = f'{abs(left_minima[m-1] - center_pos):.2f}'
    else:
        dist_l = '-'
    if m <= len(right_minima):
        dist_r = f'{abs(right_minima[m-1] - center_pos):.2f}'
    else:
        dist_r = '-'
    print(f'{m:<5} {str(x_l):<12} {str(x_r):<12} {dist_l if dist_l != "-" else dist_r:<12}')

print('=' * 60)