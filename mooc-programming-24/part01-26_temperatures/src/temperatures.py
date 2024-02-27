# Write your solution here
farenheits = int(input("Please type in a temperature (F): "))
celcius = (farenheits - 32)*5/9
print(f"{farenheits} degrees Fahrenheit equals {celcius} degrees Celsius")

if celcius < 0:
    print("Brr! It's cold in here!")