__author__ = 'Nathan'
### Nathanial Benjamin, UCI, Calit2, CalPlug, 2014-Feb

######################################################
#                                                    #
#                       MAIN                         #
#                                                    #
######################################################

import CSV_functions
from CSV_functions import read_csv, make_csv
from Interface import gather_info, parse_csv, evaluate_worst_grip, evaluate_best_grip, what_song
from Mglove_str_gen import grip_avg_summary_str,summary_generator,emo_less_feedback,worst_grip_str_generator
from Send_to_voice_server import reset_RIVA_log,text_to_RIVA,text_to_ispeech,ispeech_formatter,to_no_voice_log
from time import sleep, strftime
from user_stats import User_Stats

'''

'''
SONG_OVER_CHECK_TIME = 10
TIME_BETWEEN_FEEDBACK = 30
ACCEPTABLE_LEVEL = 150

class MusicGloveSong:


    def __init__(self):
        self. _feedback_plat = 'RIVA' # possible choices: RIVA, iSpeech, and Text
        self. _grip_count = 0
        self. _lastline = self._read_lastline()
        self. _last_30_sec = []
        self. _csv_result = []
        self. _song_over = True
        self. _last_worst_grip = 0
        self. _RIVA_message_num = 0
        self. _last_response = ''
        self.user_stats = User_Stats()
        pass


    def _check_completion(self) -> None:
        """ waits 5 seconds then check if lastline matches past iteration's lastline
        """
        sleep(SONG_OVER_CHECK_TIME)        ###Wait 10 seconds
        #print("entering 5sec")
        csv_lastline = self._read_lastline()
        #print("csv_lastline = ", csv_lastline)
        #print("self._lastline = ", self._lastline)
        if csv_lastline == self._lastline:
            self._song_over = True
            print("Song Over")
        else:
            #print("song continues")
            self._lastline = csv_lastline
            self._song_over = False
        return


    def _summarize_period(self) -> None:
        """ Call time_5_sec() 6 times, if the song ends return immediately, otherwise return once iterations are complete.
        """
        #print("entering 30sec")
        for i in range(TIME_BETWEEN_FEEDBACK//SONG_OVER_CHECK_TIME):    ### Wait 30 seconds
            self._check_completion()
            if self._song_over is True:
                break
        self._set_last_30_sec()
        return


    def _set_last_30_sec(self) -> None:
        """ sets the grip list for the past 30 seconds of the song
        """
        #print("entering set_last_30")
        grip_list = read_csv(CSV_functions.MUSICGLOVE)
        test_info = len(grip_list)
        if self._grip_count == 0:
            self._grip_count = len(grip_list)
        else:
            for j in range(self._grip_count):
                #print("j = {} and grip_list = {}".format(j, len(grip_list)))
                grip_list.remove(grip_list[0])
            self._grip_count += len(grip_list)
        self._last_30_sec = grip_list
        return


    def _read_lastline(self)-> str:
        """ Reads the last line of the csv containing the user's grip information
        """
        #print("entering _read_lastline()")
        #print(read_csv(CSV_functions.MUSICGLOVE))
        try:
            lastline = read_csv(CSV_functions.MUSICGLOVE)[-1]
        except IndexError:
            return "Empty File"
        return lastline


    def _compile_result(self, summary: str) -> None:
        """ Extends the result that will be added to the log.csv
        """
        #print("entering _compile_result()")
        self._csv_result.append(summary)
        return

    def select_response(self, best_grip, worst_grip) -> (str,str):
        """ Chooses an appropriate response based upon user's performance. Returns that response string"""
        print("last response =", self._last_response)
        print("worst_grip = ", worst_grip, "avg = ", self.user_stats.get_grip_avg(worst_grip))
        print("best_grip = ", best_grip, "avg = ", self.user_stats.get_grip_avg(best_grip))
        print("overall avg = ", self.user_stats._overall_avg)
        if self._last_response == "training_prompt":
            print("Training Response")
            # Call training_response(self._last_worst_grip, self.user_stats.get_old_grip_avg(self._last_worst_grip), self.user_stats.get_grip_avg(self._last_worst_grip))
            # If the prompt was positive
            self._last_response = "training_response"
            # Else self._last_response = "training_prompt" ???              #If a training prompt is repeated multiple times do we disable it after a certain point?
            #                                                               # Should we have two seperate training response functions and decide positive/negative here?
            return "training_response"
        elif self.user_stats.get_grip_avg(best_grip) > ACCEPTABLE_LEVEL:
            print("Negative Response")
            self._last_response = "negative_response"
            # Call negative_response()
            return "negative_response"
        elif self.user_stats.get_grip_avg(worst_grip) < ACCEPTABLE_LEVEL:
            # Call positive_response()
            self._last_response = "positive_response"
            print("Positive Response")
            return "positive_response"
        self._last_response = "training_prompt"
        print("Training Prompt")
        # Call training_prompt(self._last_worst_grip)
        return "training_prompt"






    def test_for_restart(self) -> None:
        """ Tests whether the a new song has been started
        """
        #print("entering test_for_restart()")
        while True:
            self._check_completion()
            if self._song_over is False:
                if self._feedback_plat == "RIVA":
                    reset_RIVA_log()
                elif self._feedback_plat == "Text":
                    to_no_voice_log((emo_less_feedback(0,0,0)))
                self.execute_song()
                if self._song_over is True:
                    interface_info = gather_info(
                        parse_csv(read_csv(CSV_functions.MUSICGLOVE)))
                    #print(interface_info)
                    self.user_stats.set_grips(interface_info)
                    self._compile_result(grip_avg_summary_str(interface_info))
                    evaluated_info = [evaluate_worst_grip(interface_info, self._last_worst_grip),
                                      evaluate_best_grip(interface_info)]
                    summary = summary_generator(evaluated_info[0],evaluated_info[1])
                    if self._feedback_plat == "RIVA":
                        self._RIVA_message_num += 1
                        #print("message_num={} summary={}".format(self._message_num, summary))
                        text_to_RIVA(self._RIVA_message_num, evaluated_info[0],evaluated_info[1])
                    elif self._feedback_plat == "Text":
                        to_no_voice_log(emo_less_feedback(self._RIVA_message_num,evaluated_info[0],evaluated_info[1]))
                    else:
                        text_to_ispeech(ispeech_formatter(summary))
                    self._last_30_sec = []
                    self._compile_result(summary)
                    self._csv_result.extend(read_csv(CSV_functions.MUSICGLOVE))
                    make_csv(self._csv_result, CSV_functions.M_GLOVE_SUMMARIES, what_song(self._grip_count))
                    self.__init__()
            else:
                print("no restart yet")
        return


    def execute_song(self) -> None:
        """ organizes methods, and runs a song
        """
        print("entering execute_song()")
        while self._song_over is False:
            self._summarize_period()
            grip_info = gather_info(parse_csv(self._last_30_sec))
            self.user_stats.set_grips(grip_info)
            best_grip = evaluate_best_grip(grip_info)
            self._compile_result(grip_avg_summary_str(grip_info))
            summary = self.select_response(evaluate_worst_grip(grip_info, self._last_worst_grip),best_grip)
            #summary = summary_generator(evaluate_worst_grip(grip_info, self._last_worst_grip),best_grip)
            self._last_worst_grip = evaluate_worst_grip(grip_info, self._last_worst_grip)
            self._compile_result(summary)
            self._compile_result('system time = {}'.format(strftime("%H:%M:%S")))
            self._compile_result(' ')
            if self._song_over is True:
                print('Number of grips this song = ', self._grip_count)
                return
            if self._feedback_plat == "RIVA":
                self._RIVA_message_num += 1
                text_to_RIVA(self._RIVA_message_num, self._last_worst_grip, best_grip)
            elif self._feedback_plat == "Text":
                to_no_voice_log(emo_less_feedback(self._RIVA_message_num,self._last_worst_grip,best_grip))
            else:
                text_to_ispeech(ispeech_formatter(summary))
        return
            



if __name__ == "__main__":
    reset_RIVA_log()
    MusicGloveSong().test_for_restart()