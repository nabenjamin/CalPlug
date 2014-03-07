__author__ = 'Nathan'
### Nathanial Benjamin, UCI, Calit2, CalPlug, 2014-Feb


import time
import CSV_functions
import Interface
import Mglove_str_gen
import Send_to_voice_server

'''
   -Add grip stats to stat temp.csv
   -Add 2nd worst grip str, if worst grip hasn't changed
   -Add function to test which song is being played by comparing to song files on MusicGlove server.

   __Try enclosing summary in compile results in an extra set of brackets:  [[summary]]
'''
SONG_OVER_CHECK_TIME = 10
TIME_BETWEEN_FEEDBACK = 30

class MusicGloveSong:


    def __init__(self):
        self. _grip_count = 0
        self. _lastline = self._read_lastline()
        self. _last_30_sec = []
        self. _csv_result = []
        self. _song_over = True
        pass


    def _time_5_sec(self) -> None:
        """ waits 5 seconds then check if lastline matches past iteration's lastline
        """
        time.sleep(SONG_OVER_CHECK_TIME)
        print("entering 5sec")
        csv_lastline = self._read_lastline()
        print("csv_lastline = ", csv_lastline)
        print("self._lastline = ", self._lastline)
        if csv_lastline == self._lastline:
            self._song_over = True
            print("Song Over")
        else:
            print("song continues")
            self._lastline = csv_lastline
            self._song_over = False


    def _time_30_sec(self) -> None:
        """ Call time_5_sec() 6 times, if the song ends return immediately, otherwise return once iterations are complete.
        """
        print("entering 30sec")
        for i in range(TIME_BETWEEN_FEEDBACK//SONG_OVER_CHECK_TIME):                          ### Wait 30 seconds
            self._time_5_sec()
            if self._song_over is True:
                break
        self._set_last_30_sec()


    def _set_last_30_sec(self) -> None:
        print("entering set_last_30")
        grip_list = CSV_functions.read_csv(CSV_functions.MUSICGLOVE)
        if self._grip_count == 0:
            self._grip_count = len(grip_list)
        else:
            for j in range(self._grip_count):
                print("j = {} and grip_list = {}".format(j, len(grip_list)))
                grip_list.remove(grip_list[0])
        self._last_30_sec = grip_list


    def _read_lastline(self)-> str:
        """ Reads the last line of the csv
        """
        print("entering _read_lastline()")
        lastline = CSV_functions.read_csv(CSV_functions.MUSICGLOVE)[-1]
        return lastline


    def _compile_result(self, summary: str) -> None:
        """ Extends the result that will be added to the log.csv
        """
        print("entering _compile_result()")
        self._csv_result.extend(self._last_30_sec)
        self._csv_result.extend([summary])


    def test_for_restart(self) -> None:
        """ Tests whether the a new song has been started
        """
        print("entering test_for_restart()")
        while True:
            self._time_5_sec()
            if self._song_over is False:
                self.execute_song()
                if self._song_over is True:
                    interface_info = Interface.gather_info(Interface.parse_csv(CSV_functions.read_csv(CSV_functions.MUSICGLOVE)))
                    summary = Mglove_str_gen.summary_generator(Interface.evaluate_info(interface_info),
                                                               Interface.evaluate_best_grip(interface_info))
                    Send_to_voice_server.text_to_ispeech(Send_to_voice_server.text_str_translator(summary))     ###print("summary = ",summary)
                    self._last_30_sec = []
                    self._compile_result(summary)
                    CSV_functions.make_csv(self._csv_result)
                    self.__init__()
            else:
                print("no restart yet")


    def execute_song(self) -> None:
        """ organizes methods, and runs a song
        """
        print("entering execute_song()")
        while self._song_over is False:
            self._time_30_sec()
            summary = Mglove_str_gen.worst_grip_str_generator(Interface.evaluate_info(Interface.gather_info(Interface.parse_csv(self._last_30_sec))))
            self._compile_result(summary)
            if self._song_over is True:
                break
            Send_to_voice_server.text_to_ispeech(Send_to_voice_server.text_str_translator(summary))         ###print("summary = ",summary)
            

if __name__ == "__main__":
    S = MusicGloveSong()
    S.test_for_restart()
