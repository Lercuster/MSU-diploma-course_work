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
    todo: add description
    :param column:
    :param stress:
    :param beginning:
    :param ending:
    :return:
    """
    max_column = np.max(column[beginning:ending, 0])
    min_column = np.min(column[beginning:ending, 0])
    column_ampl = max_column - min_column
    return column_ampl


def get_period_frequency(column, beginning, ending):
    """
    todo: add description
    :param column:
    :param beginning:
    :param ending:
    :return:
    """
    period = column[ending, 0] - column[beginning, 0]
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


def build_graph(file_name, time=None, stress=None, strain=None, strain_in_percent=False):
    """
    
    :param file_name:
    :param time:
    :param stress:
    :param strain:
    :param strain_in_percent:
    :return:
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
        plt.savefig(storage_path + file_name + '_sigma_eps.png')
        plt.clf()
    if strain is not None:
        plt.plot(time, strain*multiplier, '.')
        plt.title('Зависимость деформации от времени.', fontsize = 16)
        plt.xlabel('Время, с', fontsize = 14)
        plt.ylabel('Деформация, %', fontsize = 14)
        plt.savefig(storage_path + file_name + '_time_eps.png')
        plt.clf()
    if stress is not None:
        plt.plot(time, stress, '.')
        plt.title('Зависимость напряжения от времени.', fontsize = 16)
        plt.xlabel('Время, с', fontsize = 14)
        plt.ylabel('Напряжение, МПа', fontsize = 14)
        plt.savefig(storage_path + file_name + '_time_sigma.png')
        plt.clf()


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
    mech_work_average = frequency_average = period_average = 0
    cycle_begin, cycle_end = find_cycle(strain)
    result_header = '\t\t'.join(["num", "start", 'stop',
                                 'peak', 'SnAmpl', 'StAmpl', 'period', "freq",
                                 'temp', 'Work'])
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

        string_to_write.append(mech_work)
        print(result_header)
        print('\t\t'.join(map(str, string_to_write)), '\n')
    mech_work_average /= num_cycles
    frequency_average /= num_cycles
    period_average /= num_cycles
    print('\t\t'.join(["mech w", 'freq', 'period']))
    print('\t\t'.join(map(str, np.around([mech_work_average,frequency_average, period_average], 5))))


if __name__ == "__main__":
    data = np.loadtxt(source_path + '20_1_1.txt')
    time = data[:, 0:1]
    temp = data[:, 1:2]
    strain = data[:, 2:3]  # * strain_calibration
    stress = data[:, 3:4]  # * stress_calibration
    experiment_processing(time, strain, stress, temp)
    build_graph("20_1_1", time, stress, strain)