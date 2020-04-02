import numpy as np
import cycle_functions as cyc
import matplotlib.pyplot as plt

pathh = 'D:/qoursuch 3.0/experiments/rubber cord 90 deg with temp control (2%)/maxwell/dotted/'
relax = []
time = np.linspace(0, 1, 1001)

params_2exp = [0.000526,
               0.02866,
               11.91735 ** 2,
               4.06837 ** 2]

params_3exp = [0.0001959,
               0.0001959,
               0.03674,
               17.66417 ** 2,
               17.66474 ** 2,
               4.62921 ** 2]

params_3exp_Ti_from_rubber = [0.00458,
                              0.00458,
                              0.03953,
                              4.05721 ** 2,
                              4.05721 ** 2,
                              4.45203 ** 2]

params_2exp_Ti_from_rubber = [0.00458,
                              0.03953,
                              4.89774 ** 2,
                              3.90908 ** 2]

relax_3_exp_Ti_from_rubber = cyc.get_relaxation_f(time, params_3exp_Ti_from_rubber, 3)
relax_3_exp = cyc.get_relaxation_f(time, params_3exp, 3)
relax_2_exp = cyc.get_relaxation_f(time, params_2exp, 2)
relax_2_exp_Ti_from_rubber = cyc.get_relaxation_f(time, params_2exp_Ti_from_rubber, 2)

j = 10
n = 1
k = 10
l = 1

step = 20
plt.plot(time[n::step], relax_3_exp_Ti_from_rubber[n::step], linewidth=0.3,
         label='Approximation with 3 exp, t from rubber', marker='.')
plt.plot(time[k::step], relax_3_exp[k::step], linewidth=0.3, marker='.', label='Approximation with 3 exp')
# plt.plot(time[l::step], relax_2_exp[l::step], linewidth=0.3, marker='.', label='Approximation with 2 exp')
# plt.plot(time[j::step], relax_2_exp_Ti_from_rubber[j::step], linewidth=0.3, marker='.',
#         label='Approximation with 2 exp, t from rubber')

plt.xlabel('time, s', fontsize=14)
plt.ylabel('Relaxation Function', fontsize=14)
plt.legend(fontsize=12)
# plt.show()
plt.savefig(pathh + 'relaxations_dotted.png')
