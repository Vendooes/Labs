import numpy as np
import matplotlib.pyplot as plt

# Исходные данные
names = [r'$H_\alpha$', r'$H_\beta$', r'$H_\gamma$', r'$H_\delta$']
lam = np.array([6566, 4857, 4337, 4100])   # длины волн, ангстремы
n   = np.array([3, 4, 5, 6])               # квантовые числа

x = 1/4 - 1/n**2        # безразмерная переменная (1/4 - 1/n^2)
y = 1e8 / lam           # 1/lambda, см^-1

# Аппроксимация прямой y = k*x + b (МНК)
k, b = np.polyfit(x, y, 1)

print(f"k = {k:.1f} см^-1,  b = {b:.1f} см^-1")

# График
xs = np.linspace(0.13, 0.235, 100)
plt.figure(figsize=(7, 5))
plt.plot(xs, k*xs + b, 'b-', lw=2,
         label=f'аппроксимация: 1/λ = {k:.0f}·x {b:+.0f}')
plt.plot(x, y, 'ro', ms=8, label='эксперимент')
for xi, yi, nm in zip(x, y, names):
    plt.annotate(nm, (xi, yi), textcoords='offset points', xytext=(8, -4))
plt.xlabel(r'$(1/4 - 1/n^2)$')
plt.ylabel(r'$1/\lambda$, см$^{-1}$')
plt.title('Серия Бальмера')
plt.grid(True)
plt.legend()
plt.show()