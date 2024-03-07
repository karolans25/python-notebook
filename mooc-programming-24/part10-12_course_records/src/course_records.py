# tee ratkaisusi tänne
class Course:
    def __init__(self, name: str, grade: int, credit: int):
        if name == '':
            raise ValueError('Ten name can\'t be an empty string')
        if credit < 1:
            raise ValueError('The credits can\'t below 1')
        if not (1 <= grade <= 5):
            raise ValueError('The grade must be from 1 to 5')
        
        self.__name = name
        self.__grade = grade
        self.__credit = credit
    
    def name(self):
        return self.__name

    def grade(self):
        return self.__grade

    def credit(self):
        return self.__credit

    def edit_course(self, grade: int, credits: int):
        if grade > self.grade():
            self.__grade = grade
        self.__credits = credits

class CourseKeeper:
    def __init__(self):
        self.__courses = {}
        self.__total_credits = 0
        self.__mean = 0.0
    
    def add_course(self, name: str, grade: int, credit: int):
        if name in self.__courses.keys():
            self.__courses[name].edit_course(grade, credit)
        else:
            course = Course(name, grade, credit)
            self.__courses[name] = course

    def get_courses(self):
        return self.__courses

    def get_course_data(self, name: str):
        if name not in self.__courses:
            return None
        return self.__courses[name]

    def get_total_credits(self):
        if len(self.__courses.keys()) == 0:
            return 0
        return sum([self.__courses[name].credit() for name in self.__courses.keys()])

    def get_mean(self):
        if len(self.__courses.keys()) == 0:
            return 0.0
        ## Real form to calculate mean
        # partial_grades = sum([course.grade() * course.credit() for course in self.__courses.values()])
        # return round(partial_grades / self.get_total_credits() , 1)
        ## Way that the exercise wants
        partial_grades = sum([course.grade() for course in self.__courses.values()])
        return round(partial_grades / len(self.get_courses()) , 1)

    def get_grade_distribution(self):
        res = [0]*5
        for course in self.__courses.values():
            res[course.grade() - 1] += 1
        return res

class CourseKeeperApp:
    def __init__(self):
        self.__coursekeeper = CourseKeeper()

    def help(self):
        print("1 add course")
        print("2 get course data")
        print("3 statistics")
        print("0 exit")

    def add_course(self):
        name = input('name: ')
        grade = int(input('grade: '))
        credit = int(input('credits: '))
        self.__coursekeeper.add_course(name, grade, credit)

    def get_course_data(self):
        name = input('name: ')
        course = self.__coursekeeper.get_course_data(name)
        if course == None:
            print('no entry for this course')
        else:
            print(f"{course.name()} ({course.credit()} cr) grade {course.grade()}")

    def get_statistics(self):
        courses = self.__coursekeeper.get_courses()
        distribution = self.__coursekeeper.get_grade_distribution()
        print(f"{len(courses)} completed courses, a total of {self.__coursekeeper.get_total_credits()} credits")
        print(f"mean {self.__coursekeeper.get_mean()}")
        print('grade distribution')
        for i in range(len(distribution), 0, -1):
            print(f"{i}: {'x'*distribution[i - 1]}")

    def execute(self):
        self.help()
        while True:
            print("")
            command = input("command: ")
            if command == "0":
                break
            elif command == "1":
                self.add_course()
            elif command == "2":
                self.get_course_data()
            elif command == "3":
                self.get_statistics()
            else:
                self.help()


app = CourseKeeperApp()
app.execute()
# keeper = CourseKeeper()
# print(keeper.get_courses())
# print(keeper.get_total_credits())
# print(keeper.get_mean())
# keeper.add_course('ltp', 3, 5)
# keeper.add_course('java', 4, 4)
# keeper.add_course('ltp', 5, 5)
# keeper.add_course('ltp', 1, 5)
# keeper.add_course('IA', 5, 3)
# keeper.add_course('machine laerning', 5, 2)
# for course in keeper.get_courses().values():
#     print(course.name(), course.grade(), course.credit())
# print(keeper.get_total_credits())
# print(keeper.get_mean())
# print(keeper.get_grade_distribution())