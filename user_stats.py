__author__ = 'Nathan'

### Nathanial Benjamin, UCI, Calit2, CalPlug, 2014-Feb

### if overall avg <0 tell user they're reacting too early
### if overall avg >0 tell user they're reacting too late

from Interface import gather_info, parse_csv, evaluate_worst_grip, evaluate_best_grip, what_song
from collections import namedtuple
Difference = namedtuple('Difference', 'red blue green purple yellow overall')

class User_Stats:
    def __init__(self):
        self._old_red_avg = 0
        self._old_blue_avg = 0
        self._old_green_avg = 0
        self._old_purple_avg = 0
        self._old_yellow_avg = 0
        self._old_overall_avg = 0
        self._red_avg = 0
        self._blue_avg = 0
        self._green_avg = 0
        self._purple_avg = 0
        self._yellow_avg = 0
        self._overall_avg = 0
        self._difference = Difference(0,0,0,0,0,0)
        self._followup = None        # The grip which the user was last assigned to concentrate on.

    def set_grips(self, grips: tuple):
        """ Updates old grips to those from the last call, and sets the new grip averages to match those since the last call.
        """
        #print("entering set_grips")
        self._old_red_avg = self._red_avg
        self._old_blue_avg = self._blue_avg
        self._old_green_avg = self._green_avg
        self._old_purple_avg = self._purple_avg
        self._old_yellow_avg = self._yellow_avg
        self._red_avg = grips[0]
        self._blue_avg = grips[1]
        self._green_avg = grips[2]
        self._purple_avg = grips[3]
        self._yellow_avg = grips[4]
        self.set_difference()
        self.set_overall_avg()

    def get_grip_avg(self, grip_number: int) -> float:
        """ Takes an int representing a grip, and returns that grips average"""
        avgs = [self._red_avg, self._blue_avg, self._green_avg, self._purple_avg, self._yellow_avg]
        for i in range(1,5):
            if i == grip_number:
                print("i="+ str(i))
                return avgs[i]

    def get_old_grip_avg(self, grip_number: int) -> float:
        """ Takes an int representing a grip, and returns that grips average"""
        avgs = [self._old_red_avg, self._old_blue_avg, self._old_green_avg, self._old_purple_avg, self._old_yellow_avg]
        for i in range(1,5):
            if i == grip_number:
                return avgs[i-1]

    def _new_overall_avg(self):
        """ Calculates the new_overall average
        """
        #print("entering _overall_avg")
        sum = (self._red_avg+self._green_avg+self._blue_avg+self._purple_avg+self._yellow_avg)
        if sum == 0:
            return 0
        return sum / 5

    def set_overall_avg(self):
        """ Updates old to match the overall average from the last call, and new overall average to match this call.
        """
        #print("entering set_overall_avg")
        self._old_overall_avg = self._overall_avg
        self._overall_avg = (self._overall_avg + self._new_overall_avg())/2
        #print("in set_overall_avg: overall avg = ", self._overall_avg)

    def get_overall_avg(self) -> float:
        return self._overall_avg

    def get_old_overall_avg(self) -> float:
        return self._old_overall_avg

    def set_difference(self):
        """ Sets the difference tuple to show the  average error difference between the past 30 seconds and the current
            30 seconds
        """
        #print("entering set_difference")
        self._difference = Difference(abs(self._old_red_avg) - abs(self._red_avg),
                                     abs(self._old_blue_avg) - abs(self._blue_avg),
                                     abs(self._old_green_avg) - abs(self._green_avg),
                                     abs(self._old_purple_avg) - abs(self._purple_avg),
                                     abs(self._old_yellow_avg) - abs(self._yellow_avg),
                                     abs(self._old_overall_avg) - abs(self._overall_avg))

    def overall_avg_feedback(self):
        """ Assigns feedback relating to the overall average of all griptimes.
        """
        print("entering overall_avg_feedback")
        #If the difference between the past and current overall grip averages is negative then return improved feedback
        if self._difference.overall >= 0:
            return "overall_improvment_feedback"
        else:
            #If overall average is positive tell the user they are late; otherwise tell them they are early
            if self._overall_avg > 0:
                return "user is too late"
            else:
                return "user is too early"

    def grip_feedback(self):
        """ Check to see which grip has the largest difference between the past and present 30 seconds
        """
        print("entering grip_feedback")
        test, result = self._difference.red, 'red'
        if test < self._difference.blue:
            test, result = self._difference.blue, 'blue'
        elif test < self._difference.green:
            test, result = self._difference.green, 'green'
        elif test < self._difference.purple:
            test, result = self._difference.purple, 'purple'
        else:
            test, result = self._difference.yellow, 'yellow'
        # Then check whether that grip's difference shows improvement over the past 30 seconds.
        if test >= 0:
            return "best_grip_feedback"
        else:
            self._followup = result
            return "worst_grip_feedback"

    def followup_feedback(self):
        """ Check whether the user has improved on their assigned grip
        """
        #print("entering followup_feedback")
        if eval('self._difference.{}'.format(self._followup)) >= 0:
            return "improved_feedback_str"
        else:
            return "negative_feedack_str"


    def select_feedback(self):
        """ Figure out whether to use overall feedback or feedback for a specific grip
        """
        print("entering select_feedback")
        if self._followup != None:
            return self.followup_feedback()
        #print(max(self._difference.red,    self._difference.blue, self._difference.green,
        #       self._difference.purple, self._difference.yellow))
        #print(max(self._difference.red,    self._difference.blue, self._difference.green,
        #       self._difference.purple, self._difference.yellow) >= self._difference.overall)
        if max(self._difference.red,    self._difference.blue, self._difference.green,
               self._difference.purple, self._difference.yellow) >= self._difference.overall:
            return self.overall_avg_feedback()
        else:
            return self.grip_feedback()

if __name__ == '__main__':
    test_csv = [['1', '1', '-1'], ['4', '4', '-4'], ['3', '3', '-3'],
                ['3', '3', '3'], ['3', '3', '3'], ['2', '2', '2'],
                ['2', '2', '2'], ['3', '3', '3'], ['2', '2', '2'],
                ['1', '1', '1'], ['2', '2', '-2'], ['1', '1', '1'],
                ['4', '4', '-4'], ['3', '3', '-3'], ['3', '3', '-3'],
                ['3', '3', '-3'], ['2', '2', '-2'], ['2', '2', '-2'],
                ['3', '3', '-3'], ['2', '2', '-2'], ['1', '1', '-1'],
                ['2', '2', '-2'], ['3', '3', '-3'], ['2', '2', '-2'],
                ['1', '1', '-1'], ['1', '1', '1'], ['4', '4', '4'],
                ['3', '3', '-3'], ['2', '2', '2'], ['1', '1', '-1'],
                ['1', '1', '-1'], ['4', '4', '4'], ['3', '3', '3'],
                ['3', '3', '-3'], ['3', '3', '-3'], ['2', '2', '-2'],
                ['2', '2', '-2'], ['3', '3', '-3'], ['2', '2', '-2'],
                ['1', '1', '-1'], ['2', '2', '-2'], ['1', '1', '1']]
    print(test_csv)
    print(parse_csv(test_csv))
    test_info = gather_info(parse_csv(test_csv))
    print(test_info)
    test = User_Stats()
    test.set_overall_avg(-14.003)
    test.set_grips(test_info)
    print()
    print("new values: {}, {}, {}, {}, {}, {}".format(test._red_avg,test._blue_avg, test._green_avg, test._purple_avg, test._yellow_avg, test._overall_avg))
    print(test._difference)
    print("old values: {}, {}, {}, {}, {}, {}".format(test._old_red_avg,test._old_blue_avg, test._old_green_avg, test._old_purple_avg, test._old_yellow_avg, test._old_overall_avg))
    print("test 1 = " + test.select_feedback())
    for t in [1,2,3,4,5]:
        print("t= {}; avg= {}; old_avg= {}".format(int(t), test.get_grip_avg(t), test.get_old_grip_avg(t)))
    '''test.set_overall_avg(-1)
    print("test 2 = " + test.select_feedback())
    test.set_overall_avg(14.003)
    print("test 3 = " + test.select_feedback())
    test.set_overall_avg(1)
    print("test 4 = " + test.select_feedback())
    test.set_overall_avg(3)
    test._followup = "red"
    print("test 5 = " + test.select_feedback())
    '''
