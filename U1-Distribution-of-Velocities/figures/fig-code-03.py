import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['xtick.major.size'] = 0
plt.rcParams['ytick.major.size'] = 0

v = np.linspace(0, 3, 500)
dNvdv = v**2 * np.exp(-v**2)
T = 1
fv_1 = v**2 * np.exp(-v**2 / T) / T**1.5

plt.figure(figsize=(10, 6))

plt.box(False)
plt.axhline(0, c='k', lw=1.5)
plt.axvline(0, c='k', lw=1.5)
plt.plot(v, fv_1)

plt.axvline(v[np.argmax(fv_1)], c='gray', ls='--', lw=0.8)
plt.text(0.92*v[np.argmax(fv_1)], 0.7*max(fv_1), r'$v_p$', fontsize=16, rotation=90)

plt.axvline(1.13*v[np.argmax(fv_1)], c='gray', ls='--', lw=0.8)
plt.text(0.93*1.13*v[np.argmax(fv_1)], 0.7*max(fv_1), r'$v_\text{avg}$', fontsize=16, rotation=90)

plt.axvline(1.22*v[np.argmax(fv_1)], c='gray', ls='--', lw=0.8)
plt.text(0.95*1.22*v[np.argmax(fv_1)], 0.7*max(fv_1), r'$v_\text{rms}$', fontsize=16, rotation=90)

plt.xlim(min(v), max(v))
plt.ylim(min(fv_1), 1.2*max(fv_1))
plt.xticks([0, max(v)], [r'$0$', r'$v$'], fontsize=16)
plt.yticks([1.2*max(fv_1)], [r'$f_v$'], fontsize=16)
plt.show()