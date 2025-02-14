import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

f = pd.read_csv('iris_data.csv')

fig = plt.figure(figsize = (16,16)) 
ax1 = fig.add_subplot(711)
ax2 = fig.add_subplot(712)
ax3 = fig.add_subplot(713)
ax4 = fig.add_subplot(714)
ax5 = fig.add_subplot(715)
ax6 = fig.add_subplot(716)
ax7 = fig.add_subplot(717)

ax1.scatter([f['SepalLengthCm']], [f['SepalWidthCm']])
ax2.scatter([f['SepalLengthCm']], [f['PetalLengthCm']])
ax3.scatter([f['SepalLengthCm']], [f['PetalWidthCm']])
ax4.scatter([f['SepalWidthCm']], [f['PetalLengthCm']])
ax5.scatter([f['SepalWidthCm']], [f['PetalWidthCm']])
ax6.scatter([f['PetalLengthCm']], [f['PetalWidthCm']])

x = [0, 8.0]
y = np.interp(x, f['SepalLengthCm']+f['SepalLengthCm']+f['SepalLengthCm']+f['SepalWidthCm'], f['SepalWidthCm']+f['PetalLengthCm']+f['PetalWidthCm']+f['PetalLengthCm'])
ax7.plot(x,y, 'r')
print(f'Коэффициенты мнк: {y}')
plt.show()