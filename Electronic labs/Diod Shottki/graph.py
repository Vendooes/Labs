# -*- coding: utf-8 -*-
"""
Построение графика I-V характеристики с расчётом коэффициента наклона
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy import stats  # для линейной регрессии

# ================================
# 1. ЧТЕНИЕ ДАННЫХ
# ================================
bias = []
current = []

with open('D:\Labs\Electronic labs\Diod Shottki\www.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

start_reading = False
for line in lines:
    line = line.strip()
    if not line or line.startswith('Measurement') or line.startswith('Bias'):
        continue
    if line == 'RealMeasuredPoints':
        start_reading = True
        continue
    if line == 'Bias\tCurrent\tResistance':
        continue
    if start_reading and '\t' in line:
        try:
            parts = line.split('\t')
            if len(parts) >= 2:
                b = float(parts[0])
                c = float(parts[1])
                bias.append(b)
                current.append(c)
        except:
            continue

bias = np.array(bias)
current = np.array(current)

print(f"✓ Загружено точек: {len(bias)}")

# ================================
# 2. РАСЧЁТ КОЭФФИЦИЕНТА НАКЛОНА
# ================================

# Вариант А: Средний наклон (линейная регрессия)
# Берём только ту часть, где ток меняется монотонно (убираем петлю гистерезиса)
# Для простоты — используем все данные, но можно выбрать диапазон

slope, intercept, r_value, p_value, std_err = stats.linregress(bias, current)

print(f"\n📊 Средний коэффициент наклона ВАХ:")
print(f"   G = dI/dV = {slope:.4e} А/В = {slope*1e6:.4f} мкА/В")
print(f"   Это соответствует сопротивлению: R = 1/G = {1/slope:.2f} Ом")
print(f"   Коэффициент детерминации R² = {r_value**2:.4f} (чем ближе к 1, тем лучше линейность)")

# Вариант Б: Локальный наклон (производная) — для понимания нелинейности
# Используем разности между соседними точками
dV = np.diff(bias)
dI = np.diff(current)
# Избегаем деления на ноль
local_slope = np.zeros_like(bias)
local_slope[1:] = np.where(np.abs(dV) > 1e-10, dI / dV, 0)

print(f"\n📈 Диапазон локальной проводимости:")
print(f"   Мин: {np.min(local_slope[local_slope!=0]):.4e} А/В")
print(f"   Макс: {np.max(local_slope):.4e} А/В")

# ================================
# 3. ПОСТРОЕНИЕ ГРАФИКОВ
# ================================
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 10))

# График 1: I-V характеристика + линия регрессии
ax1.plot(bias, current * 1e6, 'b-', linewidth=1, label='Измеренные данные', alpha=0.7)
# Рисуем линию линейной аппроксимации
regression_line = slope * bias + intercept
ax1.plot(bias, regression_line * 1e6, 'r--', linewidth=2, label=f'Лин. аппроксимация (G={slope*1e6:.3f} мкА/В)')

ax1.set_xlabel('Напряжение, В', fontsize=11)
ax1.set_ylabel('Ток, мкА', fontsize=11)
ax1.set_title('Вольт-амперная характеристика', fontsize=13, fontweight='bold')
ax1.grid(True, alpha=0.3, linestyle='--')
ax1.legend(fontsize=10)
ax1.axhline(y=0, color='gray', linewidth=0.5)
ax1.axvline(x=0, color='gray', linewidth=0.5)

# График 2: Локальная проводимость (производная dI/dV)
ax2.plot(bias[1:], local_slope[1:] * 1e6, 'g-', linewidth=1)
ax2.set_xlabel('Напряжение, В', fontsize=11)
ax2.set_ylabel('Локальная проводимость, мкА/В', fontsize=11)
ax2.set_title('Как меняется наклон ВАХ (производная dI/dV)', fontsize=13, fontweight='bold')
ax2.grid(True, alpha=0.3, linestyle='--')
ax2.axhline(y=0, color='gray', linewidth=0.5)
ax2.axvline(x=0, color='gray', linewidth=0.5)

# Добавим горизонтальную линию среднего значения
ax2.axhline(y=slope*1e6, color='red', linestyle=':', linewidth=1.5, label=f'Среднее: {slope*1e6:.3f} мкА/В')
ax2.legend(fontsize=9)

plt.tight_layout()
plt.show()

# ================================
# 4. ДОПОЛНИТЕЛЬНО: если нужна проводимость только для линейного участка
# ================================
# Например, возьмём диапазон от -1 В до +1 В, где кривая более линейная
mask = (bias >= -1.0) & (bias <= 1.0)
if np.sum(mask) > 10:  # если достаточно точек в этом диапазоне
    slope_linear, _, r_val, _, _ = stats.linregress(bias[mask], current[mask])
    print(f"\n🎯 На линейном участке [-1 В; +1 В]:")
    print(f"   G = {slope_linear*1e6:.4f} мкА/В")
    print(f"   R = {1/slope_linear:.2f} Ом")
    print(f"   R² = {r_val**2:.4f}")