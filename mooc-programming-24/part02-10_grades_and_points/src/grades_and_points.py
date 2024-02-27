# Write your solution here
points = int(input("How many points [0-100]: "))
grade = 'impossible!'

if 0 <= points <= 49: 
    grade = 'fail'
elif 50 <= points <= 59: 
    grade = 1
elif 60 <= points <= 69: 
    grade = 2
elif 70 <= points <= 79: 
    grade = 3
elif 80 <= points <= 89: 
    grade = 4
elif 90 <= points <= 100: 
    grade = 5

print(f"Grade: {grade}")