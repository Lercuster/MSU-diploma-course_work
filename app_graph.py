import numpy as np
import cycle_functions as cyc
import matplotlib.pyplot as plt

pathh = 'C:/Users/user/qoursuch 3.0/experiments/rubber with temp control (2%)/maxwell/'
relax = []
time = np.linspace(0, 2, 201)
params1 = [0.00458,
          0.03953,
          0.00458,
          3.00462**2,
          3.62377**2,
          3.72303**2]

params2 = [0.00458,
          0.03953,
          0.00458,
          3.00462**2,
          3.62377**2,
          3.72303**2]




exp_data = np.loadtxt(pathh + 'work_freq_table.txt', delimiter='\t', dtype=np.float, skiprows=0)

#plt.plot(exp_data[:, 0], exp_data[:, 1], linewidth=5)

#plt.scatter(app_data[:, 0], app_data[:, 1], color='red', marker='.')
plt.show()