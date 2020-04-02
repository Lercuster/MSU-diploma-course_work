import numpy as np
import cycle_functions as cyc
import matplotlib.pyplot as plt

pathh = 'C:/Users/user/qoursuch 3.0/experiments/rubber cord 90 deg with temp control (2%)/maxwell/'
pathh1 = 'D:/qoursuch 3.0/experiments/relax func comp/4% deform/dotted/'
time = np.linspace(0, 1, 1001)

params_90 = [0.00501,
             0.04285,
             5.23384 ** 2,
             4.29917 ** 2]

params_60 = [0.00512,
             0.03889,
             0.00512,
             3.36485 ** 2,
             3.83413 ** 2,
             3.58973 ** 2]

params_45 = [0.00697,
             0.00697,
             0.06936,
             4.04266 ** 2,
             4.04194 ** 2,
             4.79624 ** 2]

relax_90 = cyc.get_relaxation_f(time, params_90, elnum=2)
relax_60_exp = cyc.get_relaxation_f(time, params_60)
relax_60_app = cyc.from_rubber_to_cord_formula(np.pi / 3, relax_90)
relax_45_exp = cyc.get_relaxation_f(time, params_45, elnum=3)
relax_45_app = cyc.from_rubber_to_cord_formula(np.pi / 4, relax_90)

n = 2
k = 2
l = 2
j = 11

step = 12
plt.plot(time[n::step], relax_90[n::step], linewidth=0.3, marker='.', label='rubber cord 90 deg')
plt.plot(time[k::step], relax_45_exp[k::step], linewidth=0.3, marker='.', label='rubber cord 45 deg experiment')
plt.plot(time[l::step], relax_45_app[l::step], linewidth=0.3, marker='.', label='rubber cord 45 deg approximation')
# plt.plot(time[5:], relax_2_exp_fixed_t[5:], linewidth=1, marker='', label='2 exp fixed t')

plt.xlabel('time, s', fontsize=14)
plt.ylabel('Relaxation Function', fontsize=14)
plt.legend(fontsize=12)
#plt.show()
plt.savefig(pathh1 + 'relaxations_90_2exp_45_3exp_dotted.png')
