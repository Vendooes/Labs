import numpy as np
import matplotlib.pyplot as plt

# Данные из таблицы
T_td = np.array([1220, 1320, 1420, 1520, 1620, 1720, 1820, 1920, 2020, 2120, 2220])
P    = np.array([0.77, 1.02, 1.36, 1.78, 2.09, 2.80, 3.60, 4.29, 5.27, 6.36, 7.96])

# Логарифмируем
x = np.log(T_td)
y = np.log(P)

w = P**2
w = w / np.mean(w)  # нормировка (не обязательна, но удобна)


Sw   = np.sum(w)
Swx  = np.sum(w * x)
Swy  = np.sum(w * y)
Swxx = np.sum(w * x * x)
Swxy = np.sum(w * x * y)

denom = Sw * Swxx - Swx**2
b = (Sw * Swxy - Swx * Swy) / denom
a = (Swy - b * Swx) / Sw

residuals = y - (a + b * x)
chi2 = np.sum(w * residuals**2)
s2 = chi2 / (len(x) - 2)  # дисперсия взвешенных остатков

sigma_b = np.sqrt(s2 * Sw / denom)
sigma_a = np.sqrt(s2 * Swxx / denom)

print("=" * 50)
print("Взвешенный МНК:  ln(P) = a + b · ln(T_тд)")
print("=" * 50)
print(f"  a (своб. член)  = {a:.4f}  ±  {sigma_a:.4f}")
print(f"  b (наклон)      = {b:.4f}  ±  {sigma_b:.4f}")
print(f"  χ²/(N-2)        = {s2:.4f}")
print("=" * 50)

x_fit = np.linspace(x.min() - 0.05, x.max() + 0.05, 200)
y_fit = a + b * x_fit

fig, ax = plt.subplots(figsize=(8, 6))

sigma_y = 1.0 / np.sqrt(w)  # условные погрешности
ax.errorbar(x, y, yerr=sigma_y, fmt='o', color='red',
            label='Эксп. данные', capsize=4, zorder=5)

# Линия аппроксимации
ax.plot(x_fit, y_fit, 'b-', linewidth=2,
        label=f'МНК: ln(P) = {a:.3f} + {b:.3f}·ln(T_тд)')

ax.set_xlabel('ln(T_тд)', fontsize=14)
ax.set_ylabel('ln(P)', fontsize=14)
ax.set_title('Зависимость ln(P) от ln(T_тд)\n(взвешенный МНК)', fontsize=14)
ax.legend(fontsize=11)
ax.grid(True, alpha=0.4)

textstr = (f'a = {a:.4f} ± {sigma_a:.4f}\n'
           f'b = {b:.4f} ± {sigma_b:.4f}')
ax.text(0.05, 0.95, textstr, transform=ax.transAxes,
        fontsize=11, verticalalignment='top',
        bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

plt.tight_layout()
plt.savefig('lnP_vs_lnTtd.png', dpi=150)
plt.show()






# import numpy as np
# import matplotlib.pyplot as plt

# # ══════════════════════════════════════════════════
# # Данные из первой таблицы
# # ═══════════════════════════════════════════════════
# T_td = np.array([1220, 1320, 1420, 1520, 1620, 1720, 1820, 1920, 2020, 2120, 2220])
# P    = np.array([0.77, 1.02, 1.36, 1.78, 2.09, 2.80, 3.60, 4.29, 5.27, 6.36, 7.96])

# # ═══════════════════════════════════════════════════
# # Данные из второй таблицы: ε_T(T)
# # ═══════════════════════════════════════════════════
# T_tab = np.array([800, 900, 1000, 1100, 1200, 1300, 1400, 1500,
#                   1600, 1700, 1800, 1900, 2000])
# eps_tab = np.array([0.067, 0.081, 0.105, 0.119, 0.133, 0.144, 0.164, 0.179,
#                     0.195, 0.209, 0.223, 0.236, 0.249])

# # Интерполяция ε_T для значений T_тд (линейная, с экстраполяцией)
# eps_T = np.interp(T_td, T_tab, eps_tab,
#                   left=eps_tab[0] + (T_td[0]-T_tab[0])*(eps_tab[1]-eps_tab[0])/(T_tab[1]-T_tab[0]),
#                   right=eps_tab[-1] + (T_td[-1]-T_tab[-1])*(eps_tab[-1]-eps_tab[-2])/(T_tab[-1]-T_tab[-2]))

# print("T_тд, K  |  ε_T (интерп.)")
# print("-" * 30)
# for t, e in zip(T_td, eps_T):
#     print(f"  {t:5d}   |   {e:.4f}")

# # ═══════════════════════════════════════════════════
# # B = σ · S,  S = 0.36 см² = 0.36·10⁻ м²
# # ═══════════════════════════════════════════════════
# sigma_SB = 5.670374419e-8   # Вт/(м²·К⁴)
# S = 0.36e-4                 # м²
# B_theory = sigma_SB * S
# print(f"\nB_теор = σ·S = {B_theory:.4e} Вт/К⁴")
# print(f"ln(B_теор) = {np.log(B_theory):.4f}")

# # ═══════════════════════════════════════════════════
# # Переменные для МНК
# # ═══════════════════════════════════════════════════
# x = np.log(T_td)
# y = np.log(P / eps_T)       # ln(P/ε_T) = ln(B) + n·ln(T_тд)

# # Веса: w  P²  (постоянная абсолютная погрешность ΔP)
# w = P**2
# w = w / np.mean(w)

# # ─── Взвешенный МНК: y = a + n·x ──
# Sw   = np.sum(w)
# Swx  = np.sum(w * x)
# Swy  = np.sum(w * y)
# Swxx = np.sum(w * x * x)
# Swxy = np.sum(w * x * y)

# denom = Sw * Swxx - Swx**2
# n_coef = (Sw * Swxy - Swx * Swy) / denom
# a_coef = (Swy - n_coef * Swx) / Sw

# # Погрешности
# residuals = y - (a_coef + n_coef * x)
# chi2 = np.sum(w * residuals**2)
# s2 = chi2 / (len(x) - 2)

# sigma_n = np.sqrt(s2 * Sw / denom)
# sigma_a = np.sqrt(s2 * Swxx / denom)

# B_fit = np.exp(a_coef)
# sigma_B = B_fit * sigma_a   # propagation: σ_B = B·σ_a

# print("\n" + "=" * 55)
# print("  Взвешенный МНК:  ln(P/ε_T) = a + n · ln(T_тд)")
# print("=" * 55)
# print(f"  n  (наклон)       = {n_coef:.4f}  ±  {sigma_n:.4f}")
# print(f"  a  (своб. член)   = {a_coef:.4f}  ±  {sigma_a:.4f}")
# print(f"  B_аппрокс = e^a   = {B_fit:.4e}  ±  {sigma_B:.4e}  Вт/К⁴")
# print(f"  B_теор            = {B_theory:.4e}  Вт/К⁴")
# print(f"  Относ. отклонение = {abs(B_fit - B_theory)/B_theory*100:.1f} %")
# print(f"  χ²/(N-2)          = {s2:.4f}")
# print("=" * 55)

# # ═══════════════════════════════════════════════════
# # График
# # ═══════════════════════════════════════════════════
# x_fit = np.linspace(x.min() - 0.1, x.max() + 0.1, 200)
# y_fit = a_coef + n_coef * x_fit

# fig, ax = plt.subplots(figsize=(9, 6))

# sigma_y = 1.0 / np.sqrt(w)
# ax.errorbar(x, y, yerr=sigma_y, fmt='o', color='red',
#             label='Эксп. данные', capsize=4, zorder=5)

# ax.plot(x_fit, y_fit, 'b-', linewidth=2,
#         label=f'МНК: n = {n_coef:.3f} ± {sigma_n:.3f}')

# ax.set_xlabel('ln(T_тд)', fontsize=14)
# ax.set_ylabel('ln(P / ε_T)', fontsize=14)
# ax.set_title('Определение показателя степени n\n'
#              'модель: P = ε_T · B · T_тдⁿ', fontsize=14)
# ax.legend(fontsize=11)
# ax.grid(True, alpha=0.4)

# textstr = (f'n  = {n_coef:.4f} ± {sigma_n:.4f}\n'
#            f'a  = {a_coef:.4f} ± {sigma_a:.4f}\n'
#            f'B  = {B_fit:.3e} Вт/К⁴\n'
#            f'(теор. {B_theory:.3e})')
# ax.text(0.05, 0.95, textstr, transform=ax.transAxes,
#         fontsize=11, verticalalignment='top',
#         bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

# plt.tight_layout()
# plt.savefig('lnP_epsT_vs_lnTtd.png', dpi=150)
# plt.show()