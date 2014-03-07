__author__ = 'Nathan'
### Nathanial Benjamin, UCI, Calit2, CalPlug, 2014-Feb

### The MusicGlove interface: evaluates a csv file's data and converts that data into statistics telling how well the
###    user is preforming, then returns a string giving encouragement and advice.

"""
currently when incorrect input is done 'nan' is being interpreted as 200 25% more than the maximum late grip
    -how much should nan be worth, compared to a slow response?
    -i.e. I missed purple twice because I wasn't paying attention, but I really was slow on yellow.
    -Solution? -- Give an accepted misses threshold?
add ability to test if worst grip has remained the same... if it has substitute 2nd worst grip
"""

import Mglove_str_gen
from collections import namedtuple
Stat = namedtuple('Stat', 'expected actual difference')

def parse_csv(infile: "stat_list") -> [Stat]:
    '''Read data from a .csv file, and return a namedtuple containing
       the actual and expected fingers, and the time difference from expected.
    '''
    ALPHA = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    print("entering parse_CSV")
    stat_list = []
    for temp_stat in infile:
        try:
            if type(temp_stat) is str:
                continue
            if temp_stat[2] == 'nan': #Keep it from throwing errors because 'nan' is not a float
                temp_stat[2] = -200 # A missed grip will count 25% more than the maximum late/early grip
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

def evaluate_info(grip_times: [int]) -> int:
    '''Determines which grip needs the most focus'''
    print("entering evaluate info")
    current = 0
    worst_grip = 0
    i = 0
    for time in grip_times:
        i += 1
        if current < time:
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
        if current > time:
            if current != 0:
                current = time
            best_grip = i
            print("best grip =", best_grip)
    return best_grip


if __name__ == '__main__':
    print(Mglove_str_gen.worst_grip_str_generator(evaluate_info(gather_info(parse_csv()))))
