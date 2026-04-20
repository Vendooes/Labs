import numpy as np
import matplotlib.pyplot as plt

# Экспериментальные данные
data = [
    # m, (φ1 град, мин, сек), (φ2 град, мин, сек), D_exp, σ_D
    ( 1, (163, 24, 24), (163, 28, 26), 11.62, 0.3),
    (-1, (197,  5, 40), (197,  1, 40), 11.43, 0.3),
    ( 2, (145,  9, 39), (145,  0, 41), 25.62, 0.6),
    (-2, (215, 46, 39), (215, 38, 20), 23.76, 0.8),
    ( 3, (121,  4, 59), (120, 44,  9), 59.52, 0.7),
    (-3, (241, 24, 20), (241,  0, 10), 69.05, 0.7),
]

def dms_to_deg(deg, minute, sec):
    """Перевод градусов, минут, секунд в десятичные градусы."""
    return deg + minute / 60 + sec / 3600

# Период решётки в ангстремах
d_mkm = 1.96           # мкм
d_A = d_mkm * 1e4       # 1 мкм = 10^4 Å

# Подготовка списков
m_exp, D_exp, sigma_D, D_theor = [], [], [], []

for m, phi1, phi2, d_exp, sig in data:
    # Средний угол дифракции
    theta1 = dms_to_deg(*phi1)
    theta2 = dms_to_deg(*phi2)
    theta_avg = (theta1 + theta2) / 2.0
    theta_rad = np.radians(theta_avg)
    
    # Теоретическая дисперсия (рад/Å) -> arcsec/Å
    D_t_rad_per_A = np.abs(m) / (d_A * np.abs(np.cos(theta_rad)))
    D_t_arcsec_per_A = D_t_rad_per_A * (180 * 3600 / np.pi)
    
    m_exp.append(m)
    D_exp.append(d_exp)
    sigma_D.append(sig)
    D_theor.append(D_t_arcsec_per_A)

# Сортировка по модулю m для соединительной линии
order = np.argsort(np.abs(m_exp))
m_sorted = np.array(m_exp)[order]
D_theor_sorted = np.array(D_theor)[order]

# Построение
plt.figure(figsize=(8, 6))
plt.errorbar(m_exp, D_exp, yerr=sigma_D, fmt='o', capsize=4,
             label='Эксперимент', color='blue')
plt.scatter(m_exp, D_theor, marker='s', color='red', 
            label='Теория (d = 1.96 мкм)')
plt.plot(m_sorted, D_theor_sorted, '--', color='red', alpha=0.7)

plt.xlabel('Порядок дифракции, m')
plt.ylabel('Угловая дисперсия D, arcsec/Å')
plt.title('Зависимость угловой дисперсии от порядка дифракции')
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend()
plt.tight_layout()
plt.show()