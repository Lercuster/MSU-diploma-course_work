import numpy as np
import cycle_functions as cyc

num_experiments = 10
strain_calibration = 1
stress_calibration = 1

# todo: kinda user interface
# todo: normalaizing data


while True:
    summary_data = ['\t\t'.join(['peak', 'meck_work', 'temp', 'freq'])]
    freq = input("\nfrequency to process: " + str())
    if freq == "q":
        break
    else:
        for i in range(1, 7):
            file_name_expand = freq + '_' + str(i)
            data = cyc.read_file_raw(file_name_expand)
            time = data[:, 0:1]
            temp = data[:, 1:2]
            strain = data[:, 2:3] * strain_calibration
            stress = data[:, 3:4] * stress_calibration
            processed_data, series_summary = cyc.experiment_processing(time, strain, stress, temp)
            summary_data.append(series_summary)
            cyc.build_graph(file_name_expand, freq, time, stress, strain, strain_in_percent=True)
            cyc.write_results(processed_data, freq, i)
        cyc.write_results(summary_data, freq, '0', True)