import numpy as np
import cycle_functions as cyc
import matplotlib.pyplot as plt

pathh = 'D:/qoursuch 3.0/experiments/rubber cord 45 deg with temp control (2%)/maxwell/dotted/'
time = np.linspace(0, 0.3, 1001)
error = []

params_2exp = [0.000526,
 0.02866,
 11.91735**2,
 4.06837**2]

params_3exp = [0.0004594,
 0.02863,
 0.000454,
 9.1137**2,
 4.06916**2,
 8.97488**2]

params_3exp_Ti_from_rubber = [0.00458,
 0.00458,
 0.03953,
 3.46322**2,
 3.46322**2,
 3.90908**2]

params_2exp_Ti_from_rubber = [0.00458,
 0.03953,
 4.89774**2,
 3.90908**2]


relax_3_exp_Ti_from_rubber = cyc.get_relaxation_f(time, params_3exp_Ti_from_rubber,
                                                  elnum=len(params_3exp_Ti_from_rubber) // 2)
relax_3_exp = cyc.get_relaxation_f(time, params_3exp, elnum=len(params_3exp) // 2)
relax_2_exp = cyc.get_relaxation_f(time, params_2exp, elnum=len(params_2exp) // 2)
relax_2_exp_Ti_from_rubber = cyc.get_relaxation_f(time, params_2exp_Ti_from_rubber,
                                                  elnum=len(params_2exp_Ti_from_rubber) // 2)



n = 5
k = 5
l = 10
j = 10

step_1 = 20
step_2 = 30
step_3 = 25

#plt.plot(time[n::step_3], relax_3_exp_Ti_from_rubber[n::step_3], linewidth=0,
 #       label='N = 3, t_n для резины', marker='o', color='black')
plt.plot(time[k::step_1], relax_3_exp[k::step_1], linewidth=0, marker='X', label='N = 3', color='black')
plt.plot(time[l::step_2], relax_2_exp[l::step_2], linewidth=0, marker='d', label='N = 2', color='black')
#plt.plot(time[j::step_1], relax_2_exp_Ti_from_rubber[j::step_1], linewidth=0, marker='v',
 #      label='Аппроксимация 2 эксп, время из резины', color='black')

plt.xlabel('Время (сек)', fontsize=14)
plt.ylabel('Функция релаксации', fontsize=14)
plt.legend(fontsize=10)
plt.show()
# plt.savefig(pathh + 'relaxations_dotted start segment.png')
plt.clf()
