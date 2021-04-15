import numpy as np
import cycle_functions as cyc
import matplotlib.pyplot as plt


omega = [31.186024785508227, 46.870740267820636,	62.55551858198611, 78.18563318397912,
            93.93927520911129, 109.63134201823308, 125.2268991010366]

path = 'D:/qoursuch 3.0/experiments/rubber with temp control (2_)/results/summary/'
data_rubber = cyc.mean_summary_value(path, [1])

path = 'D:/qoursuch 3.0/experiments/rubber cord 90 deg with temp control (2_)/results/summary/'
data_cord_90 = cyc.mean_summary_value(path, [1])

path = 'D:/qoursuch 3.0/experiments/rubber cord 60 deg with temp control (2_)/results/summary/'
data_cord_60 = cyc.mean_summary_value(path, [1])

path = 'D:/qoursuch 3.0/experiments/rubber cord 45 deg with temp control (2_)/results/summary/'
data_cord_45 = cyc.mean_summary_value(path, [1])

data_rubber_cord_90 = cyc.from_rubber_to_cord_formula(np.pi/2, data_rubber, gamma=0.88)
data_rubber_cord_60 = cyc.from_rubber_to_cord_formula(np.pi/3, data_rubber, gamma=0.88)
data_rubber_cord_45 = cyc.from_rubber_to_cord_formula(np.pi/4, data_rubber, gamma=0.88)

err_90 = cyc.error_calc_average(data_cord_90, data_rubber_cord_90, omega[:5])
err_60 = cyc.error_calc_average(data_cord_60, data_rubber_cord_60, omega)
err_45 = cyc.error_calc_average(data_cord_45, data_rubber_cord_45, omega)

f = open(cyc.STORAGE_PATH + 'error 4%.txt', 'a')
f.write('\t'.join(map(str,[err_90, err_60, err_45])))
f.close()

print('\t'.join(map(str,[err_90, err_60, err_45])))

plt.plot(omega, data_rubber,  linewidth=1.5, marker='o', label='Rubber', color='black')
plt.plot(omega[:5], data_cord_90[:5],  linewidth=1.5, marker='v', label=str(int(np.round(np.pi/2 * 180 / np.pi, 0))) + ' deg experiment', color='black')
plt.plot(omega[:5], data_rubber_cord_90[:5],  linewidth=1.5, marker='s', label=str(int(np.round(np.pi/2 * 180 / np.pi, 0))) + ' deg approximation', color='black')
#plt.plot(omega, data_cord_60,  linewidth=1.5, marker='o', label=str(int(np.round(np.pi/3 * 180 / np.pi, 0))) + ' град эксперимент', color='black')
#plt.plot(omega, data_rubber_cord_60,  linewidth=1.5, marker='o', label=str(int(np.round(np.pi/3 * 180 / np.pi, 0))) + ' град аппрокс.', color='black')
#plt.plot(omega, data_cord_45,  linewidth=1.5, marker='v', label=str(int(np.round(np.pi/4 * 180 / np.pi, 0))) + ' deg experiment', color='black')
#plt.plot(omega, data_rubber_cord_45,  linewidth=1.5, marker='s', label=str(int(np.round(np.pi/4 * 180 / np.pi, 0))) + ' deg approximation', color='black')
plt.xlabel('Frequency (rad/s)', fontsize=14)
plt.ylabel('Mechanical work (MPa*Strain)', fontsize=14)
#plt.title(, fontsize=16)
plt.legend(fontsize=10)
#plt.savefig(cyc.STORAGE_PATH + 'Mech work vs freq angle comp 4% ' + '.png')
plt.show()
plt.clf()
