import numpy as np
import cycle_functions as cyc
import matplotlib.pyplot as plt

pathh = 'C:/Users/user/qoursuch 3.0/experiments/rubber cord 90 deg with temp control (2%)/maxwell/'
pathh1 = 'D:/qoursuch 3.0/experiments/relax func comp/4% deform/dotted/'
time = np.linspace(0, 0.3, 501)

params_rub = [0.00458,
 0.03953,
 0.00458,
 3.00462**2,
 3.6237**2,
 3.72303**2]

params_90 = [0.00501,
 0.04285,
 5.23384**2,
 4.29917**2]


params_60 = [0.0004594,
 0.02863,
 0.000454,
 9.1137**2,
 4.06916**2,
 8.97488**2]

params_45 = [0.03754,
 0.00422,
 4.74844**2,
 6.14996**2]

relax_rub = cyc.get_relaxation_f(time, params_rub, elnum=len(params_rub)//2)
relax_90_exp = cyc.get_relaxation_f(time, params_90, elnum=len(params_90)//2)
relax_90_app = cyc.from_rubber_to_cord_formula(np.pi/2, relax_rub)
relax_60_exp = cyc.get_relaxation_f(time, params_60, elnum=len(params_60)//2)
relax_60_app = cyc.from_rubber_to_cord_formula(np.pi / 3, relax_rub)
relax_45_exp = cyc.get_relaxation_f(time, params_45, elnum=len(params_45)//2)
relax_45_app = cyc.from_rubber_to_cord_formula(np.pi / 4, relax_rub)


n = 9
k = 9
l = 10
j = 10

step = 20
plt.plot(time[n::step], relax_rub[n::step], linewidth=1.5, marker='o', label='Rubber', color='black')
plt.plot(time[k::step], relax_45_exp[k::step], linewidth=1.5, marker='s', label='Rubber cord 45 deg, experiment', color='black')
plt.plot(time[l::step], relax_45_app[l::step], linewidth=1.5, marker='v', label='Rubber cord 45 deg, approximation', color='black')

plt.xlabel('time (s)', fontsize=14)
plt.ylabel('Relaxation function', fontsize=14)
plt.legend(fontsize=12)
plt.show()
#plt.savefig(pathh1 + 'relaxations_90_2exp_45_3exp dotted start segment.png')
plt.clf()