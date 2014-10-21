__author__ = 'Nathan'
### Nathanial Benjamin, UCI, Calit2, CalPlug, 2014-Feb


import urllib
from urllib import request
import winsound
from pydub import AudioSegment
from Mglove_str_gen import RIVA_translator, emo_less_feedback
###     Note: pydub requires FFmpeg to convert audio files, make sure it is on the host computer.

### RIVA log file
RIVA_LOG = "Z:\\musicglove\\resources\\saves\\temp\\RIVA_log.txt"
LOCAL_RIVA_LOG = "C:\\Users\\Nathan\\Desktop\\CalPlug\\RIVA_log.txt"
NO_VOICE_LOG = "Z:\\musicglove\\resources\\saves\\temp\\NORIVA_log.txt"

def txt_to_NPCEditor(turn_id, text_str) -> None:
    """takes given text string and turns it into a VHToolkit vrSpeech call
    vrSpeech start turn_id user
    vrSpeech finished-speaking turn_id
    vrSpeech interp turn_id 1 1 text_str
    vrSpeech asr-complete turn_id
    """
    pass

def ispeech_formatter(text_str: str) -> None:
    """ Replaces all the spaces ' ' in a string, with pluses '+'
    """
    print("entering text_str_translator")
    translated_string = text_str.replace(' ', '+')
    return translated_string


def text_to_ispeech(text_str: str) -> None:
    developer_trial_version = 'http://api.ispeech.org/api/rest?apikey=developerdemokeydeveloperdemokey&action=convert&voice=usenglishfemale&format=mp3&filename=myaudiofile&text='
    actual_server_info = 'http://api.ispeech.org/api/rest?apikey=18cf918d69404c654f6a7fb037302c67&action=convert&voice=usenglishfemale&speed=0&format=mp3&text='
    #print("entering text_to_ispeech")
    URL = (developer_trial_version + text_str)
    mp3file = urllib.request.urlopen(URL)
    output = open('test.mp3','wb')
    output.write(mp3file.read())
    output.close()
    play_sound("test.mp3")
    return


def play_sound(filename: str) -> None:
    """Plays the Feedback from the virtual trainer"""
    AudioSegment.converter = 'C:\\vhtoolkit\\bin\\FFmpeg\\bin\\ffmpeg.exe'
    song = AudioSegment.from_mp3(filename)
    song.export("test.wav", format='wav')
    winsound.PlaySound("test.wav", winsound.SND_FILENAME)
    return


def reset_RIVA_log() -> None:
    #print("entering reset_RIVA_log")
    with open(RIVA_LOG, 'w') as file:
        file.write("NewData:0;ENCOURAGEMENT:0;WORST_GRIP_STR:0;WORST_GRIP:0;BEST_GRIP_STR:0;BEST_GRIP:0")
        #print("NewData:0;ENCOURAGEMENT:0;WORST_GRIP_STR:0;WORST_GRIP:0;BEST_GRIP_STR:0;BEST_GRIP:0")


def text_to_RIVA(msg_number: int, worst_grip: int, best_grip: int, RIVA_direction, msg='') -> None:
    """takes a number representing how many messages have been sent this song, and a txt string. formats it for RIVA
    """
    # for best grip if a best grip str will not be included, put a five in its place.
    #print("entering text_to_RIVA")
    RIVA_message = RIVA_translator(msg_number,worst_grip,best_grip,RIVA_direction, message=msg)
    with open(RIVA_LOG, 'w', newline= '\n') as outfile:
        outfile.write(RIVA_message)
        print(RIVA_message)


def to_no_voice_log(message: str) -> None:
    """ Takes a worst and best grips, then sends them to Musicglove's logfile
    """
    #print("entering to_no_voice_log")
    with open(NO_VOICE_LOG, 'w', newline= '\n') as outfile:
        outfile.write(message)
        print(message)



'''
def Old_text_to_RIVA(msg_number: int, text_str: str) -> None:
    """takes a number representing how many messages have been sent this song, and a txt string. formats it for RIVA
    """
    # for best grip if a best grip str will not be included, put a five in its place.
    print("entering text_to_RIVA")
    with open(RIVA_LOG, 'w', newline= '\n') as outfile:
        outfile.write('NewData:{};{}\r\n'.format(str(msg_number), text_str))
        print('NewData:{};{}\r\n'.format(str(msg_number), text_str))
'''



if __name__ == '__main__':
    test = 'Keep up the good work! I noticed that you were having a little trouble with the Blue Grip. But I also noticed you have improved quite a bit on the Yellow Grip!'
    print(test)
    print(ispeech_formatter(test))
    #text_to_ispeech(text_str_translator(test))
    reset_RIVA_log()
    text_to_RIVA(1,3,0)
    text_to_RIVA(2,1,0)
    text_to_RIVA(3,2,0)
    text_to_RIVA(4,4,0)
    text_to_RIVA(5,5,3)
