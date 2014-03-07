import urllib
from urllib import request
import Mglove_str_gen
import winsound
import Interface
import CSV_functions

###Need to replace spaces in text_str with pluses

def text_str_translator(text_str) -> None:
    ''' Replaces all the spaces ' ' in a string, with pluses '+'
    '''
    print("entering text_str_translator")
    translated_string = text_str.replace(' ', '+')
    return translated_string


def text_to_ispeech(text_str) -> None:

    ### actual_server_info = 'http://api.ispeech.org/api/rest?apikey=18cf918d69404c654f6a7fb037302c67&action=convert&voice=usenglishfemale&format=wav&filename=myaudiofile&text=I+noticed+that+you+were+having+a+little+trouble+with+the+blue+grip'
    print("entering text_to_ispeech")
    URL = ('http://api.ispeech.org/api/rest?apikey=developerdemokeydeveloperdemokey&action=convert&voice=usenglishfemale&format=wav&filename=myaudiofile&text=' + text_str)
    mp3file = urllib.request.urlopen(URL)
    output = open('test.mp3','wb')
    output.write(mp3file.read())
    output.close()

    winsound.PlaySound('test.mp3', winsound.SND_FILENAME)
"""
if __name__ == '__main__':
    test = Mglove_str_gen.worst_grip_str_generator(Interface.evaluate_info(Interface.gather_info(Interface.parse_csv(CSV_functions.read_csv(CSV_functions.MUSICGLOVE)))))
    print(test)
    print(text_str_translator(test))
    #text_to_ispeech(text_str_translator(test))
"""