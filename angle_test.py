import numpy as np
import cycle_functions as cyc
import matplotlib.pyplot as plt

path = 'C:/Users/user/qoursuch 3.0/experiments/rubber with temp control (4%)/results/summary/'
data_rubber = cyc.mean_summary_value(path, [1])

path = 'C:/Users/user/qoursuch 3.0/experiments/rubber cord 60 deg with temp control (4%)/results/summary/'
data_cord_1 = cyc.mean_summary_value(path, [1])

path = 'C:/Users/user/qoursuch 3.0/experiments/rubber cord 45 deg with temp control (4%)/results/summary/'
data_cord_2 = cyc.mean_summary_value(path, [1])

data_rubber_cord_1 = cyc.from_rubber_to_cord_formula(np.pi/3, data_rubber)
data_rubber_cord_2 = cyc.from_rubber_to_cord_formula(np.pi/4, data_rubber)

f = open(cyc.STORAGE_PATH + 'error 4 %.txt', 'a')
f.write('60 deg\n')
error = cyc.error_calc(data_rubber_cord_1, data_cord_1)
f.write('\t'.join(map(str, error)))
f.write('\n45 deg\n')
error = cyc.error_calc(data_rubber_cord_2, data_cord_2)
f.write('\t'.join(map(str, error)))

plt.plot(data_rubber,  linewidth=1, marker='o', label='rubber')
plt.plot(data_cord_1,  linewidth=1, marker='o', label=str(int(np.round(np.pi/3 * 180 / np.pi, 0))) + ' cord exp')
plt.plot(data_rubber_cord_1,  linewidth=1, marker='o', label=str(int(np.round(np.pi/3 * 180 / np.pi, 0))) + ' cord calc')
plt.plot(data_cord_2,  linewidth=1, marker='o', label=str(int(np.round(np.pi/4 * 180 / np.pi, 0))) + ' cord exp')
plt.plot(data_rubber_cord_2,  linewidth=1, marker='o', label=str(int(np.round(np.pi/4 * 180 / np.pi, 0))) + ' cord calc')
plt.xlabel('Frequency, Hz', fontsize=14)
plt.ylabel('Mechanical Work', fontsize=14)
plt.title('Plot for Mechanical Work versus Frequency.', fontsize=16)
plt.legend(fontsize=10)
plt.savefig(cyc.STORAGE_PATH + 'Mech work vs freq angle comp 4% ' + '.png')
plt.clf()
