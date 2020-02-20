import numpy as np
import matplotlib.pyplot as plt
import cycle_functions as cyc
import os


params1 = [0.00045,
           0.40628,
           0.01603,
           14.69572**2,
           9.3594**2,
           3.98351**2]

plt.plot(time[2:], relax_3_fixed_t[2:], linewidth=1, label='3 exp fixed t', marker='')
plt.plot(time[2:], relax_3_exp[2:], linewidth=1, marker='', label='3 exp')
plt.plot(time[2:], relax_2_exp[2:], linewidth=1, marker='', label='2 exp')