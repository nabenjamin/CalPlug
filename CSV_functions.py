__author__ = 'Nathan'

import csv
MUSICGLOVE = 'Z:\\musicglove\\resources\\saves\\temp\\temp.csv'
CALPLUG = 'C:\\Users\\Nathan\\Desktop\\CalPlug\\temp.csv'

def read_csv(file_path: str) -> list:
    '''Read data from a .csv file, and return a namedtuple containing
       the actual and expected fingers, and the time difference from expected.
    '''
    print("entering read_csv")
    stat_list = []
    with open(file_path, 'r') as infile:

        for line in infile:
            temp_stat = line.strip().split(",")
            stat_list.append(temp_stat)
    return stat_list

def make_csv(stat_list: list):
    print("entering make_csv")
    with open('C:\\Users\\Nathan\\Desktop\\CalPlug\\temp.csv', 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',')
        for i in stat_list:
            spamwriter.writerow(i)

if __name__ == '__main__':
    print(read_csv(MUSICGLOVE))
