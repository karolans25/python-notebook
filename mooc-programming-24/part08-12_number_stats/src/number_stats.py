# Write your solution here!
class  NumberStats:
    def __init__(self):
        self.numbers = []

    def add_number(self, number:int):
        self.numbers.append(number)

    def count_numbers(self):
        return len(self.numbers)

    def get_sum(self):
        if len(self.numbers) > 0:
            return sum(self.numbers)
        else:
            return 0
    
    def average(self):
        if len(self.numbers) > 0:
            return self.get_sum() / self.count_numbers()
        else:
            return 0.0


## Part 1
# stats = NumberStats()
# stats.add_number(3)
# stats.add_number(5)
# stats.add_number(1)
# stats.add_number(2)
# print("Numbers added:", stats.count_numbers())

## Part 2
# stats = NumberStats()
# stats.add_number(3)
# stats.add_number(5)
# stats.add_number(1)
# stats.add_number(2)
# print("Numbers added:", stats.count_numbers())
# print("Sum of numbers:", stats.get_sum())
# print("Mean of numbers:", stats.average())

## Part 3
# stats = NumberStats()
# print('Please type in integer numbers:')
# while True:
#     temp = int( input() )
#     if temp == -1:
#       break
#     stats.add_number(temp)

# if stats.count_numbers() > 0:
#     print(f"Sum of numbers: {stats.get_sum()}")
#     print(f"Mean of numbers: {stats.average()}")

## Part 4
all_stats = NumberStats()
even_stats = NumberStats()
odd_stats = NumberStats()

print('Please type in integer numbers:')
while True:
    temp = int( input() )
    if temp == -1:
        break

    all_stats.add_number(temp)
    if temp % 2 == 1:
        odd_stats.add_number(temp)
    else:
        even_stats.add_number(temp)

if all_stats.count_numbers() > 0:
    print(f"Sum of numbers: {all_stats.get_sum()}")
    print(f"Mean of numbers: {all_stats.average()}")
    print(f"Sum of even numbers: {even_stats.get_sum()}")
    print(f"Sum of odd numbers: {odd_stats.get_sum()}")
