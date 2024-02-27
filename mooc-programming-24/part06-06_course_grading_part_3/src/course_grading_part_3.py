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

# Read student file
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
    
# Read excersise file
with open(exercise_data) as exercises:
    for line in exercises:
        line = line.replace('\n', '').strip()
        temp = line.split(';')
        if temp[0] == 'id':
            continue
        for i in range(1, len(temp)):
            temp[i] = int(temp[i])
        data[temp[0]]['exercises'] = temp[1:]

# Read exam file
with open(exam_points) as points:
    for line in points:
        line = line.replace('\n', '').strip()
        temp = line.split(';')
        if temp[0] == 'id':
            continue
        for i in range(1, len(temp)):
            temp[i] = int(temp[i])
        data[temp[0]]['points'] = temp[1:]

# Headers
header = ['name', 'exec_nbr', 'exec_pts.', 'exm_pts.', 'tot_pts.', 'grade']
for i in range(len(header)):
    if i == 0:
        print(f"{header[i]:<30}", end='')
    else:
        print(f"{header[i]:<10}", end='')
print()

# print(f"{value['first']} {value['last']:30} ", end='' )
# print(f"{exec_value:10} {exec_pts:10} {exam_pts:10} {total_pts:10} {grade:10}")

for value in data.values():
    exec_value = sum(value['exercises'])
    exec_pts = exec_value * 10 // 40
    exam_pts = sum(value['points'])
    total_pts = exec_pts + exam_pts
    grade = 0
    if 0 <= total_pts <= 14:
        grade = 0
    elif 15 <= total_pts <= 17:
        grade = 1
    elif 18 <= total_pts <= 20:
        grade = 2
    elif 21 <= total_pts <= 23:
        grade = 3
    elif 24 <= total_pts <= 27:
        grade = 4
    elif 28 <= total_pts:
        grade = 5
        
    name = value['first'] + ' ' + value['last']
    print(f"{name:<30}", end='' )
    print(f"{exec_value:<10}{exec_pts:<10}{exam_pts:<10}{total_pts:<10}{grade:<10}")
