import matplotlib.pyplot as plt

plt.figure()
plt.xlim(0, 5)
plt.ylim(0, 5)

for i in range(0, 5):
    plt.axhspan(i, i+.2, facecolor='0.2', alpha=0.5)
    plt.axvspan(i, i+.5, facecolor='b', alpha=0.5)

plt.show()


############## DARK BACKGROUND

import numpy as np
import matplotlib.pyplot as plt


plt.style.use('dark_background')

fig, ax = plt.subplots()

L = 6
x = np.linspace(0, L)
ncolors = len(plt.rcParams['axes.prop_cycle'])
shift = np.linspace(0, L, ncolors, endpoint=False)
for s in shift:
    ax.plot(x, np.sin(x + s), 'o-')
ax.set_xlabel('x-axis')
ax.set_ylabel('y-axis')
ax.set_title("'dark_background' style sheet")

plt.show()

################
