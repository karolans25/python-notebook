# Write your solution here
hourly_wage = float(input("Hourly wage: "))
hours_worked = float(input("Hours worked: "))
day = input("Day of the week: ")

result = hourly_wage * hours_worked

if day == 'Sunday':
    result *= 2

print (f"Daily wages: {result} euros")