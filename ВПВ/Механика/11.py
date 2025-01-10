import numpy as np
import matplotlib.pyplot as plt

t = list(map(int, input().split()))

l = []
for i in t:
    a = 2*3.14*1.2*(0.045)**2*0.21*2*3.14*2*(0.5+9.81*i)
    a = round(a, 3)
    l.append(a)

fig = plt.figure(figsize=(8,5), dpi=100)

plt.plot(t, l, 'b', label='')

plt.grid()
plt.xlim(0)
plt.ylim(0)

plt.legend()

plt.title("Зависимость силы от времени")
plt.xlabel("Время(с)")
plt.ylabel("Сила (Н)")

plt.savefig('mygraph.png', dpi=300)

plt.show()
