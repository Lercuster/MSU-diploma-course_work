import numpy as np
import cycle_functions as cyc

num_experiments = 10
strain_calibration = 1
stress_calibration = 1

# todo: kinda user interface
# todo: normalaizing data


while True:
    freq = input("\nfrequency to process: " + str())
    if freq == "q":
        break
    else:
        for i in range(1, 11):
            file_name_expand = freq + '_' + str(i)
            data = cyc.read_file_raw(file_name_expand)
            time = data[:, 0:1]
            temp = data[:, 1:2]
            strain = data[:, 2:3] * strain_calibration
            stress = data[:, 3:4] * stress_calibration

