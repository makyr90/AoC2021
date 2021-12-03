from common import get_input_of_day
import numpy as np

def get_most_frequent_bit(array,index):
    return 1 if np.sum(array[:,index]) >= array.shape[0]/2 else 0

def get_least_frequent_bit(array,index):
    return 1 if np.sum(array[:,index]) < array.shape[0]/2 else 0

def solve_part1(input_list):

    report_data = []
    for row in input_list:
        bits = np.asarray([x for x in str(row.strip())])
        report_data.append([int(x) for x in bits])
    report_data = np.stack(report_data, axis=0)
    most_frequent_bits = [str(get_most_frequent_bit(report_data,x)) for x in range(report_data.shape[1])]
    least_frequent_bits = [str(get_least_frequent_bit(report_data,x)) for x in range(report_data.shape[1])]
    gamma = int("".join(most_frequent_bits),2)
    epsilon = int("".join(least_frequent_bits),2)

    return gamma*epsilon

def solve_part2(input_list):

    report_data = []
    for row in input_list:
        bits = np.asarray([x for x in str(row.strip())])
        report_data.append([int(x) for x in bits])

    report_data = np.stack(report_data, axis=0)
    ogr_data = np.copy(report_data)
    for idx in range(report_data.shape[1]):
        if ogr_data.shape[0] == 1:
            break
        most_frequent_bit = get_most_frequent_bit(ogr_data,idx)
        ogr_data = ogr_data[ogr_data[:,idx] == most_frequent_bit]

    assert ogr_data.shape[0] == 1, "Error during ogr value calculation"
    ogr_value = int("".join([str(x) for x in ogr_data[0]]),2)

    co2_data = np.copy(report_data)
    for idx in range(report_data.shape[1]):
        if co2_data.shape[0] == 1:
            break
        least_frequent_bit = get_least_frequent_bit(co2_data,idx)
        co2_data = co2_data[co2_data[:,idx] == least_frequent_bit]

    assert co2_data.shape[0] == 1, "Error during co2 value calculation"
    co2_value = int("".join([str(x) for x in co2_data[0]]),2)

    return ogr_value*co2_value


if __name__ == '__main__':

    print("Day 3 part 1 answer: {}".format(solve_part1(get_input_of_day(3))))
    print("Day 3 part 2 answer: {}".format(solve_part2(get_input_of_day(3))))
