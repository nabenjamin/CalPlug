### Nathanial Benjamin, UCI Calit2 CalPlug 2014-Feb

### Timing program allowing the MusicGlove interface program to be called
###    at regular intervals during a song.

import time
import Interface
'''
    -Without clearing the test.csv file, on each iteration,
       it will be difficult to track the stats for each 30 period
       rather than tracking a cummulative total for the entire session.

    -How do I start this in tandem with the start of the song..?
       could be opened on another screen, as the song begins
       or controlled by the tester during an observational experiment...
'''

TIME_BETWEEN_RESPONSES = 15

clock = time.perf_counter()     ###Can be used to time the session
user_input = 'y'

while user_input != 'q':        ###Concept Test
    
    time.sleep(TIME_BETWEEN_RESPONSES)
    print(Interface.response_generator(Interface.evaluate_info(Interface.gather_info(Interface.read_csv()))))
    ###user_input = input("Please enter a letter, q will quit")     ###Concept Test
