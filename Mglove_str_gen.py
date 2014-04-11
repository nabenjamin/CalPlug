__author__ = 'Nathan'
### Nathanial Benjamin, UCI, Calit2, CalPlug, 2014-Feb

from random import randrange

# Grip list
GRIP_1 = 'Red Grip'
GRIP_2 = 'Blue Grip'
GRIP_3 = 'Green Grip'
GRIP_4 = 'Purple Grip'
GRIP_5 = 'Yellow Grip'


ENCOURAGEMENT_STR_LIST = [
    'You are doing very well!',
    'Good job on that last set!',
    'You have improved a lot!',
    'Excellent work!',
    'Have you been practicing?',
    'Keep up the good work!'
]

WORST_GRIP_STR_LIST = [
    "I noticed that you were having a little trouble with the ", #blue grip...for
    "On this next set lets try focusing on the ",
    "We could still do a little more work on the ",
    "Why don't we focus on the ",
    "Let's keep working on the "
]

BEST_GRIP_STR_LIST = [
    "But I also noticed you have improved quite a bit on the", #blue grip...for
    "You did well on the",
    "You seemed most proficient with the",
    "You obviously do not need any more practise on the",
    "you are doing great with the",
]

def grip_avg_summary_str(grip_avg_list: list) -> str:
    ''' returns a string showing the average times for all grips (includes grips that may have been unused this song)
    '''
    return "Red Grip avg: {}; Blue Grip avg: {};Green Grip avg: {}; Purple Grip avg: {}; Yellow Grip avg: {}".format(
        grip_avg_list[0], grip_avg_list[1], grip_avg_list[2], grip_avg_list[3], grip_avg_list[4])


def encouraging_str_generator() -> str:
    ''' Make an encouraging statement
    '''
    return ENCOURAGEMENT_STR_LIST[randrange(len(ENCOURAGEMENT_STR_LIST))]


def worst_grip_str_generator(worst_grip: int) -> str:
    '''Join an encouragement string with an appropriate finger string'''
    grip = ''
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
    elif worst_grip == 0:
        return encouraging_str_generator()
    grip_string = ('{} {}.'.format(WORST_GRIP_STR_LIST[randrange(len(WORST_GRIP_STR_LIST))], grip))
    return ('{} {}'.format(encouraging_str_generator(), grip_string))


def summary_generator(worst_grip: int, best_grip: int) -> str:
    ''' Returns 3 sentences: an encouragement_str, worst_grip_str, best_grip_str
    '''
    grip = ''
    # determine grip was best
    if best_grip == 1:
        grip = GRIP_1
    elif best_grip == 2:
        grip = GRIP_2
    elif best_grip == 3:
        grip = GRIP_3
    elif best_grip == 4:
        grip = GRIP_4
    elif best_grip == 5:
        grip = GRIP_5
    best_grip_str = ('{} {}'.format(BEST_GRIP_STR_LIST[randrange(len(BEST_GRIP_STR_LIST))], grip))
    return ('{} {}!'.format(worst_grip_str_generator(worst_grip), best_grip_str))




if __name__ == '__main__':
    print(summary_generator(1,2))
    print(summary_generator(4,1))
    print(summary_generator(5,3))
    print(summary_generator(2,5))
    print(summary_generator(3,4))
