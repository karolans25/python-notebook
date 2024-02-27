# Write your solution here
number = int(input("Upper limit: "))
exp = 0

while 2**exp <= number:
    print(2**exp)
    exp += 1
