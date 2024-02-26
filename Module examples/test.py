#plot y= tanx and y=x in the range [1,5]
import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(1, 5, 100)
y1 = np.tan(x)-x

plt.plot(x, y1, '-r', label='y=tanx-x')
# draw a bisector at x =0
plt.axhline(0, color='black', lw=1)


plt.legend(loc='upper left')
plt.ylim(-10, 10)
plt.show()
