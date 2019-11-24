import numpy as np
import matplotlib.pyplot as plt


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


def get_amplitude(column, beginning, ending):
    """
    This function calculates and returns amplitude value (max value - min value)
     of a given column on a given index interval, from beginning to ending.

    :param column: np.array - given array
    :param beginning: int - index of the interval beginning
    :param ending: int - index of the interval ending
    :return: float - calculated amplitude value
    """
    max_column = np.max(column[beginning:ending, 0])
    min_column = np.min(column[beginning:ending, 0])
    column_ampl = max_column - min_column
    return column_ampl


def get_mechanical_work(strain, stress, beginning, ending):
    """
    This function calculates a mechanical work for one cycle of loading
    using np.trapz function. The scope od a cycle is determined by its beginning and ending
    with beginning and ending arguments.

    :param strain: np.array with shape (n, 1)
    :param stress: np.array with shape (n, 1)
    :param beginning: int - index of cycle beginning
    :param ending: int - index of cycle ending
    :return: float - result of calculating mechanical work
    """
    mechanical_work = np.trapz(stress[beginning:ending, 0], strain[beginning:ending, 0])
    mechanical_work = float('{:.5f}'.format(mechanical_work))
    return mechanical_work


def build_graph(file_name, freq, time=None, stress=None, strain=None, strain_in_percent=False):
    """
    This function just builds graphs of stress~~strain, stress~~time and strain~~time.
    All plots are saved in storage directory with other results.
    All data arrays may be missing if so the building of the corresponding plot is skipped.

    :param file_name: str
    :param time: array like
    :param stress: array like
    :param strain: array like
    :param strain_in_percent: bool - indicates is strain will be represented in percents ot not
    """
    if strain_in_percent:
        multiplier = 100
    else:
        multiplier = 1
    if stress is not None and strain is not None:
        plt.plot(strain*multiplier, stress, linewidth = 1)
        plt.title('Зависимость напряжения от деформации.', fontsize = 16)
        plt.xlabel('Деформация, %', fontsize = 14)
        plt.ylabel('Напряжение, МПа', fontsize = 14)
        plt.savefig(storage_path + freq + '/'+ file_name + '_sigma_eps.png')
        plt.clf()
    if strain is not None:
        plt.plot(time, strain*multiplier, '.')
        plt.title('Зависимость деформации от времени.', fontsize = 16)
        plt.xlabel('Время, с', fontsize = 14)
        plt.ylabel('Деформация, %', fontsize = 14)
        plt.savefig(storage_path + freq + '/' + file_name + '_time_eps.png')
        plt.clf()
    if stress is not None:
        plt.plot(time, stress, '.')
        plt.title('Зависимость напряжения от времени.', fontsize = 16)
        plt.xlabel('Время, с', fontsize = 14)
        plt.ylabel('Напряжение, МПа', fontsize = 14)
        plt.savefig(storage_path + freq + '/' + file_name + '_time_sigma.png')
        plt.clf()


def write_results(data_to_write, freq, series_number):
    f = open(storage_path + freq + '/' + freq + '_' + str(series_number) + '_results.txt', 'a')
    for stirng_to_write in data_to_write:
        f.write(stirng_to_write)
        f.write('\n')
    f.close()


def experiment_processing(time, strain, stress, temp):
    """

    :param time:
    :param strain:
    :param stress:
    :param temp:
    :return:

    Main function where all magic occur.
    Function for processing 1 experiment chunk.
    """
    num_cycles = 0
    data_to_write = []
    mech_work_average = frequency_average = period_average = peak_stress_average = 0
    cycle_begin, cycle_end = find_cycle(strain)
    result_header = '\t\t'.join(["#", "start", 'stop',
                                 'peak', 'SnAmpl', 'StAmpl', 'period', "freq",
                                 'temp', 'Work', '\n'])
    data_to_write.append(result_header)
    while True:
        cycle_begin, cycle_end = find_cycle(strain, cycle_end)
        if cycle_end == -1:
            break

        num_cycles += 1
        peak_stress = np.max(stress[cycle_begin:cycle_end, 0])
        strain_ampl = get_amplitude(strain, cycle_begin, cycle_end)
        stress_ampl = get_amplitude(stress, cycle_begin, cycle_end)
        period = time[cycle_end, 0] - time[cycle_begin, 0]
        frequency = 1 / period
        mech_work = get_mechanical_work(strain, stress, cycle_begin, cycle_end)

        string_to_write = []
        string_to_write.extend(np.around([num_cycles, time[cycle_begin, 0], time[cycle_end, 0], peak_stress,
                                          strain_ampl, stress_ampl, period, frequency, temp[cycle_begin, 0]], 3))
        mech_work_average += mech_work
        frequency_average += frequency
        period_average += period
        peak_stress_average += peak_stress_average

        string_to_write.append(mech_work)
        print(result_header)
        print('\t\t'.join(map(str, string_to_write)), '\n')
        data_to_write.append('\t\t'.join(map(str, string_to_write)))

    mech_work_average /= num_cycles
    frequency_average /= num_cycles
    period_average /= num_cycles
    peak_stress_average /= num_cycles

    data_to_write.append('\n\n' + '\t\t'.join(["mech w", 'freq', 'period']))
    data_to_write.append('\t\t'.join(map(str, np.around([mech_work_average,frequency_average, period_average], 5))))
    return data_to_write


if __name__ == "__main__":
    data = np.loadtxt(source_path + '20_1_1.txt')
    time = data[:, 0:1]
    temp = data[:, 1:2]
    strain = data[:, 2:3]  # * strain_calibration
    stress = data[:, 3:4]  # * stress_calibration
    data_to_write = experiment_processing(time, strain, stress, temp, '20_1', 1)
    build_graph("20_1_1", time, stress, strain)
    write_results(data_to_write, freq='20', series_number=1)