import numpy as np
import cycle_functions as cyc
import matplotlib.pyplot as plt

pathh = 'C:/Users/user/qoursuch 3.0/experiments/rubber cord 45 deg with temp control (4%)/maxwell/'
relax = []
time = np.linspace(0, 1, 1001)



params1 = [0.0409,
           0.00445,
           0.00445,
           4.70729**2,
           4.24272**2,
           4.24272**2]

params2 = [0.00697,
           0.00697,
           0.06936,
           4.04266**2,
           4.04194**2,
           4.79624**2]

params3 = [0.00697,
           0.06936,
           5.71668**2,
           4.79624**2]

params4 = [0.00697,
           0.06936,
           5.71668**2,
           4.79624**2]


relax_3_fixed_t = cyc.get_relaxation_f(time, params1, 3)
relax_3_exp = cyc.get_relaxation_f(time, params2, 3)
relax_2_exp = cyc.get_relaxation_f(time, params3, 2)
#relax_2_exp_fixed_t = cyc.get_relaxation_f(time, params4, 2)



plt.plot(time, relax_3_fixed_t, linewidth=1, label='3 exp fixed t', marker='')
plt.plot(time, relax_3_exp, linewidth=1, marker='', label='3 exp')
plt.plot(time, relax_2_exp, linewidth=1, marker='', label='2 exp')
#plt.plot(time[5:], relax_2_exp_fixed_t[5:], linewidth=1, marker='', label='2 exp fixed t')

plt.xlabel('time, s', fontsize=14)
plt.ylabel('Relaxation Function', fontsize=14)
plt.legend(fontsize=14)
#plt.show()
plt.savefig(pathh + 'relaxations.png')