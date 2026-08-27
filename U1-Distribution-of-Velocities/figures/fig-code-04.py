import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['xtick.major.size'] = 0
plt.rcParams['ytick.major.size'] = 0

E = np.linspace(0, 5, 500)
T = 1
fE = E**0.5 * np.exp(-E / T) / T**1.5

plt.figure(figsize=(10, 6))

plt.box(False)
plt.axhline(0, c='k', lw=1.5)
plt.axvline(0, c='k', lw=1.5)
plt.plot(E, fE)

plt.xlim(min(E), max(E))
plt.ylim(min(fE), 1.2*max(fE))
plt.xticks([0, max(E)], [r'$0$', r'$E/k_BT$'], fontsize=16)
plt.yticks([1.2*max(fE)], [r'$f_E$'], fontsize=16)
plt.show()