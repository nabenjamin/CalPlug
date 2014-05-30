__author__ = 'Nathan'
### Nathanial Benjamin, UCI, Calit2, CalPlug, 2014-Feb

from random import randrange
from time import strftime, gmtime

""" Remove lines 5 and 73 (meant for testing)
    check if sergio wants encouragment string removed from NORIVA.log...
    Also check if there should be semi-colons between strings in NORIVA.log...
"""

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
    'Have you been practicing?!',
    'Keep up the good work!'
]

WORST_GRIP_STR_LIST = [
    "I noticed that you were having a little trouble with the ", #blue grip...for example
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
    "you are doing great with the"
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
    grip_string = ('{} {}.'.format(WORST_GRIP_STR_LIST[randrange(len(WORST_GRIP_STR_LIST))], grip_selector(worst_grip)))
    print('system time = {}'.format(strftime("%H;%M;%S")))
    return '{} {} {}'.format(encouraging_str_generator(), WORST_GRIP_STR_LIST[randrange(len(
        WORST_GRIP_STR_LIST))], grip_selector(worst_grip))


def grip_selector(grip):
    ''' Returns the string corresponding to the grip number (grip)
    '''
    if grip == 1:
        return GRIP_1
    elif grip == 2:
        return GRIP_2
    elif grip == 3:
        return GRIP_3
    elif grip == 4:
        return GRIP_4
    elif grip == 5:
        return GRIP_5
    elif grip == 0:
        return ''

def summary_generator(worst_grip: int, best_grip: int) -> str:
    ''' Returns 3 sentences: an encouragement_str, worst_grip_str, best_grip_str
    '''
    return '{} {}!'.format(worst_grip_str_generator(worst_grip),
                            BEST_GRIP_STR_LIST[randrange(len(BEST_GRIP_STR_LIST))],
                            grip_selector(best_grip))

def RIVA_translator(msg_number: int, worst_grip: int, best_grip: int) -> str:
    ''' Takes a generated feedback string, prepends number for RIVA's facial generator
    '''
    if best_grip  == 0:
        best_grip_str = 0
    else:
        best_grip_str = str(randrange(1,len(BEST_GRIP_STR_LIST)+1))
    return 'NewData:{};ENCOURAGEMENT:{};WORST_GRIP_STR:{};WORSt_GRIP:{};BEST_GRIP_STR:{};BEST_GRIP:{}\r\n'.format(
        str(msg_number),
        str(randrange(1,len(ENCOURAGEMENT_STR_LIST)+1)),
        str(randrange(1,len(WORST_GRIP_STR_LIST)+1)), worst_grip,
        best_grip_str, best_grip)
"""
def OLD_RIVA_translator(summary: str) -> str:
    ''' Takes a generated feedback string, prepends number for RIVA's facial generator
    '''
    return "{};TTS:{}".format(ENCOURAGEMENT_STR_LIST.index(summary.split('!')[0] + '!'), summary)
"""


def emo_less_feedback(msg_num: int, worst_grip: int, best_grip=0) -> str:
    ''' Takes a worst grip and optional best grip, and returns an emotionless string representation
    '''
    result = ["Worst Grip = " + grip_selector(worst_grip)]
    if best_grip != 0:
        result.append("Best Grip = " + grip_selector(best_grip))
    else:
        result.append('0')
    return "NewData:{};TTS1:Have you been practicing?!:TTS2:{}TTS3:{}".format(msg_num,result[0],result[1])

if __name__ == '__main__':
    print(RIVA_translator(1,3,0))
    print(RIVA_translator(2,1,5))
    print(emo_less_feedback(3,0))
    print(emo_less_feedback(1,5))
    print(summary_generator(1,2))
    print(summary_generator(4,1))
    print(summary_generator(5,3))
    print(summary_generator(2,5))
    print(summary_generator(3,4))
