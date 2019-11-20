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




def experiment_processing(time, strain, stress):
    """

    :param time:
    :param strain:
    :param stress:
    :return:

    Main function where all magic occur.
    Function for processing 1 experiment chunk.
    """
    num_cycles = 0
    cycle_begin, cycle_end = find_cycle(strain)
    while True:
        cycle_begin, cycle_end = find_cycle(strain, cycle_end)
        if cycle_end == -1:
            break




if __name__ == "__main__":
    file_name_expand = source_path + "20_1_1.txt"
    data = np.loadtxt(file_name_expand, delimiter='\t', dtype=np.float)
    time = data[:, 0:1]
    temp = data[:, 1:2]
    strain = data[:, 2:3]
    print(strain.shape)
    stress = data[:, 3:4] #* stress_calibration
    cycle_beggining, cycle_ending = find_cycle(strain)
    print(time[cycle_beggining, 0], time[cycle_ending, 0])
    cycle_beggining, cycle_ending = find_cycle(strain, cycle_ending)
    print(time[cycle_beggining, 0], time[cycle_ending, 0])
    cycle_beggining, cycle_ending = find_cycle(strain, cycle_ending)
    print(time[cycle_beggining, 0], time[cycle_ending, 0])