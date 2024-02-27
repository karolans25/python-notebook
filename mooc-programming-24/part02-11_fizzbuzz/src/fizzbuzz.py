# Write your solution here
number = int(input("Number: "))
result = ''

if number % 3 == 0:
    result += 'Fizz'
if number % 5 == 0:
    result += 'Buzz'

print(result)