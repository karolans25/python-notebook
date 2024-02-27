# write your solution here
student_info = input("Student information: ")
exercise_data = input("Exercises completed: ")

# if False:
#     # this is never executed
#     student_info = input("Student information: ")
#     exercise_data = input("Exercises completed: ")
# else:
#     # hard-coded input
#     student_info = "students1.csv"
#     exercise_data = "exercises1.csv"

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

for value in data.values():
    print(f"{value['first']} {value['last']} {sum(value['exercises'])}")

