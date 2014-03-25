__author__ = 'Nathan'
### Nathanial Benjamin, UCI, Calit2, CalPlug, 2014-Feb

### The MusicGlove interface: evaluates a csv file's data and converts that data into statistics telling how well the
###    user is preforming, then returns a string giving encouragement and advice.

"""
currently when incorrect input is done 'nan' is being interpreted as 300 50% more than the maximum late grip
    -how much should nan be worth, compared to a slow response?
"""

import Mglove_str_gen
from collections import namedtuple

Stat = namedtuple('Stat', 'expected actual difference')

def parse_csv(infile: "stat_list") -> [Stat]:
    '''Read data from a list of statistics, and return a namedtuple containing
       the actual and expected fingers, and the time difference from expected.
    '''
    print("entering parse_CSV")
    stat_list = []
    for temp_stat in infile:
        try:
            if type(temp_stat) is str:
                continue
            if temp_stat[2] == 'nan': #Keep it from throwing errors because 'nan' is not a float
                temp_stat[2] = -300 # A missed grip will count 25% more than the maximum late/early grip
            stat_list.append(Stat(int(temp_stat[0]), int(temp_stat[1]), float(temp_stat[2])))
        except IndexError:
            pass
    return stat_list

def difference_from_zero(time: float) -> float:
    '''calculates the difference from zero'''
    if time > 0:
        return time
    elif time < 0:
        return (0 - time)
    else:
        return 0

def average_grip_time(grip_stats: [Stat]) -> float:
    '''Sums the total time for a given grip, then returns average reaction time'''
    print("entering average_grip_time")
    if grip_stats == []:
        return 0
    time = 0
    for stat in grip_stats:
        time += difference_from_zero(stat.difference)
    if len(grip_stats) == 0:
        return 0
    average_grip_time = (time/len(grip_stats))
    return average_grip_time


def gather_info(stat_list: [Stat]) -> [int]:
    '''Use the stats to evaluate user performance, then determine what
       correction needs to be taken'''
    print("entering gather_info")
    error_list = []
    grip_1_list = []
    grip_2_list = []
    grip_3_list = []
    grip_4_list = []
    grip_5_list = []
    for stat in stat_list:
        if stat.expected != stat.actual:
            error_list.append(stat)
        if stat.expected == 1:
            grip_1_list.append(stat)
        elif stat.expected == 2:
            grip_2_list.append(stat)
        elif stat.expected == 3:
            grip_3_list.append(stat)
        elif stat.expected == 4:
            grip_4_list.append(stat)
        elif stat.expected == 5:
            grip_5_list.append(stat)

    grip_1_avg =  average_grip_time(grip_1_list)
    grip_2_avg = average_grip_time(grip_2_list)
    grip_3_avg = average_grip_time(grip_3_list)
    grip_4_avg = average_grip_time(grip_4_list)
    grip_5_avg = average_grip_time(grip_5_list)
    return [grip_1_avg, grip_2_avg, grip_3_avg, grip_4_avg, grip_5_avg]


def evaluate_info(grip_times: [int], last_worst_grip: int) -> int:
    '''Determines which grip needs the most focus'''
    print("entering evaluate info")
    current = 0
    worst_grip = 0
    i = 0
    for time in grip_times:
        i += 1
        if i == last_worst_grip:
            continue
        elif current < time:
            current = time
            worst_grip = i
    return worst_grip


def evaluate_best_grip(grip_times: [int]) -> int:
    '''Determines which grip needs the most focus'''
    print("entering evaluate_best_grip")
    current = 9001
    best_grip = 0
    i = 0
    for time in grip_times:
        i += 1
        if time == 0:
            continue
        if current > time:
            print(time)
            current = time
            best_grip = i
            print("best grip =", best_grip)
    return best_grip




if __name__ == '__main__':
    test_csv = [['1', '1', '-16.823999999999614'], ['4', '4', '-35.30199999999968'], ['3', '3', '-85.779999999999745'],
                ['3', '3', '5.2640000000001237'], ['3', '3', '18.786000000000058'], ['2', '2', '48.307999999999993'],
                ['2', '2', '13.829999999999927'], ['3', '3', '42.113000000001193'], ['2', '2', '39.39600000000064'],
                ['1', '1', '5.9179999999996653'], ['2', '2', '-44.559999999999491'], ['1', '1', '9.5280000000002474'],
                ['4', '4', '-8.9499999999989086'], ['3', '3', '-11.427999999998065'], ['3', '3', '-48.383999999998196'],
                ['3', '3', '-2.8619999999973516'], ['2', '2', '-37.339999999996508'], ['2', '2', '-23.817999999999302'],
                ['3', '3', '-43.534999999999854'], ['2', '2', '-31.252000000000407'], ['1', '1', '-65.730000000003201'],
                ['2', '2', '-20.208000000002357'], ['3', '3', '-3.3590000000040163'], ['2', '2', '-7.0760000000045693'],
                ['1', '1', '-9.5540000000073633'], ['1', '1', '19.967999999993481'], ['4', '4', '61.375999999992928'],
                ['3', '3', '-5.2600000000056752'], ['2', '2', '9.1039999999957217'], ['1', '1', '-25.532000000002881'],
                ['1', '1', '-15.168000000001484'], ['4', '4', '175.51399999999921'], ['3', '3', '30.195999999999913'],
                ['3', '3', '-52.440000000002328'], ['3', '3', '-5.7580000000016298'], ['2', '2', '-55.076000000000931'],
                ['2', '2', '-40.394000000000233'], ['3', '3', '-26.370999999999185'], ['2', '2', '-60.347999999998137'],
                ['1', '1', '-45.665999999997439'], ['2', '2', '-30.98399999999674'], ['1', '1', '11.744000000006054']]
    test_info = gather_info(parse_csv(test_csv))
    print(Mglove_str_gen.worst_grip_str_generator(evaluate_info(gather_info(parse_csv(test_csv)), 0)))
    print(Mglove_str_gen.worst_grip_str_generator(evaluate_info(gather_info(parse_csv(test_csv)), 4)))
    print(Mglove_str_gen.worst_grip_str_generator(evaluate_info(gather_info(parse_csv(test_csv)), 1)))
    print(Mglove_str_gen.summary_generator(evaluate_info(test_info, 0), evaluate_best_grip(test_info)))