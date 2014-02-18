__author__ = 'Nathan'
"""
Need to reroute read_csv() to the actual temp.csv in the server
currently when incorrect input is done 'nan' is being interpreted as 0
"""
from random import randrange
from collections import namedtuple
Stat = namedtuple('Stat', 'expected actual difference')

# Grip list
GRIP_1 = 'Red Grip'
GRIP_2 = 'Blue Grip'
GRIP_3 = 'Green Grip'
GRIP_4 = 'Purple Grip'
GRIP_5 = 'Yellow Grip'


encouragement_string_list = [
    "You are doing very well!",
    "Good job on that last set!",
    "You have improved a lot!",
    "Excellent work",
    "Have you been practicing?",
    "Keep up the good work!"
]

Grip_String_list = [
    "I noticed that you were having a little trouble with the", #blue grip...for
    "On this next set lets try focusing on the",
    "We could still do a little more work on the",
    "Why don't we focus on the",
]
def read_csv() -> [Stat]:
    '''Read data from a .csv file, and return a namedtuple containing
       the actual and expected fingers, and the time difference from expected.
    '''

    stat_list = []
    with open('test.csv', 'r') as infile:

        for line in infile:
            temp_stat = line.strip().split(",")
            if temp_stat[2] == 'nan': #Keep it from throwing errors because 'nan' is not a float
                temp_stat[2] = 0
            stat_list.append(Stat(int(temp_stat[0]), int(temp_stat[1]), float(temp_stat[2])))
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
    current = 0
    worst_grip = 0
    i = 0
    for time in grip_times:
        i += 1
        if current < time:
            current = time
            worst_grip = i
    print(worst_grip)
    return worst_grip

def response_generator(worst_grip: int) -> str:
    '''Join an encouragement string with an appropriate finger string'''
    grip = ''
    print(worst_grip)
    # determine grip that needs work
    if worst_grip == 1:
        grip = GRIP_1
    elif worst_grip == 2:
        grip = GRIP_2
    elif worst_grip == 3:
        grip = GRIP_3
    elif worst_grip == 4:
        grip = GRIP_4
    elif worst_grip == 5:
        grip = GRIP_5

    encouragement_string = encouragement_string_list[randrange(len(encouragement_string_list))]
    if grip == '':
        return encouragement_string

    grip_string = ('{} {}'.format(Grip_String_list[randrange(len(Grip_String_list))], grip))
    return ('{} {}'.format(encouragement_string, grip_string))



'''Test Data
stat_list = read_csv()
for stat in stat_list:
        print("expected grip = {} grip = {} time difference = {}".format(stat.actual, stat.expected, stat.time))
'''

if __name__ == '__main__':
    print(response_generator(evaluate_info(gather_info(read_csv()))))