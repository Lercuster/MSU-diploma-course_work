import numpy as np
import cycle_functions as cyc
import matplotlib.pyplot as plt

pathh = 'C:/Users/user/qoursuch 3.0/experiments/rubber cord 45 deg with temp control (4%)/maxwell/'
time = np.linspace(0, 1, 1001)

params_90 = [0.0001959,
             0.0001959,
             0.03674,
             17.66417**2,
             17.66474**2,
             4.62921**2]

params_60 = [0.000459,
             0.02863,
             0.000454,
             9.1137**2,
             4.06916**2,
             8.97488**2]

relax_90 = cyc.get_relaxation_f(time, params_90)
relax_60_exp = cyc.get_relaxation_f(time, params_60)
relax_60_app = cyc.from_rubber_to_cord_formula(np.pi/3, relax_90)

n = 5

plt.plot(time[n:], relax_90[n:], linewidth=1, label='90 ', marker='')
plt.plot(time[n:], relax_60_exp[n:], linewidth=1, marker='', label='60 exp')
plt.plot(time[n:], relax_60_app[n:], linewidth=1, marker='', label='60 app')
#plt.plot(time[5:], relax_2_exp_fixed_t[5:], linewidth=1, marker='', label='2 exp fixed t')

plt.xlabel('time, s', fontsize=14)
plt.ylabel('Relaxation Function', fontsize=14)
plt.legend(fontsize=14)
plt.show()
#plt.savefig(pathh + 'relaxations.png')