import numpy as np
import cycle_functions as cyc
import matplotlib.pyplot as plt

path_strain = 'C:/Users/maksi/OneDrive/Рабочий стол/ANSYS/results/strain_time.txt'
path_stress = 'C:/Users/maksi/OneDrive/Рабочий стол/ANSYS/results/stress_time.txt'
path_results = 'C:/Users/maksi/OneDrive/Рабочий стол/ANSYS/results/time_strain_stress.txt'
path_results_results = 'C:/Users/maksi/OneDrive/Рабочий стол/ANSYS/results/results.txt'
path_exp = 'D:/qoursuch 3.0/experiments/rubber with temp control (2_)/raw/10_5.ASC'
data_strain = np.loadtxt(path_strain, skiprows=6, delimiter='\t', dtype='str')


def read_stupid_ansys_output(path):
    data = np.loadtxt(path, skiprows=6, delimiter='\t', dtype='str')
    correct_data = []
    for i in range(0, len(data)):
        row = data[i].split()
        if 'E' in row[1]:
            multiplier = int(row[0][-2:])
        else:
            multiplier = 0
        t = round(float(row[0][0:7]) * 10 ** (-multiplier), 7)
        if 'E' in row[1]:
            multiplier = int(row[1][-2:])
        else:
            multiplier = 0
        ux = round(float(row[1][0:7]) * 10 ** (-multiplier), 7)
        correct_data.append([t, ux])
    return np.array(correct_data)


data_strain = read_stupid_ansys_output(path_strain)
data_stress = read_stupid_ansys_output(path_stress)

f = open(path_results, 'w')
for i in range(0, len(data_strain)):
    f.write('\t'.join(map(str, np.append(data_strain[i], data_stress[i, 1]))))
    f.write('\n')
f.close()

data = np.loadtxt(path_results, dtype='float')
time = data[:, 0].reshape(len(data), 1)
strain = data[:, 1].reshape(len(data), 1)
stress = data[:, 2].reshape(len(data), 1)
temp = data[:, 2].reshape(len(data), 1)
processed_data, series_summary = cyc.experiment_processing(time, strain, stress, temp)

f = open(path_results_results, 'w')
for string_to_write in processed_data:
    f.write('\t\t'.join(map(str, string_to_write)))
    f.write('\n')
f.close()

exp = np.loadtxt(path_exp, dtype='float')

STRAIN_CALIBRATION = 1 / 237.2
STRESS_CALIBRATION = 9.8 / (2 * 80) # KG -> MPa

time = exp[:, 0:1]
temp = exp[:, 1:2]
strain_exp = exp[:, 2:3] * STRAIN_CALIBRATION - 0.0255
stress_exp = exp[:, 3:4] * STRESS_CALIBRATION

plt.plot(strain, stress + 2, label='ansys')
plt.plot(strain_exp, stress_exp, label='exp')
plt.legend()
plt.show()
plt.clf()