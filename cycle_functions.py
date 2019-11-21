import numpy as np
import matplotlib.pyplot as plt

# todo: read raw asci file, obtian columns as variables
# todo: find period function
# todo: cycle integration function
# todo: find peak value function
# todo: find amplitude function
# todo: graph builder function
# todo: exp processing function

source_path = "C:/Users/User/qoursuch 3.0/experiment raw data/"
storage_path = 'C:/Users/User/qoursuch 3.0/processed data/'


def read_file_raw(file_name: str):
    # todo: add description
    try:
        data = np.loadtxt(source_path + file_name + ".asc", delimiter="\t", dtype=np.float)
        return data
    except OSError:
        print('sorry no such file')
        return -1


def find_cycle(strain, cycle_beginning=0):
    # todo: add description
    i = 0
    while strain[cycle_beginning + i] >= strain[cycle_beginning + i + 1]:
        i += 1
        if cycle_beginning + i >= len(strain) - 5:
            return -1, -1
    while strain[cycle_beginning + i] <= strain[cycle_beginning + i + 1]:
        i += 1
        if cycle_beginning + i >= len(strain) - 5:
            return -1, -1
    cycle_ending = cycle_beginning + i
    return cycle_beginning, cycle_ending


def get_amplitude(strain, stress, cycle_beginning, cycle_ending):
    """
    todo: add description
    :param strain:
    :param stress:
    :param cycle_beginning:
    :param cycle_ending:
    :return:
    """
    max_strain = np.max(strain[cycle_beginning:cycle_ending, 0])
    max_stress = np.max(stress[cycle_beginning:cycle_ending, 0])
    min_strain = np.min(strain[cycle_beginning:cycle_ending, 0])
    min_stress = np.min(stress[cycle_beginning:cycle_ending, 0])
    strain_ampl = max_strain - min_strain
    stress_ampl = max_stress - min_stress
    return strain_ampl, stress_ampl


def get_period_frequency(time, cycle_beginning, cycle_ending):
    """
    todo: add description
    :param time:
    :param cycle_beginning:
    :param cycle_ending:
    :return:
    """
    period = time[cycle_ending, 0] - time[cycle_beginning, 0]
    frequency = 1 / period
    return period, frequency


def get_mechanical_work(strain, stress, cycle_beginning, cycle_ending):
    """
    todo: add description
    :param strain:
    :param stress:
    :return:
    """
    A = np.trapz(stress[cycle_beginning:cycle_ending, 0], strain[cycle_beginning:cycle_ending, 0])
    A = float('{:.5f}'.format(A))
    return A


def experiment_processing(time, strain, stress, temp):
    """

    :param time:
    :param strain:
    :param stress:
    :return:

    Main function where all magic occur.
    Function for processing 1 experiment chunk.
    """
    num_cycles = 0
    string_to_write = []
    cycle_begin, cycle_end = find_cycle(strain)
    result_header = '\t\t'.join(["cycle num", "time start", 'time stop',
                                 'max stress', 'strain ampl', 'stress ampl', 'period', "freq",
                                 'temp', 'Work'])
    while True:
        cycle_begin, cycle_end = find_cycle(strain, cycle_end)
        if cycle_end == -1:
            break
        num_cycles += 1
        peak_stress = np.max(stress[cycle_begin:cycle_end, 0])
        strain_ampl, stress_ampl = get_amplitude(strain, stress, cycle_begin, cycle_end)
        period, freq = get_period_frequency(time, cycle_begin, cycle_end)
        A = get_mechanical_work(strain, stress, cycle_begin, cycle_end)
        string_to_write = []
        string_to_write.extend(np.around([num_cycles, time[cycle_begin, 0], time[cycle_end, 0], peak_stress,
                                          strain_ampl, stress_ampl, period, freq, temp[cycle_begin, 0]], 3))
        string_to_write.append(A)
        print(result_header)
        print('\t\t'.join(map(str, string_to_write)), '\n')


if __name__ == "__main__":
    data = np.loadtxt(source_path + '20_1_1.txt')
    time = data[:, 0:1]
    temp = data[:, 1:2]
    strain = data[:, 2:3]  # * strain_calibration
    stress = data[:, 3:4]  # * stress_calibration
    experiment_processing(time, strain, stress, temp)
