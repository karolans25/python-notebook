# Write your solution here
def add_student(students_dic: dict, name: str):
    students_dic[name] = {}

def add_course(students_dic: dict, name: str, course: tuple):
    dic_courses = students_dic[name]
    if course[0] in dic_courses.keys():
        if course[1] > dic_courses[course[0]]:
            dic_courses[course[0]] = course[1]
    elif course[1] > 0:
        students_dic[name][course[0]] = course[1]

def get_num_courses_completed(student_dic: dict):
    return len(student_dic.keys())

def get_average_grade(student_dic: dict):
    sum = 0
    for value in student_dic.values():
        sum += value
    return sum / len(student_dic.keys())

def most_courses_completed(students_dic: dict):
    most = 0
    most_name = ''
    for name in students_dic.keys():
        num_courses = len(students_dic[name].keys())
        if num_courses > most:
            most = num_courses
            most_name = name
    return most, most_name

def best_average_grade(students_dic: dict):
    best = 0
    best_name = ''
    for name in students_dic.keys():
        average_grade = get_average_grade(students_dic[name])
        if average_grade > best:
            best = average_grade
            best_name = name
    return best, best_name

def print_data_courses(student_dic: dict):
    for key, value in student_dic.items():
        print(f"  {key} {value}")

def print_student(students_dic: dict, name: str):
    if name in students_dic:
        print(f"{name}:")
        num_courses = get_num_courses_completed(students_dic[name])
        if num_courses > 0:
            average_grade = get_average_grade(students_dic[name])
            print(f" {num_courses} completed courses:")
            print_data_courses(students_dic[name])
            print(f" average grade {average_grade}")
        else: 
            print(f" no completed courses")
    else:
        print(f"{name}: no such person in the database")

def summary(students_dic: dict):
    print(f"students {len(students_dic.keys())}")
    most, most_name = most_courses_completed(students_dic)
    print(f"most courses completed {most} {most_name}")
    best, best_name = best_average_grade(students_dic)
    print(f"best average grade {best} {best_name}")

if __name__ == "__main__":
    # #Part 1:
    # students = {}
    # add_student(students, "Peter")
    # add_student(students, "Eliza")
    # print_student(students, "Peter")
    # print_student(students, "Eliza")
    # print_student(students, "Jack")
    
    # #Part2:
    # students = {}
    # add_student(students, "Peter")
    # add_course(students, "Peter", ("Introduction to Programming", 3))
    # add_course(students, "Peter", ("Advanced Course in Programming", 2))
    # print_student(students, "Peter")

    # #Part3:
    # students = {}
    # add_student(students, "Peter")
    # add_course(students, "Peter", ("Introduction to Programming", 3))
    # add_course(students, "Peter", ("Advanced Course in Programming", 2))
    # add_course(students, "Peter", ("Data Structures and Algorithms", 0))
    # add_course(students, "Peter", ("Introduction to Programming", 2))
    # print_student(students, "Peter")

    #Part4:
    students = {}
    add_student(students, "Peter")
    add_student(students, "Eliza")
    add_course(students, "Peter", ("Data Structures and Algorithms", 1))
    add_course(students, "Peter", ("Introduction to Programming", 1))
    add_course(students, "Peter", ("Advanced Course in Programming", 1))
    add_course(students, "Eliza", ("Introduction to Programming", 5))
    add_course(students, "Eliza", ("Introduction to Computer Science", 4))
    summary(students)