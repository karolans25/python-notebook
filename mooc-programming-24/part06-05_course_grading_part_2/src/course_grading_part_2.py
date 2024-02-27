# write your solution here
student_info = input("Student information: ")
exercise_data = input("Exercises completed: ")
exam_points = input("Exam points: ")

# if False:
#     # this is never executed
#     student_info = input("Student information: ")
#     exercise_data = input("Exercises completed: ")
# else:
#     # hard-coded input
#     student_info = "students1.csv"
#     exercise_data = "exercises1.csv"
#     exam_points = "exam_points1.csv"

data = {}

with open(student_info) as students:
    for line in students:
        line = line.replace('\n', '').strip()
        temp = line.split(';')
        if temp[0] == 'id':
            continue
        if temp[0] not in data:
            data[temp[0]] = {}    
        data[temp[0]]['first'] = temp[1]
        data[temp[0]]['last'] = temp[2]
    
with open(exercise_data) as exercises:
    for line in exercises:
        line = line.replace('\n', '').strip()
        temp = line.split(';')
        if temp[0] == 'id':
            continue
        for i in range(1, len(temp)):
            temp[i] = int(temp[i])
        data[temp[0]]['exercises'] = temp[1:]

with open(exam_points) as points:
    for line in points:
        line = line.replace('\n', '').strip()
        temp = line.split(';')
        if temp[0] == 'id':
            continue
        for i in range(1, len(temp)):
            temp[i] = int(temp[i])
        data[temp[0]]['points'] = temp[1:]

for value in data.values():
    exercises_points = sum(value['exercises']) * 10 // 40
    exam_points = sum(value['points'])
    grade = exercises_points + exam_points
    if 0 <= grade <= 14:
        grade = 0
    elif 15 <= grade <= 17:
        grade = 1
    elif 18 <= grade <= 20:
        grade = 2
    elif 21 <= grade <= 23:
        grade = 3
    elif 24 <= grade <= 27:
        grade = 4
    elif 28 <= grade:
        grade = 5
        
    print(f"{value['first']} {value['last']} {grade}")
