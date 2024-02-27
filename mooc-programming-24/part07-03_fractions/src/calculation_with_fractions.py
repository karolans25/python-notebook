# Write your solution here
from fractions import Fraction

def fractionate(amount: int):
    result = Fraction(1, amount)
    return [result] * amount

if __name__ == "__main__":
    for p in fractionate(3):
        print(p)

    print()

    print(fractionate(5))