# Write your solution here
year = int(input("Year: "))
next_leap_year = year + 1

while True:
    if next_leap_year % 100 == 0:
        if next_leap_year % 400 == 0 :
            break
    elif next_leap_year % 4 == 0:
        break
    next_leap_year += 1

print(f"The next leap year after {year} is {next_leap_year}")