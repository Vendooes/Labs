import numpy as np
import matplotlib.pyplot as plt

T_td = np.array([1220, 1320, 1420, 1520, 1620,
                 1720, 1820, 1920, 2020, 2120, ], dtype=float)
P    = np.array([0.77, 1.02, 1.36, 1.78, 2.09,
                 2.80, 3.60, 4.29, 5.27, 6.36, ], dtype=float)


weights = 1.0 / P**2


degree = 2
# numpy.polyfit поддерживает веса через параметр w
coeffs = np.polyfit(T_td, P, deg=degree, w=np.sqrt(weights))


P_fit = np.polyval(coeffs, T_td)

# Для плавной кривой на графике
T_smooth = np.linspace(T_td.min(), T_td.max(), 200)
P_smooth = np.polyval(coeffs, T_smooth)

a, b, c = coeffs
print(f"Аппроксимация: P(T) = {a:.6e}·T² + {b:.6e}·T + {c:.4f}")

residuals = P - P_fit
chi2 = np.sum(weights * residuals**2)
print(f"Взвешенная сумма квадратов остатков (χ²) = {chi2:.4f}")
print(f"Среднеквадратичное отклонение (невзвешенное) = "
      f"{np.sqrt(np.mean(residuals**2)):.4f} Вт")

fig, ax = plt.subplots(figsize=(9, 6))

sizes = 80 * weights / weights.max()
ax.scatter(T_td, P, s=sizes, c='red', zorder=5,
           label='Эксперимент (размер ∝ вес)', edgecolors='black')

ax.plot(T_smooth, P_smooth, 'b-', linewidth=2,
        label=f'Взвешенный МНК (степень {degree})')

for ti, pi, pfi in zip(T_td, P, P_fit):
    ax.plot([ti, ti], [pi, pfi], 'g--', alpha=0.5, linewidth=1)

ax.set_xlabel('T_тд, К', fontsize=13)
ax.set_ylabel('P, Вт', fontsize=13)
ax.set_title('Зависимость мощности P от температуры T_тд\n'
             'аппроксимация взвешенным МНК (w = 1/P²)', fontsize=13)
ax.legend(fontsize=11)
ax.grid(True, alpha=0.4)

plt.tight_layout()
plt.savefig('P_vs_Ttd_WLS.png', dpi=150)
plt.show()