import numpy as np
import cycle_functions as cyc

NUM_EXPERIMENTS = 10
STRAIN_CALIBRATION = 1
STRESS_CALIBRATION = 1


while True:
    summary_data = np.array([[]])
    freq = input("\nfrequency to process: " + str())
    if freq == "q":
        break
    else:
        for i in range(1, 7):
            file_name_expand = freq + '_' + str(i)
            data = cyc.read_file_raw(file_name_expand)
            time = data[:, 0:1]
            temp = data[:, 1:2]
            strain = data[:, 2:3] * STRAIN_CALIBRATION
            stress = data[:, 3:4] * STRESS_CALIBRATION
            processed_data, series_summary = cyc.experiment_processing(time, strain, stress, temp)
            summary_data = np.append(summary_data, series_summary)
            cyc.build_series_graph(file_name_expand, freq, time, stress, strain, strain_in_percent=True)
            cyc.write_results(processed_data, freq, i)
        summary_data = summary_data.reshape(6, 4)
        cyc.write_results(summary_data, freq, '0', True)
cyc.summary_graph_constructor()
