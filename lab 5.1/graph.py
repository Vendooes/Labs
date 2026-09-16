import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def linear_model(x, k, b):
    return k * x + b

datasets = [
    {
        'name': 'Fe (до 7.2)',
        'x': np.array([0, 1.03, 2.06, 3.09, 4.11, 5.14, 6.17, 7.2]),
        'y': np.array([0.00, 0.59, 1.17, 1.72, 2.26, 2.80, 3.38, 3.87]),
        'color': 'red',
        'marker': 'o'
    },
    {
        'name': 'Al (до 14.7)',
        'x': np.array([0, 2.1, 4.2, 6.3, 8.4, 10.5, 12.6, 14.7]),
        'y': np.array([0.00, 0.42, 0.83, 1.23, 1.62, 2.02, 2.42, 2.81]),
        'color': 'blue',
        'marker': 's'
    },
    {
        'name': 'Pb (до 3.36)',
        'x': np.array([0, 0.48, 0.96, 1.44, 1.92, 2.4, 2.88, 3.36]),
        'y': np.array([0.00, 0.58, 1.13, 1.69, 2.21, 2.79, 3.30, 3.76]),
        'color': 'green',
        'marker': '^'
    },
    {
        'name': 'пробка (до 13.58)',
        'x': np.array([0, 1.94, 3.88, 5.82, 7.76, 9.7, 11.64, 13.58]),
        'y': np.array([0.00, 0.01, 0.03, 0.06, 0.07, 0.09, 0.11, 0.12]),
        'color': 'purple',
        'marker': 'D'
    }
]

fig, ax = plt.subplots(figsize=(12, 8))

print("=" * 60)
print(f"{'Материал':<20} | {'k (наклон)':<10} | {'b (сдвиг)':<10} | {'chi^2':<10}")
print("=" * 60)

for ds in datasets:
    x, y = ds['x'], ds['y']
    

    sigma_y = np.ones_like(y) * 0.1 
    

    popt, pcov = curve_fit(linear_model, x, y, sigma=sigma_y, absolute_sigma=True)
    
    k_fit, b_fit = popt
    
    y_model = linear_model(x, k_fit, b_fit)                    
    residuals = y - y_model                                   
    chi_squared = np.sum((residuals / sigma_y) ** 2)          
    
    print(f"{ds['name']:<20} | {k_fit:<10.4f} | {b_fit:<10.4f} | {chi_squared:<10.2f}")

    ax.scatter(x, y, color=ds['color'], marker=ds['marker'], s=80, zorder=5, label=ds['name'])
    
    x_fit = np.linspace(0, x.max() * 1.05, 100)
    y_fit = linear_model(x_fit, k_fit, b_fit)
    ax.plot(x_fit, y_fit, color=ds['color'], linewidth=2, linestyle='--')
    
    ax.text(x.max() * 0.55, k_fit * x.max() * 0.55 + 0.1,
            f'k={k_fit:.4f}\n' + r'$\chi^2$' + f'={chi_squared:.2f}', 
            fontsize=10, color=ds['color'], fontweight='bold',
            bbox=dict(facecolor='white', alpha=0.8, edgecolor=ds['color']))

ax.set_xlabel('Толщина бруска', fontsize=13)
ax.set_ylabel(r'$\ln(N_0/N)$', fontsize=13)
ax.set_title('Зависимость $\ln(N_0/N)$ от толщины бруска\n(Аппроксимация методом $\chi^2$)', fontsize=14)
ax.legend(fontsize=10, loc='upper left')
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

print("=" * 60)
print("Примечание: Хорошим считается значение chi^2, близкое к числу степеней свободы")
print("(число точек минус число параметров, т.е. n - 2).")
print("=" * 60)