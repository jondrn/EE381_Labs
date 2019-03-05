# EE 381 Spring 2019 Project 1
# Jonathan Duran
# 014327168
# Start Date:  1/23/2019
# Finish Date: 2/6/2019
# Description: This program will output a summary of data for user inputted values

import matplotlib.pyplot as pareto


def mean(user_list, length):                # Finds the mean of the user inputted data
    list_sum = 0
    for value in user_list:
        list_sum = list_sum + value
    mean_value = list_sum / length
    return mean_value


def median(user_list, length):              # Finds the median value within the list of integers
    if (length % 2) == 0:
        median_value = (user_list[int(length / 2)] + user_list[(int(length / 2)) - 1]) / 2
    else:
        median_value = user_list[int(length / 2)]
    return median_value


def mode(user_list):                         # Finds the mode of the mode of the list
    count_dict = {}
    for i in user_list:
        count = user_list.count(i)
        if i not in count_dict.keys():
            count_dict[i] = count
    max_count = 0
    for key in count_dict:
        if count_dict[key] >= max_count:
            max_count = count_dict[key]
    corr_keys = []
    for corr_key, count_value in count_dict.items():
        if count_dict[corr_key] == max_count:
            corr_keys.append(corr_key)
    if max_count == 1 and len(count_dict) != 1:
        return 'There is no mode for this data set. All values occur only once.'
    else:
        corr_keys = sorted(corr_keys)
        return corr_keys, max_count


def range_function(user_list):              # Finds the range of the list
    range_value = max(user_list) - min(user_list)
    return range_value


def variance(user_list, mean_val, length):  # Finds the variance of the list
    temp_list = []
    variance_list = []
    for x in user_list:
        temp_list.append(x - mean_val)
    for x in temp_list:
        variance_list.append(x ** 2)
    variance_list_sum = sum(variance_list)
    variance_value = variance_list_sum / length
    return variance_value


def standard_deviation(var_val):           # Finds the Standard Deviation of the list
    std_deviation = var_val ** 0.5
    return std_deviation


def pareto_chart():
    x = []
    y = []
    debts = [['Rent', 0], ['Credit', 0], ['Transport', 0], ['Groceries', 0]]
    for i in debts:
        print("Category: ", i[0])
        i[1] = float(input("Amount of money owed: "))
    debts.sort(key=lambda v: v[1], reverse=True)
    for i in debts:
        x.append(i[0])
    for i in debts:
        y.append(i[1])
    pareto.bar(x, y, 1.0)
    pareto.show()


def main():
    num_list = []
    while True:
        try:
            input_value = int(input("Enter non-negative integers to be evaluated (Enter any letter to end input): "))
            num_list.append(input_value)
        except ValueError:
            break
    list_size = len(num_list)
    num_list = sorted(num_list)
    mean_value = mean(num_list, list_size)
    print("Your list: ", num_list)
    print("Mean: ", mean_value)
    median_value = median(num_list, list_size)
    print("Median: ", median_value)
    mode_value = mode(num_list)
    print("Mode(value, frequency): ", str(mode_value).strip('[]'))
    range_value = range_function(num_list)
    print("Range: ", range_value)
    variance_value = variance(num_list, mean_value, list_size)
    print("Variance: {0:.2f}".format(variance_value))
    std_dev = standard_deviation(variance_value)
    print("Standard Deviation: {0:.2f}".format(std_dev))
    pareto_chart()


main()


























