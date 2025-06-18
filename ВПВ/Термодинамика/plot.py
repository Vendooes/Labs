import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import R

# Характеристические температуры для H2 (K)
theta_rot = 85.4    # вращательная
theta_vib = 6332    # колебательная

# Функции для компонент теплоемкости
def c_v_trans():
    return 1.5 * R  # поступательная

def c_v_rot(T):
    x = theta_rot / T
    return R * x**2 * np.exp(x) / (np.exp(x) - 1)**2  # вращательная

def c_v_vib(T):
    x = theta_vib / T
    # Учет высокотемпературного предела
    mask = x < 1e-6
    result = np.zeros_like(T)
    result[mask] = R  # T >> theta_vib
    # Стандартная формула для остальных случаев
    x_valid = x[~mask]
    exp_val = np.exp(x_valid)
    result[~mask] = R * (x_valid**2) * exp_val / (exp_val - 1)**2
    return result

# Диапазон температур (K)
T = np.logspace(0.3, 5, 1000)  # от 2 до 100000 K в логарифмическом масштабе
C_v_trans = c_v_trans()
C_v_rot = c_v_rot(T)
C_v_vib = c_v_vib(T)
C_v_total = C_v_trans + C_v_rot + C_v_vib

# Построение графика
plt.figure(figsize=(12, 8))
plt.plot(T, C_v_total / R, 'k-', lw=2, label='Total $C_v / R$')
plt.plot(T, C_v_trans / R * np.ones_like(T), 'b--', label='Translational $C_v$')
plt.plot(T, C_v_rot / R, 'g-.', label='Rotational $C_v$')
plt.plot(T, C_v_vib / R, 'r:', label='Vibrational $C_v$')

# Области замораживания
plt.axvline(x=theta_rot, color='gray', linestyle=':', alpha=0.7)
plt.axvline(x=theta_vib, color='gray', linestyle=':', alpha=0.7)
plt.text(theta_rot/2, 0.5, 'Rotational\nFreezing', ha='center', fontsize=10)
plt.text(theta_vib*2, 3.2, 'Vibrational\nFreezing', ha='center', fontsize=10)

# Настройки графика
plt.xscale('log')
plt.xlabel('Temperature (K)', fontsize=12)
plt.ylabel('$C_v / R$', fontsize=12)
plt.title('Molar Heat Capacity $C_v$ of $H_2$', fontsize=14)
plt.legend(fontsize=10)
plt.grid(True, which="both", ls="--", alpha=0.5)
plt.ylim(0, 4.5)
plt.xlim(2, 1e5)
plt.tight_layout()
plt.show()