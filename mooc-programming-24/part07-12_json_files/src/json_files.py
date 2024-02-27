# Write your solution here
import json

def print_persons(filename: str):
    with open(filename) as file:
        data = file.read()

    students = json.loads(data)
    for student in students:
        name = student['name']
        age = student['age']
        hobbies = ', '.join(student['hobbies'])
        print(f"{name} {age} years ({hobbies})")

if __name__ == '__main__':
    print_persons('./file1.json')
    print()
    print_persons('./file2.json')
    print()
    print_persons('./file3.json')
    print()
    print_persons('./file4.json')
