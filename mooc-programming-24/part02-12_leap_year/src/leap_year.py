# Write your solution here
year = int(input("Please type in a year: "))
isLeapYear = False

if year % 100 == 0:
    if year % 400 == 0:
        isLeapYear = True
    else:
        isLeapYear = False
elif year % 4 == 0:
    isLeapYear = True

if isLeapYear:
    print("That year is a leap year.")
else:
    print("That year is not a leap year.")