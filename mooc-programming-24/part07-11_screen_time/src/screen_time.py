from datetime import datetime, timedelta

filename = input('Filename: ')
# filename = 'late_june.txt'

start_date = input("Starting date in the format dd.mm.yyyy: ")
# start_date = '15.04.1992'

my_time = datetime.strptime(start_date, "%d.%m.%Y")

days = int(input('How many days: '))
# days = 5

print('Please type in screen time in minutes on each day (TV computer mobile):')

data = {}
total = 0
for i in range(days):
    new_time = my_time + timedelta(days=i)
    text = 'Screen time ' + new_time.strftime("%d.%m.%Y") + ' : '
    value = list(map(int, input(text).split(' ')))
    data[new_time.strftime("%d.%m.%Y")] = value
    total += sum(value)

# print(data)

with open(filename, 'w') as file:
    period = my_time.strftime("%d.%m.%Y") + '-' + (my_time + timedelta(days=days - 1)).strftime("%d.%m.%Y")
    file.write('Time period: ' + period + '\n')
    file.write('Total minutes: ' + str(total) + '\n')
    file.write('Average minutes: ' + str(total/days) + '\n')

    for key, value in data.items():
        line = '/'.join(str(i) for i in value)
        file.write(key + ': ' + line + '\n')

print(f"Data stored in file {file}")