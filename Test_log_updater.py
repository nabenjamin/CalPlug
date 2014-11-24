__author__ = 'Nathan'

import csv
from CSV_functions import MUSICGLOVE as CSV_FILE
from random import randrange
from time import sleep
import CSV_functions
from CSV_functions import read_csv
from Interface import parse_csv, grip_times
from time import sleep
from user_stats import User_Stats


#CSV_FILE = 'Z:\\musicglove\\resources\\saves\\temp\\temp.csv'
#CSV_FILE = 'C:\\Users\\Nathan\\Desktop\\CalPlug\\temp.csv'


class N_test:

    def __init__(self):
        self.seconds = input("how many seconds should simulation last? ")
        while type(self.seconds) != int:
            try:
                self.seconds = int(self.seconds)
            except:
                self.seconds = input("seconds must be a whole number")
                pass
        self.grip_number = input("how many grips should be used in the test? (1-5): ")
        while self.grip_number not in range(1,6): #really 1-5, range is exclusive...
            try:
                self.grip_number = int(self.grip_number)
            except ValueError:
                self.grip_number = input("number must be between 1 and 5: ")
                pass
        pass

    def new_grip(self, number_of_grips):
        """ Generates a random line for the MGlove log file (assuming correct
                grips)
        """
        grip = randrange(1,number_of_grips+1)
        timing = randrange(-300000,300000)
        if timing != 0:
            timing = timing/1000
        return [grip, grip, timing]

    def chosen_grip(self, number_of_grips: int, diff: int) -> None:
        """ Generates a line, within 10 milliseconds of diff, for the MGlove
                log file(assuming correct grips)
        """
        grip = randrange(1,number_of_grips+1)
        timing = randrange(diff-10,diff+10)
        if timing != 0:
            timing = timing/1000
        return [grip, grip, timing]

    def read_csv(self):
        with open(CSV_FILE, 'r', newline='') as infile:
            temp_list = []
            csv_reader = csv.reader(infile, delimiter=',')
            for line in csv_reader:
                if line == '':
                    temp_list.append("new song")
                    continue
                else:
                    temp_list.append(line)
        return temp_list

    def write_csv(self, temp_list,new_grip):
        with open(CSV_FILE, 'w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile, delimiter=',')
            if temp_list == [] or temp_list[0] == []:
                csv_writer.writerow(new_grip)
            else:               
                for i in temp_list:
                    csv_writer.writerow(i)
                csv_writer.writerow(new_grip)
        return
    
    def update_csv(self, new_grip):
        """ Adds a new line to the CSV File.
        """
        temp_list = self.read_csv()
        self.write_csv(temp_list, new_grip)
        return

    def clear_csv(self):
        with open(CSV_FILE, 'w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile, delimiter=',')
            csv_writer.writerow('')
        return

    def tester1(self) -> None:
        """Updates log file to simulate user interaction with MGlove
        """
        grip_number = self.grip_number
        seconds = self.seconds
        j = 0
        self.clear_csv()
        for i in range(seconds):
            #print("entering sleep")
            self.update_csv(self.new_grip(grip_number))
            sleep(1)
            if i % 30 == 0:
                j += 1
                print("30 second mark number",j)
        print("first simulated song is over")

    def tester2(self) -> None:
        """Updates log file to simulate specified user interaction with MGlove
        """
        grip_number = self.grip_number
        seconds = self.seconds
        self.clear_csv()
        while seconds > 0:
            print("2nd simulated song started")
            for i in range(32):
                self.update_csv(self.chosen_grip(grip_number,150))
                seconds-=1
                sleep(1)
            print("expect welcome")
            for i in range(32):
                seconds-=1
                self.update_csv(self.chosen_grip(grip_number,300))
                sleep(1)
            print("expect Negative")
            grip_list = grip_times(parse_csv(read_csv(CSV_functions.MUSICGLOVE)))
            user_stats = User_Stats()
            for i in range(32):
                seconds-=1
                self.update_csv(self.chosen_grip(grip_number,1))
                sleep(1)
            print("expect Positive")
            grip_list = grip_times(parse_csv(read_csv(CSV_functions.MUSICGLOVE)))
            user_stats = User_Stats()
            for i in range(7):
                seconds-=5
                self.update_csv(self.chosen_grip(1,250))
                for j in range(1,5):
                    self.update_csv(self.chosen_grip(j+1,150))
                sleep(5)
            print("expect red prompt")
            grip_list = grip_times(parse_csv(read_csv(CSV_functions.MUSICGLOVE)))
            user_stats = User_Stats()
            for i in range(7):
                seconds-=5
                self.update_csv(self.chosen_grip(1,300))
                for j in range(1,5):
                    self.update_csv(self.chosen_grip(j+1,150))
                sleep(5)
            print("expect Negative red response")
            grip_list = grip_times(parse_csv(read_csv(CSV_functions.MUSICGLOVE)))
            user_stats = User_Stats()
            for i in range(7):
                seconds-=5
                self.update_csv(self.chosen_grip(1,150))
                for j in range(1,5):
                    self.update_csv(self.chosen_grip(j+1,150))
                sleep(5)
            print("expect Positive red response")
            grip_list = grip_times(parse_csv(read_csv(CSV_functions.MUSICGLOVE)))
            user_stats = User_Stats()
            for i in range(7):
                seconds-=5
                self.update_csv(self.chosen_grip(1,1))
                for j in range(1,5):
                    self.update_csv(self.chosen_grip(j+1,150))
                sleep(5)
        print("2nd simulated song is over")

    def tester3(self) -> None:
        '''takes a predefined song file and adds it line by line to the log file'''
        temp_list = []
        with open('C:\\Users\\Nathan\\Desktop\\CalPlug\\RIVA\\musicglove3\\resources\\saves\\temp\\test.csv', 'r', newline='') as infile:
            csv_reader = csv.reader(infile, delimiter=',')
            for line in csv_reader:
                if line == '':
                    temp_list.append("new song")
                    continue
                else:
                    temp_list.append(line)
                    new_list = []
        print("Number of lines this song = ",len(temp_list))
        for i in range(len(temp_list)):
            self.write_csv(new_list, temp_list[i])
            new_list.append(temp_list[i])
            sleep(1)





if __name__ == "__main__":
    import CSV_functions
    from CSV_functions import read_csv
    from Interface import parse_csv, grip_times
    from time import sleep
    from user_stats import User_Stats
    with open(CSV_FILE, 'w', newline='') as outfile:
        outfile.write('')
    tester = N_test()
    tester.tester1()
    grip_list = grip_times(parse_csv(read_csv(CSV_functions.MUSICGLOVE)))
    user_stats = User_Stats()
    print("find_best_grip_scale = ",user_stats.find_best_grip_scale(grip_list))
    print("find_worst_grip_scale = ",user_stats.find_worst_grip_scale(grip_list))
    sleep(40)

    tester.tester2()
    sleep(40)

    tester.tester3()
