import numpy as np
import cycle_functions as cyc
import matplotlib.pyplot as plt

omega = np.linspace(30, 150, num=1000)

exp_data = [31.18621328106745,	0.00411,
46.87702345312781,	0.00431,
62.55243982118559,	0.00447,
78.1825544231786,	0.00459,
93.91514777753171,	0.00471,
109.61714201943886,	0.00489,
125.24172741836153,	0.00526]

omega_exp = exp_data[0::2]
work_exp = exp_data[1::2]

print(omega_exp)

params_3 = [0.0004594,
 0.02863,
 0.000454,
 9.1137**2,
 4.06916**2,
 8.97488**2]

params_2 = [0.000526,
 0.02866,
 11.91735**2,
 4.06837**2]

params_2_t = [0.00458,
 0.03953,
 4.89774**2,
 3.90908**2]


params_3_t = [0.00458,
 0.00458,
 0.03953,
 3.46322**2,
 3.46322**2,
 3.90908**2]


work_2 = cyc.work_vs_freq_function(omega, params_2, e_ampl=0.011, el_num=len(params_2) // 2)
work_3 = cyc.work_vs_freq_function(omega, params_3, e_ampl=0.011, el_num=len(params_3) // 2)
work_3_t = cyc.work_vs_freq_function(omega, params_3_t, e_ampl=0.011, el_num=len(params_3_t) // 2)
work_2_t = cyc.work_vs_freq_function(omega, params_2_t, e_ampl=0.011, el_num=len(params_2_t) // 2)

step_2 = 60
step_3 = 80

plt.plot(omega[100::step_2], work_2[100::step_2], marker='v', linewidth=0, label='2 эксп', color='black')
plt.plot(omega[100::step_3], work_3[100::step_3], marker='s', linewidth=0, label='3 эксп', color='black')
plt.plot(omega[::step_2], work_3_t[::step_2], marker='X', linewidth=0, label='3 эксп, t_n из резины', color='black')
plt.plot(omega[::step_3], work_2_t[::step_3], marker='d', linewidth=0, label='2 эксп, t_n из резины', color='black')
plt.plot(omega_exp, work_exp, marker='o', linewidth=1, label='Эксперимент', color='black')
plt.ylabel('Работа (МПа*Деформация)', fontsize=14)
plt.xlabel('Частота (рад/сек)', fontsize=14)
plt.legend()
plt.show()
# plt.savefig(cyc.STORAGE_PATH + 'work_vs_freq_relax_comp' + '.png')
plt.clf()
