from functools import reduce

class CourseAttempt:
    def __init__(self, course_name: str, grade: int, credits: int):
        self.course_name = course_name
        self.grade = grade
        self.credits = credits

    def __str__(self):
        return f"{self.course_name} ({self.credits} cr) grade {self.grade}"


def sum_of_all_credits(attempts: list):
    return reduce(lambda total, x: total + x.credits, attempts, 0)

def sum_of_passed_credits(attempts: list):
    return reduce(lambda total, x: total + x.credits, filter(lambda y: y.grade >= 1, attempts), 0)

def average(attempts: list):
    passed = list( filter(lambda y: y.grade >= 1, attempts) )
    return round( reduce(lambda total, x: total + x.grade, passed, 0) / len(passed) , 1)


if __name__ == "__main__":
    # #Part 1
    # s1 = CourseAttempt("Introduction to Programming", 5, 5)
    # s2 = CourseAttempt("Advanced Course in Programming", 4, 5)
    # s3 = CourseAttempt("Data Structures and Algorithms", 3, 10)
    # credit_sum = sum_of_all_credits([s1, s2, s3])
    # print(credit_sum)

    # #part 2
    # s1 = CourseAttempt("Introduction to Programming", 5, 5)
    # s2 = CourseAttempt("Advanced Course in Programming", 0, 4)
    # s3 = CourseAttempt("Data Structures and Algorithms", 3, 10)
    # credit_sum = sum_of_passed_credits([s1, s2, s3])
    # print(credit_sum)

    # #Part 3
    s1 = CourseAttempt("Introduction to Programming", 5, 5)
    s2 = CourseAttempt("Advanced Course in Programming", 0, 4)
    s3 = CourseAttempt("Data Structures and Algorithms", 3, 10)
    ag = average([s1, s2, s3])
    print(ag)