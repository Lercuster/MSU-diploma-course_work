import numpy as np
import cycle_functions as cyc
import matplotlib.pyplot as plt


path = 'C:/Users/user/qoursuch 3.0/experiments/rubber cord 60 deg with temp control (4%)/results/summary/'
pathh = 'C:/Users/user/qoursuch 3.0/experiments/rubber cord 60 deg with temp control (4%)/maxwell/'
work = cyc.mean_summary_value(path, [1], 1)
freq = cyc.mean_summary_value(path, [1], 3) * 2 * np.pi

f = open(pathh + 'work_freq_table.txt', 'a')
for i in range(len(freq)):
    f.write('\t'.join(map(str, [freq[i], work[i]])))
    f.write('\n')