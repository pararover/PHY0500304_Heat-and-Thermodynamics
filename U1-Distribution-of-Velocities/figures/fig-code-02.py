import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['xtick.major.size'] = 0
plt.rcParams['ytick.major.size'] = 0

v = np.linspace(0, 3, 500)
dNvdv = v**2 * np.exp(-v**2)
T = 1
#fv_1 = v**2 * np.exp(-v**2 / T) / T**1.5
fv_1 = v**2 * np.exp(-v**2 / T) / T**1.5
fv_quad = v**2
fv_exp = np.exp(-v**2 / T) / T**1.5

plt.figure(figsize=(10, 6))

plt.box(False)
plt.axhline(0, c='k', lw=1.5)
plt.axvline(0, c='k', lw=1.5)
plt.plot(v, fv_quad, 'b--', label=r'$v^2$')
plt.plot(v, fv_exp, 'r--', label=r'$e^{-mv^2/2k_BT}$')
plt.plot(v, fv_1, 'k', lw=2.0, label=r'$f_v$')
plt.legend(fontsize=16)
plt.xlim(min(v), max(v))
plt.ylim(min(fv_1), 3*max(fv_1))
plt.xticks([0, max(v)], [r'$0$', r'$v$'], fontsize=16)
#plt.yticks([3*max(fv_1)], [r'$f_v$'], fontsize=16)
plt.yticks([], [], fontsize=16)
plt.show()