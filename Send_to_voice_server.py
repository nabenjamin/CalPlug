import urllib
from urllib import request
import winsound
import os

def text_str_translator(text_str) -> None:
    ''' Replaces all the spaces ' ' in a string, with pluses '+'
    '''
    print("entering text_str_translator")
    translated_string = text_str.replace(' ', '+')
    return translated_string


def text_to_ispeech(text_str) -> None:
    developer_trial_version = 'http://api.ispeech.org/api/rest?apikey=developerdemokeydeveloperdemokey&action=convert&voice=usenglishfemale&format=wav&filename=myaudiofile&text='
    actual_server_info = 'http://api.ispeech.org/api/rest?apikey=18cf918d69404c654f6a7fb037302c67&action=convert&voice=usenglishfemale&speed=0&format=mp3&text='
    print("entering text_to_ispeech")
    URL = (developer_trial_version + text_str)
    mp3file = urllib.request.urlopen(URL)
    output = open('testmp3.mp3','wb')
    output.write(mp3file.read())
    output.close()
    play_sound('testmp3.mp3')
    return

def play_sound(filename: str) -> None:
    '''Plays the selected audiofile'''
    ###os.system("start C:\\Users\\Nathan\\PycharmProjects\\VH_MusicGlove_Interface\\" + filename)
    winsound.PlaySound(filename, winsound.SND_FILENAME)

if __name__ == '__main__':
    test = 'Keep up the good work! I noticed that you were having a little trouble with the Blue Grip. But I also noticed you have improved quite a bit on the Yellow Grip!'
    print(test)
    print(text_str_translator(test))
    text_to_ispeech(text_str_translator(test))
