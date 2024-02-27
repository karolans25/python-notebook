# Write your solution here
from random import shuffle, sample

def lottery_numbers(amount: int, lower: int, upper: int):
    temp = list(range(lower, upper + 1))
    return sorted(sample(temp, amount))

if __name__ == "__main__":
    for number in lottery_numbers(7, 1, 40):
        print(number)