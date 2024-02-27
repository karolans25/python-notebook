# Write your solution here
import csv
from datetime import datetime

def cheaters():
    cheaters = []
    students = {}
    year = 2000
    month = 1
    day = 1

    with open('start_times.csv') as file:
        for line in csv.reader(file, delimiter=';'):
            H, M = line[1].split(':')
            if line[0] not in students.keys():
                students[line[0]] = {
                    'start': datetime( year, month, day, int(H), int(M) ),
                    'tasks': {}
                }

    with open('submissions.csv') as file:
        for line in csv.reader(file, delimiter=';'):

            student = students[line[0]]
            
            H, M = line[3].split(':')
            end_time = datetime( year, month, day, int(H), int(M) )

            if line[1] not in student['tasks'].keys():
                student['tasks'][line[1]] = {
                    'points': line[2],
                    'end': end_time
                }
            elif student['tasks'][line[1]]['end'] < end_time:
                student['tasks'][line[1]] = {
                    'points': line[2],
                    'end': end_time
                }

    for key in students:
        student = students[key]
        for task in student['tasks'].keys():
            elapsed = student['tasks'][task]['end'] - students[key]['start']
            if elapsed.seconds/3600 > 3 and key not in cheaters:
                cheaters.append(key)

    return cheaters

if __name__ == '__main__':
    print(cheaters())