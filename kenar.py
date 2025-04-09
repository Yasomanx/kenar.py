import matplotlib.pyplot as plt
from pylab import *

x = [2, -3, -1.5, 3]
y = [3, 1, -2.5, -2]
color = ['m', 'g', 'r', 'b']

fig = plt.figure()
ax = fig.add_subplot(111)

scatter(x, y, s=100, marker='o', c=color)
a = [2, 3]
b = [3, -2]


plt.plot([a[0], a[1]], [b[0], b[1]], 'ro-')

for i in range(len(y)):
    plt.plot([3, -2], [3, -2], 'k-', linewidth=2, label='Eğimli Çizgi')
    plt.legend()

    plt.plot(x[i:i + 2], y[i:i + 2], 'ro-')

left, right = ax.get_xlim()
low, high = ax.get_ylim()
arrow(left, 0, right - left, 0, length_includes_head=True, head_width=0.15)
arrow(0, low, 0, high - low, length_includes_head=True, head_width=0.15)
xpoints = ypoints = ax.get_xlim()
ax.plot(xpoints, ypoints, linestyle='-', color='k', lw=3, scalex=False, scaley=False)
grid()
show()
