import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Калибровочные точки
theta = np.array([2602, 2572, 2508, 2496, 2472, 2450, 2440, 2402, 2396, 2378,
                  2370, 2352, 2332, 2310, 2302, 2282, 2272, 2254, 2228, 2212,
                  2184, 2166, 1906, 1868, 1860], float)
lam   = np.array([7032, 6929, 6717, 6678, 6599, 6533, 6507, 6402, 6383, 6334,
                  6305, 6267, 6217, 6164, 6143, 6096, 6074, 6030, 5976, 5945,
                  5882, 5852, 5401, 5341, 5331], float)

# Новые точки
labels_new = ['1', '2', '3', '4', '5', '6', 'K1', 'K2']
theta_new = np.array([2135, 2124, 1945, 1526,  866,  327, 2572, 2340], float)
lam_new   = np.array([5791, 5770, 5461, 4916, 4358, 4047, 6907, 6234], float)

# Объединённый набор данных
theta_all = np.concatenate([theta, theta_new])
lam_all   = np.concatenate([lam,   lam_new])

# Формула Гартмана
def hartmann(x, l0, C, x0):
    return l0 + C / (x0 - x)

# Фит только по всем точкам (x0 ограничен снизу, чтобы не уйти в деление на ноль)
x0_min = theta_all.max() + 1.0
bounds = ([-np.inf, 0.0, x0_min], [np.inf, np.inf, 1e7])
p_all, cov_all = curve_fit(hartmann, theta_all, lam_all,
                           p0=[2700, 5e6, 3800], bounds=bounds)
l0, C, x0 = p_all
dl0, dC, dx0 = np.sqrt(np.diag(cov_all))

res = lam_all - hartmann(theta_all, *p_all)
rms = np.sqrt(np.mean(res**2))
r2  = 1 - np.sum(res**2) / np.sum((lam_all - lam_all.mean())**2)

print(f"λ(θ) = {l0:.2f} + {C:.4e} / ({x0:.2f} − θ)")
print(f"  l0 = {l0:.2f} ± {dl0:.2f},  C = {C:.3e} ± {dC:.1e},  x0 = {x0:.2f} ± {dx0:.2f}")
print(f"  RMS = {rms:.2f} Å,  R² = {r2:.6f}")

# График: все точки + одна кривая
xs = np.linspace(theta_all.min(), theta_all.max(), 500)

plt.figure(figsize=(9, 6))
plt.scatter(theta, lam, s=40, color='tab:blue', label='Неон')
plt.scatter(theta_new, lam_new, s=70, marker='^', color='tab:green',
            label='Ртуть (1–6, K1, K2)')
plt.plot(xs, hartmann(xs, *p_all), 'r-', lw=2,
         label=f'Гартман по всем точкам: {l0:.1f} + {C:.3e}/({x0:.1f}−θ)')

for lab, t, l in zip(labels_new, theta_new, lam_new):
    if lab.startswith('K'):
        plt.annotate(lab, (t, l), textcoords='offset points', xytext=(7, 7))

plt.xlabel('угол (градусы)')
plt.ylabel('длина волны (ангстрем)')
plt.title('Аппроксимация по формуле Гартмана (все точки)')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()