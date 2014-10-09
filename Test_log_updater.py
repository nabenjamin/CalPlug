__author__ = 'Nathan'

import csv
from random import randrange
from time import sleep

CSV_FILE = 'Z:\\musicglove\\resources\\saves\\temp\\temp.csv'
#CSV_FILE = 'C:\\Users\\Nathan\\Desktop\\CalPlug\\temp.csv'

def new_grip(number_of_grips):
    """ Generates a random line for the MGlove log file (assuming correct grips)
    """
    grip = randrange(1,number_of_grips+1)
    timing = randrange(-300000,300000)
    if timing != 0:
        timing = timing/1000
    #        1,1,-58.823999999999614
    return [grip, grip, timing]

def update_csv(new_grip):
    """ Adds a new line to the CSV File.
    """
    temp_list = []
    #print("opening")
    with open(CSV_FILE, 'r', newline='') as infile:
        csv_reader = csv.reader(infile, delimiter=',')
        for line in csv_reader:
            temp_list.append(line)
    #print("writing")
    with open(CSV_FILE, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile, delimiter=',')
        for newline in temp_list:
            csv_writer.writerow(newline)
        csv_writer.writerow(new_grip)
    #print("returning")
    return

def tester() -> None:
    """Updates log file to simulate user interaction with MGlove
    """
    grip_number = input("how many grips should be used in the test? (1-5): ")
    while grip_number not in range(1,6): #really 1-5, range is exclusive...
        try:
            grip_number = int(grip_number)
        except ValueError:
            grip_number = input("number must be between 1 and 5: ")
            pass
    seconds = input("how many seconds should simulation last? ")
    while type(seconds) != int:
        try:
            seconds = int(seconds)
        except:
            seconds = input("seconds must be a whole number")
            pass
    for i in range(seconds):
        #print("entering sleep")
        sleep(1)
        update_csv(new_grip(grip_number))


if __name__ == "__main__":
    with open(CSV_FILE, 'w', newline='') as outfile:
        outfile.write('')
    tester()