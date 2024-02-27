# Write your solution here
from random import sample
from string import ascii_lowercase

def generate_password(amount: int, with_numbers: bool, with_special: bool):
    specials = "!?=+-()#"
    group = ascii_lowercase
    if with_numbers:
        group += 
    print(ascii_lowercase)
    letters = sample(ascii_lowercase, amount)
    return ''.join(letters)

if __name__ == "__main__":
    for i in range(10):
        print(generate_password(8, False, False))