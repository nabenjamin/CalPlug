__author__ = 'Nathan'

import csv
MUSICGLOVE = 'Z:\\musicglove\\resources\\saves\\temp\\temp.csv'
CALPLUG = 'C:\\Users\\Nathan\\Desktop\\CalPlug\\temp.csv'

def read_csv(file_path: str) -> list:
    '''Read data from a .csv file, and return a list containing
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
    ''' Takes a list of stats and/or strings and writes them into .csv file format
    '''
    print("entering make_csv")
    with open('C:\\Users\\Nathan\\Desktop\\CalPlug\\temp.csv', 'w', newline='') as csvfile:
        for i in stat_list:
            print('i = ', i)
            csv_writer = csv.writer(csvfile, delimiter=',')
            if type(i) is str:
                csv_writer.writerow([i])
                csv_writer.writerow([])
            else:
                csv_writer.writerow(i)


if __name__ == '__main__':
    test_result = ['Red Grip avg: 22.563200000001142; Blue Grip avg: 32.978142857142494;Green Grip avg: 27.25257142857195; Purple Grip avg: 60.543199999996794; Yellow Grip avg: 0',
                   'You have improved a lot! I noticed that you were having a little trouble with the Purple Grip',
                   'Red Grip avg: 27.56714285715134; Blue Grip avg: 20.77307692311073;Green Grip avg: 23.33925494792493; Purple Grip avg: 19.787199999965377; Yellow Grip avg: 0',
                   'Keep up the good work! We could still do a little more work on the Red Grip',
                   'Red Grip avg: 20.37581818212427; Blue Grip avg: 28.34021052646935;Green Grip avg: 42.730400000229324; Purple Grip avg: 21.73633333367373; Yellow Grip avg: 0',
                   'You are doing very well! On this next set lets try focusing on the Purple Grip You seemed most proficient with the Yellow Grip!']
    make_csv(test_result)
    print(read_csv(MUSICGLOVE))

