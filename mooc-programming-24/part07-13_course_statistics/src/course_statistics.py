# Write your solution here
import urllib.request
import json
from math import floor

def retrieve_all():
    link = 'https://studies.cs.helsinki.fi/stats-mock/api/courses'
    my_request = urllib.request.urlopen(link)
    data = json.loads(my_request.read())
    res = []
    for course in data:
        if course['enabled']:
            answer = (course['fullName'], course['name'], course['year'], sum(course['exercises']))
            res.append(answer)
    return res

def retrieve_course(course_name: str):
    link = 'https://studies.cs.helsinki.fi/stats-mock/api/courses/' + course_name + '/stats'
    my_request = urllib.request.urlopen(link)
    data = json.loads(my_request.read())
    
    max_students = 0
    hours = 0
    exercises = 0
    for key in data:
        if data[key]['students'] > max_students:
            max_students = data[key]['students']
        hours += data[key]['hour_total']
        exercises += data[key]['exercise_total']

    res = {}
    res['weeks'] = len(data)
    res['students'] = max_students
    res['hours'] = hours
    res['hours_average'] = floor(hours / max_students)
    res['exercises'] = exercises
    res['exercises_average'] = floor(exercises / max_students)
    return res

if __name__ == '__main__':
    # print(retrieve_all())
    print(retrieve_course('docker2019'))