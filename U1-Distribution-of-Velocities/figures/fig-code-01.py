import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['xtick.major.size'] = 0
plt.rcParams['ytick.major.size'] = 0

v = np.linspace(0, 5, 500)
dNvdv = v**2 * np.exp(-v**2)
T = 1
fv_1 = v**2 * np.exp(-v**2 / T) / T**1.5

T = 2
fv_2 = v**2 * np.exp(-v**2 / T) / T**1.5

T = 4
fv_3 = v**2 * np.exp(-v**2 / T) / T**1.5

plt.figure(figsize=(10, 6))

plt.box(False)
plt.axhline(0, c='k', lw=1.5)
plt.axvline(0, c='k', lw=1.5)
plt.plot(v, fv_1)
plt.plot(v, fv_2)
plt.plot(v, fv_3)
plt.xlim(min(v), max(v))
plt.ylim(min(fv_1), 1.2*max(fv_1))
plt.text(1.3*v[np.argmax(fv_1)], 0.9*max(fv_1), r'$T_1$', fontsize=16)
plt.text(1.3*v[np.argmax(fv_2)], 0.9*max(fv_2), r'$T_2$', fontsize=16)
plt.text(1.3*v[np.argmax(fv_3)], 0.9*max(fv_3), r'$T_3$', fontsize=16)
plt.text(1.8*v[np.argmax(fv_3)], 0.9*max(fv_1), r'$T_1<T_2<T_3$', fontsize=16)
plt.xticks([0, max(v)], [r'$0$', r'$v$'], fontsize=16)
plt.yticks([1.2*max(fv_1)], [r'$f_v$'], fontsize=16)
plt.show()