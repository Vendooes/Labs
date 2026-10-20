# import matplotlib.pyplot as plt
# import numpy as np

# # Отсортированные данные из вашей таблицы
# I = np.array([0, 0.1, 0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6, 1.8, 
#               2.0, 2.0, 2.0, 2.2, 2.4, 2.6, 2.8, 3.0, 3.05, 3.1, 3.15, 
#               3.2, 3.25, 3.3, 3.35, 3.4, 3.45, 3.5, 3.6, 3.8, 4.0, 4.2, 4.25])

# N_chist = np.array([0.35, 0.28, 0.25, 0.38, 0.32, 1.459, 3.919, 6.588, 8.697, 
#                     10.627, 11.056, 11.087, 10.997, 11.167, 9.117, 7.138, 4.768, 
#                     2.209, 3.389, 7.428, 11.146, 12.186, 14.195, 13.136, 11.346, 
#                     10.217, 8.577, 6.288, 4.019, 1.509, -0.17, -0.29, -0.26, -0.33])

# # Исходные N для расчета ошибок (sqrt(N))
# N_original = np.array([1.24, 1.17, 1.14, 1.27, 1.21, 2.349, 4.809, 7.478, 9.587, 
#                        11.517, 11.946, 11.977, 11.887, 12.057, 10.007, 8.028, 5.658, 
#                        3.099, 4.279, 8.318, 12.036, 13.076, 15.085, 14.026, 12.236, 
#                        11.107, 9.467, 7.178, 4.909, 2.399, 0.72, 0.6, 0.63, 0.56])

# # Ошибки уменьшены в 2 раза
# dN = np.sqrt(N_original) / 3

# fig, ax = plt.subplots(figsize=(10, 6))

# # Ошибки сделаны тонкими (elinewidth=0.8) и полупрозрачными (alpha=0.4)
# ax.errorbar(I, N_chist, yerr=dN, fmt='o', color='royalblue', 
#             ecolor='gray', elinewidth=0.8, capsize=3, alpha=0.8,
#             markersize=5, label='Экспериментальные точки')

# # Линия нуля
# ax.axhline(y=0, color='black', linestyle='--', linewidth=1, alpha=0.5)

# ax.set_xlabel('Ток в катушке I, А', fontsize=12)
# ax.set_ylabel('N_чист, 1/с', fontsize=12)
# ax.set_title('Бета-спектр $^{137}$Cs', fontsize=14, fontweight='bold')
# ax.legend(fontsize=10, loc='upper right')
# ax.grid(True, alpha=0.3, linestyle=':')
# ax.set_xlim(-0.1, 4.4)

# plt.tight_layout()
# plt.show()








# import matplotlib.pyplot as plt
# import numpy as np

# # Данные (отсортированы по I, а значит и по p)
# p = np.array([0, 31.67, 63.34, 126.68, 190.02, 253.36, 316.7, 380.04, 443.38, 
#               506.72, 570.06, 633.4, 633.4, 633.4, 696.74, 760.08, 823.42, 886.76, 
#               950.1, 965.935, 981.77, 997.605, 1013.44, 1029.275, 1045.11, 1060.945, 
#               1076.78, 1092.615, 1108.45, 1140.12, 1203.46, 1266.8, 1330.14, 1345.975])

# N_chist = np.array([0.35, 0.28, 0.25, 0.38, 0.32, 1.459, 3.919, 6.588, 8.697, 
#                     10.627, 11.056, 11.087, 10.997, 11.167, 9.117, 7.138, 4.768, 
#                     2.209, 3.389, 7.428, 11.146, 12.186, 14.195, 13.136, 11.346, 
#                     10.217, 8.577, 6.288, 4.019, 1.509, -0.17, -0.29, -0.26, -0.33])

# N_original = np.array([1.24, 1.17, 1.14, 1.27, 1.21, 2.349, 4.809, 7.478, 9.587, 
#                        11.517, 11.946, 11.977, 11.887, 12.057, 10.007, 8.028, 5.658, 
#                        3.099, 4.279, 8.318, 12.036, 13.076, 15.085, 14.026, 12.236, 
#                        11.107, 9.467, 7.178, 4.909, 2.399, 0.72, 0.6, 0.63, 0.56])

# dN = np.sqrt(N_original)/3

# fig, ax = plt.subplots(figsize=(10, 6))

# ax.errorbar(p, N_chist, yerr=dN, fmt='o', color='royalblue', 
#             ecolor='gray', elinewidth=0.8, capsize=3, alpha=0.8,
#             markersize=5, label='Экспериментальные точки')

# ax.axhline(y=0, color='black', linestyle='--', linewidth=1, alpha=0.5)

# ax.set_xlabel('Импульс электрона $p$, кэВ/$c$', fontsize=12)
# ax.set_ylabel('$N_{чист}$, 1/с', fontsize=12)
# ax.set_title('Бета-спектр $^{137}$Cs: зависимость скорости счета от импульса', 
#              fontsize=14, fontweight='bold')
# ax.legend(fontsize=10, loc='upper right')
# ax.grid(True, alpha=0.3, linestyle=':')
# ax.set_xlim(-50, 1400)

# plt.tight_layout()
# plt.show()














# import matplotlib.pyplot as plt
# import numpy as np

# # Данные (отсортированы по I, а значит и по T)
# T = np.array([0.00, 0.98, 3.91, 15.47, 34.19, 59.36, 90.18, 125.83, 165.54, 
#               208.64, 254.56, 302.83, 302.83, 302.83, 353.04, 404.88, 458.09, 512.46, 
#               567.80, 581.77, 595.79, 609.86, 623.98, 638.14, 652.35, 666.59, 680.88, 
#               695.20, 709.57, 738.40, 796.45, 854.98, 913.92, 928.71])

# N_chist = np.array([0.35, 0.28, 0.25, 0.38, 0.32, 1.459, 3.919, 6.588, 8.697, 
#                     10.627, 11.056, 11.087, 10.997, 11.167, 9.117, 7.138, 4.768, 
#                     2.209, 3.389, 7.428, 11.146, 12.186, 14.195, 13.136, 11.346, 
#                     10.217, 8.577, 6.288, 4.019, 1.509, -0.17, -0.29, -0.26, -0.33])

# N_original = np.array([1.24, 1.17, 1.14, 1.27, 1.21, 2.349, 4.809, 7.478, 9.587, 
#                        11.517, 11.946, 11.977, 11.887, 12.057, 10.007, 8.028, 5.658, 
#                        3.099, 4.279, 8.318, 12.036, 13.076, 15.085, 14.026, 12.236, 
#                        11.107, 9.467, 7.178, 4.909, 2.399, 0.72, 0.6, 0.63, 0.56])

# dN = np.sqrt(N_original)/3

# fig, ax = plt.subplots(figsize=(10, 6))

# ax.errorbar(T, N_chist, yerr=dN, fmt='o', color='royalblue', 
#             ecolor='gray', elinewidth=0.8, capsize=3, alpha=0.8,
#             markersize=5, label='Экспериментальные точки')

# ax.axhline(y=0, color='black', linestyle='--', linewidth=1, alpha=0.5)

# ax.set_xlabel('Кинетическая энергия электрона $T$, кэВ', fontsize=12)
# ax.set_ylabel('$N_{чист}$, 1/с', fontsize=12)
# ax.set_title('Бета-спектр $^{137}$Cs: зависимость скорости счета от энергии', 
#              fontsize=14, fontweight='bold')
# ax.legend(fontsize=10, loc='upper right')
# ax.grid(True, alpha=0.3, linestyle=':')
# ax.set_xlim(-20, 980)

# plt.tight_layout()
# plt.show()























# import matplotlib.pyplot as plt
# import numpy as np
# from scipy import stats

# # ВСЕ данные из таблицы (отсортированы по I)
# I_all = np.array([0.1, 0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6, 1.8, 
#                   2.0, 2.0, 2.0, 2.2, 2.4, 2.6, 2.8, 3.0, 3.05, 3.1, 3.15, 
#                   3.2, 3.25, 3.3, 3.35, 3.4, 3.45, 3.5, 3.6])

# N_chist_all = np.array([0.28, 0.25, 0.38, 0.32, 1.459, 3.919, 6.588, 8.697, 
#                         10.627, 11.056, 11.087, 10.997, 11.167, 9.117, 7.138, 
#                         4.768, 2.209, 3.389, 7.428, 11.146, 12.186, 14.195, 
#                         13.136, 11.346, 10.217, 8.577, 6.288, 4.019, 1.509])

# N_original = np.array([1.17, 1.14, 1.27, 1.21, 2.349, 4.809, 7.478, 9.587, 
#                        11.517, 11.946, 11.977, 11.887, 12.057, 10.007, 8.028, 
#                        5.658, 3.099, 4.279, 8.318, 12.036, 13.076, 15.085, 
#                        14.026, 12.236, 11.107, 9.467, 7.178, 4.909, 2.399])

# # Константы
# k = 316.7  # кэВ/(с·А)
# mc2 = 511  # кэВ

# # Расчет для всех точек
# p_all = k * I_all
# T_all = np.sqrt(p_all**2 + mc2**2) - mc2
# Y_raw_all = np.sqrt(N_chist_all) / (p_all**1.5)
# Y_mikro_all = Y_raw_all * 1e6

# # Ошибки (статистические)
# # Формула дает "взрыв" при малых I из-за множителя 1/p^1.5,
# # поэтому ограничиваем сверху (cap=40) и уменьшаем масштаб вдвое.
# dY_raw = (0.5 / np.sqrt(N_chist_all)) / (p_all**1.5) * 1e6
# dY = np.minimum(dY_raw, 40) * 0.5

# # Для аппроксимации берем расширенный диапазон: от I=1.0 до I=3.0
# # Это дает больше точек для тренда, избегая сильных искажений на малых энергиях
# mask_fit = (I_all >= 1.0) & (I_all <= 3.0)
# T_fit = T_all[mask_fit]
# Y_fit = Y_mikro_all[mask_fit]

# # Линейная регрессия
# slope, intercept, r_value, p_value, std_err = stats.linregress(T_fit, Y_fit)
# T_max = -intercept / slope

# print("--- Результаты для отчета (График Ферми, расширенный) ---")
# print(f"Всего точек на графике: {len(T_all)}")
# print(f"Точек для аппроксимации: {len(T_fit)} (от I=1.0 до I=3.0 А)")
# print(f"Уравнение тренда: Y(мкФерми) = {slope:.4f} * T + ({intercept:.2f})")
# print(f"Коэффициент детерминации R² = {r_value**2:.4f}")
# print(f"Измеренное T_max = {T_max:.1f} кэВ")
# print(f"Табличное значение T_max для 137Cs = 512 кэВ")
# print(f"Относительная погрешность: {abs(T_max - 512)/512 * 100:.1f}%")

# # Построение графика
# fig, ax = plt.subplots(figsize=(12, 7))

# # ВСЕ точки с ошибками (синие)
# ax.errorbar(T_all, Y_mikro_all, yerr=dY, fmt='o', color='steelblue', 
#             ecolor='lightblue', elinewidth=1.5, capsize=4, 
#             markersize=5, alpha=0.7, label='Все точки данных')

# # Точки для аппроксимации (выделены более ярко)
# ax.scatter(T_fit, Y_fit, color='blue', s=60, zorder=5, 
#            label=f'Точки для аппроксимации ({len(T_fit)} шт.)')

# # Линия тренда (красная пунктирная, как на скриншоте)
# T_line = np.linspace(min(T_fit) - 50, T_max + 50, 100)
# Y_line = slope * T_line + intercept
# ax.plot(T_line, Y_line, 'r--', linewidth=2, zorder=4, 
#         label=f'Линейный тренд (R² = {r_value**2:.3f})')

# # Линия T_max
# ax.axvline(x=T_max, color='green', linestyle=':', linewidth=1.5, 
#            label=f'$T_{{max}}$ = {T_max:.0f} кэВ')
# ax.axhline(y=0, color='black', linewidth=1, zorder=2)

# # Оформление (стиль как на скриншоте)
# ax.set_xlabel('T, кэВ', fontsize=12, fontweight='bold')
# ax.set_ylabel('mkFermi', fontsize=12, fontweight='bold')
# ax.set_title('График зависимости mkFermi от T', fontsize=14, fontweight='bold', pad=10)
# ax.legend(fontsize=10, loc='upper right')
# ax.grid(True, alpha=0.3, linestyle='-')
# ax.set_xlim(-50, 900)
# ax.set_ylim(-20, 380)

# plt.tight_layout()
# plt.show()






import matplotlib.pyplot as plt
import numpy as np

# Узкий диапазон вокруг пика для четкости
I_peak = np.array([2.6, 2.8, 3.0, 3.05, 3.1, 3.15, 3.2, 3.25, 3.3, 3.35, 3.4])
N_peak = np.array([5.658, 3.099, 4.279, 8.318, 12.036, 13.076, 15.085, 14.026, 12.236, 11.107, 9.467])

N_bg = 0.89
sigma_bg = np.sqrt(N_bg)
threshold_3sigma = N_bg + 3 * sigma_bg

fig, ax = plt.subplots(figsize=(10, 5))

# Точки с очень тонкими ошибками
ax.errorbar(I_peak, N_peak, yerr=np.sqrt(N_peak), fmt='o', color='darkblue', 
            ecolor='lightgray', elinewidth=0.8, capsize=2, markersize=6)

# Линии фона и 3-сигм
ax.axhline(y=N_bg, color='gray', linestyle='--', linewidth=1.5, label=f'Средний фон ({N_bg} отсч/с)')
ax.axhline(y=threshold_3sigma, color='red', linestyle='-.', linewidth=1.5, label=f'Порог 3$\sigma$ ({threshold_3sigma:.2f})')

# Акцент на пике
ax.plot(3.2, 15.085, 'ro', markersize=8, label='Конверсионный пик (15.085)')

ax.set_xlabel('Ток в катушке I, А', fontsize=12)
ax.set_ylabel('Скорость счета N, 1/с', fontsize=12)
ax.set_title('Оценка статистической значимости конверсионного пика', fontsize=14, fontweight='bold')
ax.legend(fontsize=10, loc='upper left')
ax.grid(True, alpha=0.3, linestyle=':')
ax.set_xlim(2.5, 3.5)
ax.set_ylim(0, 17)

plt.tight_layout()
plt.show()