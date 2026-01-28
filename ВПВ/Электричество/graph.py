import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq
import warnings
warnings.filterwarnings('ignore')

# Параметры сигнала
f0 = 10e6  # Несущая частота, Гц (10 МГц)
fm = 1e3   # Частота модуляции, Гц (1 кГц)
m = 0.8    # Глубина модуляции
J0 = 1.0   # Амплитуда тока, мА

# Увеличиваем длительность сигнала для лучшего частотного разрешения
duration = 0.01  # Длительность сигнала, с (10 мс)
fs = 50e6  # Частота дискретизации (50 МГц - достаточно по теореме Найквиста)

# Время
t = np.arange(0, duration, 1/fs)

# 1. Модулированный сигнал (временная область)
J = J0 * (1 + m * np.sin(2 * np.pi * fm * t)) * np.sin(2 * np.pi * f0 * t)

# 2. Быстрое преобразование Фурье (БПФ)
n = len(t)
J_fft = fft(J)
frequencies = fftfreq(n, 1/fs)

# 3. Вычисляем амплитуды (односторонний спектр)
amplitude = np.abs(J_fft) / (n/2)  # Нормализация
amplitude[0] = amplitude[0] / 2  # Нулевая частота

# 4. Берем только положительные частоты
positive_freq_idx = frequencies >= 0
freq_pos = frequencies[positive_freq_idx]
amp_pos = amplitude[positive_freq_idx]

# 5. Создаем фигуру
fig, axes = plt.subplots(3, 1, figsize=(12, 12))

# 5.1 Временная область (первые 100 μs)
ax1 = axes[0]
samples_to_show = int(0.0001 * fs)  # 100 мкс
t_micro = t[:samples_to_show] * 1e6  # Переводим в микросекунды
J_micro = J[:samples_to_show]
ax1.plot(t_micro, J_micro, 'b-', linewidth=1.5)
ax1.set_xlabel('Время, μs')
ax1.set_ylabel('Ток, мА')
ax1.set_title('АМ-сигнал во временной области (первые 100 μs)')
ax1.grid(True, alpha=0.3)
ax1.axhline(y=0, color='k', linestyle='-', alpha=0.3)

# 5.2 Спектр (узкий диапазон вокруг несущей)
ax2 = axes[1]
# Выделяем область вокруг несущей частоты ± 3 кГц
f_center = f0
bandwidth = 3e3
mask = (freq_pos >= f_center - bandwidth) & (freq_pos <= f_center + bandwidth)
freq_band = freq_pos[mask]
amp_band = amp_pos[mask]

ax2.plot(freq_band / 1e6, amp_band, 'r-', linewidth=2)
ax2.set_xlabel('Частота, МГц')
ax2.set_ylabel('Амплитуда, мА')
ax2.set_title(f'Спектр АМ-сигнала (область {f_center/1e6:.3f} МГц ± {bandwidth/1e3} кГц)')
ax2.grid(True, alpha=0.3)

# 5.3 Спектр с выделенными боковыми полосами (stem plot)
ax3 = axes[2]

# Находим индексы ближайших к теоретическим частотам
f_lower = f0 - fm
f_upper = f0 + fm
f_center = f0

# Находим ближайшие индексы в массиве частот
idx_lower = np.argmin(np.abs(freq_band - f_lower))
idx_upper = np.argmin(np.abs(freq_band - f_upper))
idx_center = np.argmin(np.abs(freq_band - f_center))

# Создаем stem plot для наглядности
markerline, stemlines, baseline = ax3.stem(
    freq_band / 1e6, 
    amp_band, 
    linefmt='b-', 
    markerfmt='bo', 
    basefmt='k-'
)

# Подсвечиваем боковые полосы
markerline._color = 'red'
markerline._markersize = 8

# Подсвечиваем несущую и боковые полосы
if idx_lower < len(freq_band):
    ax3.plot(freq_band[idx_lower] / 1e6, amp_band[idx_lower], 'ro', markersize=10, label=f'НБП: {freq_band[idx_lower]/1e6:.6f} МГц')
if idx_upper < len(freq_band):
    ax3.plot(freq_band[idx_upper] / 1e6, amp_band[idx_upper], 'go', markersize=10, label=f'ВБП: {freq_band[idx_upper]/1e6:.6f} МГц')
if idx_center < len(freq_band):
    ax3.plot(freq_band[idx_center] / 1e6, amp_band[idx_center], 'mo', markersize=10, label=f'Несущая: {freq_band[idx_center]/1e6:.6f} МГц')

ax3.set_xlabel('Частота, МГц')
ax3.set_ylabel('Амплитуда, мА')
ax3.set_title('Спектр АМ-сигнала с выделенными боковыми полосами (stem plot)')
ax3.grid(True, alpha=0.3)
ax3.legend()

# Устанавливаем одинаковые пределы по x для всех графиков спектра
x_limits = [f_center/1e6 - bandwidth/1e6, f_center/1e6 + bandwidth/1e6]
ax2.set_xlim(x_limits)
ax3.set_xlim(x_limits)

# Увеличиваем пределы по y для лучшей видимости боковых полос
max_amp = np.max(amp_band)
ax2.set_ylim([0, max_amp * 1.1])
ax3.set_ylim([0, max_amp * 1.1])

plt.tight_layout()
plt.show()

# 6. Выводим информацию о найденных пиках
print("НАЙДЕННЫЕ ПИКИ В СПЕКТРЕ:")
print("-" * 50)

# Находим локальные максимумы
from scipy.signal import find_peaks
peaks, properties = find_peaks(amp_band, height=0.1)  # Ищем пики с амплитудой > 0.1

for i, peak_idx in enumerate(peaks):
    freq_hz = freq_band[peak_idx]
    amplitude_ma = amp_band[peak_idx]
    print(f"Пик {i+1}:")
    print(f"  Частота: {freq_hz:.3f} Гц ({freq_hz/1e6:.6f} МГц)")
    print(f"  Амплитуда: {amplitude_ma:.4f} мА")
    print(f"  Отклонение от несущей: {(freq_hz - f0):.1f} Гц")
    print()

print("ТЕОРЕТИЧЕСКИЕ ЗНАЧЕНИЯ:")
print(f"Несущая частота: {f0:.0f} Гц ({f0/1e6:.6f} МГц)")
print(f"Нижняя боковая полоса (НБП): {f_lower:.0f} Гц ({f_lower/1e6:.6f} МГц)")
print(f"Верхняя боковая полоса (ВБП): {f_upper:.0f} Гц ({f_upper/1e6:.6f} МГц)")
print(f"\nТеоретические амплитуды:")
print(f"  Несущая: {J0:.2f} мА")
print(f"  Боковые полосы: {J0 * m / 2:.3f} мА (каждая)")
print(f"\nГлубина модуляции: m = {m}")
print(f"Разнос частот: {fm/1e3:.1f} кГц")