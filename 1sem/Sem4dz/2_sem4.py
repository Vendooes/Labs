import matplotlib.pyplot as plt
import numpy as np
fig = plt.figure(figsize = (16,9)) 
ax1 = fig.add_subplot(311) 
ax2 = fig.add_subplot(312)
ax3 = fig.add_subplot(313)
size1= 500
pos = 0
values = np.random.normal(pos, 10, size1)
ax1.hist(values, 50)
ax1.set_title('500')

size1= 5000
pos = 0
values = np.random.normal(pos, 10, size1)
ax2.hist(values, 50)
ax2.set_title('5000')

size1= 50000
pos = 0
values = np.random.normal(pos, 10, size1)
ax3.hist(values, 50)
ax3.set_title('50000')

plt.show()