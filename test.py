import numpy as np
import matplotlib.pyplot as plt
import cycle_functions as cyc
import os
'''
PATH = 'C:/Users/User/qoursuch 3.0/experiments/tarirovka/'
cyc.drop_commas(PATH)

names = os.listdir(PATH)

for name in names:
    if '.txt' in name:
        data = np.loadtxt(PATH + name)

        time = data[:, 0:1]
        stress = data[:, 3:4]

        plt.plot(time, stress)
        plt.xlabel('Sec', fontsize=14)
        plt.ylabel('Stress, mV/V', fontsize=14)
        plt.savefig(PATH + name[:-4] + '.png')
        plt.clf()
'''

print(np.linspace(0, 10, num=10, endpoint=False, dtype=np.int))