__author__ = 'Nathan'
### Nathanial Benjamin, UCI, Calit2, CalPlug, 2014-Feb

from random import randrange
from time import strftime, gmtime

'''
Notes:
- Added strings lending more interactivity to the system: "POSITIVE_STRING", "NEGATIVE_STRING", "TRAINING_PROMPT",
    "TRAINING_RESPONSE" and "OVERALL_SUMMARY".
    (commented out until ready for implimentation, need to remove level numbers or instantiate a type [such as namedtuple])
'''

# Grip list
GRIP_1 = 'Red Grip'
GRIP_2 = 'Blue Grip'
GRIP_3 = 'Green Grip'
GRIP_4 = 'Purple Grip'
GRIP_5 = 'Yellow Grip'

'''
POSITIVE_STRING = [
    1 = [
        “YOU’RE DOING WELL, BUT I KNOW YOU CAN DO BETTER.”,
        “LOOKS LIKE YOU KNOW WHAT YOU’RE DOING. SOUNDS LIKE IT TOO!”,
        “PRETTY GOOD JOB ON THAT LAST SET, KEEP GOING!”
    ],
    2 = [
        “YOU’RE GETTING BETTER, KEEP ON GOING!”,
        “THAT LAST SET WAS GOOD WORK!”,
        “FINE JOB ON THAT LAST SET.”
    ],
    3 = [
        “SOLID JOB! YOU’RE DOING GREAT.”,
        “GOOD WORK, KEEP IT UP!”,
        “THAT LAST SET WAS SOME GOOD PLAYING!”
    ],
    4 = [
        “THAT WAS AWESOME! KEEP GOING!”,
        “WELL DONE, YOUR RESPONSE TIMES ARE UNCANNILY RAPID.”,
        “NOW THAT’S WHAT I CALL ACCURATE!”
    ],
    5 = [
        “YOU’RE PLAYING AMAZINGLY! EVEN I’M IMPRESSED, AND I’M A ROBOT.”,
        “WOW, THAT LAST SET WAS INCREDIBLE!”,
        “YOU REALIZE YOUR LAST SET WAS PERFECT, RIGHT?”
    ]
]

NEGATIVE_STRING = [
    1 = [
        “NOT BAD, BUT I’M SURE YOU’LL DO BETTER ON THE NEXT SET.”,
        “NOT BAD, BUT YOU CAN DEFINITELY IMPROVE.”,
        “THAT LAST SET WAS OK, BUT WE CAN DO BETTER.”
    ],
    2 = [
        “NOT QUITE THERE, BUT YOU’RE GETTING THERE!”,
        “JUST A BIT SLOWER BACK THERE, BUT YOU’RE DOING WELL!”,
        “A BIT SLOW ON THAT LAST SET, BUT WE’RE GETTING BETTER.”
    ],
    3 = [
        “YEAH, THAT LAST SET WAS A BIT OF A TOUGH ONE, LET’S GIVE IT ANOTHER GO.”,
        “JUST A BRIEF HICCUP ON THAT LAST ONE, BUT NOTHING TO WORRY ABOUT, I SHOULD THINK.”,
        “THAT LAST SET COULD HAVE GONE BETTER, BUT THAT’S ALRIGHT, WE’LL GET IT NEXT TIME!”
    ],
    4 = [
        “YOU’RE SLOWING DOWN A LITTLE BIT, TRY FOCUSING ON THE POINT WHEN THE BOTTOM OF THE CIRCLE LINES UP WITH THE TARGET!”,
        “PHEW, THAT LAST SET REALLY WAS A DOOZY, BUT DON’T WORRY WE’LL GET BACK ON TRACK.”,
        “THAT LAST PART WAS PRETTY HARD, DON’T SWEAT IT TOO MUCH THOUGH.”
    ],
    5 = [
        “OK, WE CAN JUST PRETEND THAT LAST SET NEVER HAPPENED, NO WORRIES.”,
        “MAYBE… IT’S TIME FOR A LITTLE BREAK.”,
        “YEAH THOSE LAST FEW MEASURES SCARED ME TOO.”
    ]
]

TRAINING_PROMPT = [
    “So I noticed on that last playthrough that you’re doing great with Grip “ “! Grip “ “ is a bit slower, however, so I’d focus a bit more on that one for now.”,
    “Overall, that was a great playthrough, but I noticed you were having trouble with Grip “ “. Why don’t we focus on that one for the next song?”,
    “Great work. We could still do a little more work on Grip “ “ though. Let’s try and focus on that for a little bit.”
]

POS_TRAINING_RESPONSE = [
    “Wow, great work improving your “ “ Grip. There’s been a pretty nice jump in your response times with that grip.”,
    “Hey what did I tell you! Focusing on your “ “ Grip really paid off. I’ve noticed a pretty substantial improvement in that grip's response times.”,
    “So focusing on your “ “ Grip sure paid off! You went from an average response time of “ “ to “ “. Great work!”
]

NEG_TRAINING_RESPONSE = [
    "What happened to the " " Grip?! I thought we were going to focus on it this time?",
    "I know you can do better than that! let's try focusing on the " " Grip again.",
    "I didn't see much improvement on the " " Grip this time. Remember to concentrate on it this next time!"
]

OVERALL_SUMMARY = [
    “Hey, you’re doing better on this song than last time!”,
    “I’ve noticed some significant improvement on this particular song. Great work!”
    “You’ve really got this song down haven’t you?”
]
'''
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
    "On this next set try focusing on the ",
    "You still need a little more work on the ",
    "Why don't we focus on the ",
    "We should keep working on the "
]

BEST_GRIP_STR_LIST = [
    "I noticed you have improved quite a bit on the", #blue grip...for example
    "You did well on the",
    "You seem quite proficient with the",
    "You obviously do not need any more practice on the",
    "you are doing great with the"
]

def training_response(last_worst_grip: int, old_worst_grip_avg: float, new_worst_grip_avg: float) -> str:
    """ Takes the worst grip, it's average, and it's average last session. Checks for improvement, then returns an appropriate string
        if there was improvement congratulate them.
        Else recommit them, note that system asked for a given outcome... or simply call training_prompt()?
        pass failure/success to select_response() function
    """
    pass

def negative_response() -> str:
    """ Returns a scaled negative response                                              # Need to define scale
    """
    pass

def positive_response() -> str:
    """ Returns a scaled positive response                                              # Need to define scale
    """
    pass

def training_prompt(last_worst_grip: int) -> str:
    """Takes a worst grip and provides a string prompting user to improve that grip
    """
    pass

def grip_avg_summary_str(grip_avg_list: list) -> str:
    """ returns a string showing the average times for all grips (includes grips that may have been unused this song)
    """
    return "Red Grip avg: {}; Blue Grip avg: {};Green Grip avg: {}; Purple Grip avg: {}; Yellow Grip avg: {}".format(
        grip_avg_list[0], grip_avg_list[1], grip_avg_list[2], grip_avg_list[3], grip_avg_list[4])


def encouraging_str_generator() -> str:
    """ Make an encouraging statement
    """
    return ENCOURAGEMENT_STR_LIST[randrange(len(ENCOURAGEMENT_STR_LIST))]


def worst_grip_str_generator(worst_grip: int) -> str:
    """Join an encouragement string with an appropriate finger string"""
    grip_string = ('{} {}.'.format(WORST_GRIP_STR_LIST[randrange(len(WORST_GRIP_STR_LIST))], grip_selector(worst_grip)))
    print('system time = {}'.format(strftime("%H;%M;%S")))
    return '{} {} {}'.format(encouraging_str_generator(), WORST_GRIP_STR_LIST[randrange(len(
        WORST_GRIP_STR_LIST))], grip_selector(worst_grip))


def grip_selector(grip):
    """ Returns the string corresponding to the grip number of(grip)
    """
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
    """ Returns 3 sentences: an encouragement_str, worst_grip_str, best_grip_str
    """
    print("Entering summary_generator()")
    return '{} {} {}!'.format(worst_grip_str_generator(worst_grip),
                            BEST_GRIP_STR_LIST[randrange(len(BEST_GRIP_STR_LIST))],
                            grip_selector(best_grip))

def RIVA_translator(msg_number: int, worst_grip: int, best_grip: int) -> str:
    """ Takes a generated feedback string, prepends number for RIVA's facial generator
    """
    if best_grip == 0:
        best_grip_str = 0
    else:
        best_grip_str = str(randrange(1,len(BEST_GRIP_STR_LIST)+1)) + "_" + grip_selector(best_grip)[0]
    return 'NewData:{};ENCOURAGEMENT:{};WORST_GRIP:{}_{};BEST_GRIP:{}'.format(
        str(msg_number),
        str(randrange(1,len(ENCOURAGEMENT_STR_LIST)+1)),
        str(randrange(1,len(WORST_GRIP_STR_LIST)+1)), grip_selector(worst_grip)[0],
        best_grip_str)
'''
def OLD_RIVA_translator(summary: str) -> str:
    """ Takes a generated feedback string, prepends number for RIVA's facial generator
    """
    return "{};TTS:{}".format(ENCOURAGEMENT_STR_LIST.index(summary.split('!')[0] + '!'), summary)
'''

def emo_less_feedback(msg_num: int, worst_grip: int, best_grip=0) -> str:
    """ Takes a worst grip and optional best grip, and returns an emotionless string representation
    """
    result = ["Worst Grip = " + grip_selector(worst_grip)]
    if best_grip != 0:
        result.append("Best Grip = " + grip_selector(best_grip))
    else:
        result.append('')
    return "NewData:{};TTS:{}\n{}".format(msg_num,result[0],result[1])

def training_response(last_worst_grip: int, last_worst_grip_avg: float) -> str:
    """ Takes a grip and it's average, then evaluates if improvment has been made.
    """
if __name__ == '__main__':
    print('RIVA_translator() = ',RIVA_translator(1,3,0))
    print('RIVA_translator() = ',RIVA_translator(2,1,5))
    print('emo_less_feedback() = ',emo_less_feedback(3,2))
    print('emo_less_feedback() = ',emo_less_feedback(1,5,4))
    print('summary_generator() = ',summary_generator(1,2))
    print('summary_generator() = ',summary_generator(4,1))
    print('summary_generator() = ',summary_generator(5,3))
    print('summary_generator() = ',summary_generator(2,5))
    print('summary_generator() = ',summary_generator(3,4))
