import os
from datetime import datetime
import argparse
import pathlib

def funkcja():
    parser = argparse.ArgumentParser()
    parser.add_argument("-cls", "--calendars", help="Relative path to calendars")
    parser.add_argument("-dim", "--duration-in-minutes", help="Minimal required duration in minutes",type=int)
    parser.add_argument("-mp", "--minimum-people", help="Minimal required number of available people",type=int)
    args = parser.parse_args()
    cur_path = pathlib.Path().resolve()
    sciezka = os.path.join(cur_path,args.calendars)
    dur_in_min = args.duration_in_minutes
    datetime_format = "%Y-%m-%d %H:%M:%S"
    que = []
    people_num = 0
    min_people = args.minimum_people
    for filename in os.listdir(sciezka):
        people_num += 1
        with open(os.path.join(sciezka, filename), 'r') as f:
            lines = f.read().splitlines()
            for line in lines:
                line_split = line.split(" ")
                if len(line_split) == 1:
                    date1 = line_split[0] + " 00:00:00"
                    date2 = line_split[0] + " 23:59:59"
                else:
                    date1 = line_split[0] + " " + line_split[1]
                    date2 = line_split[3] + " " + line_split[4]
                que.append((datetime.strptime(date1, datetime_format), "s"))
                que.append((datetime.strptime(date2, datetime_format), "e"))
    que.sort(key=lambda x: x[0])
    counter = people_num
    if dur_in_min == 0:
        return que[0][0]
    for i, s in enumerate(que):
        if s[1] == "s":
            counter -= 1
        else:
            counter += 1
        if counter >= min_people:
            diff = s[0]-que[i-1][0]
            if diff.total_seconds()/60 >= dur_in_min:
                return que[i-1][0]
    return que[-1][0]


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(funkcja())







# See PyCharm help at https://www.jetbrains.com/help/pycharm/
