# Write your solution here
number = int(input("Upper limit: "))
base = int(input("Base: "))
exp = 0

while base**exp <= number:
    print(base**exp)
    exp += 1
