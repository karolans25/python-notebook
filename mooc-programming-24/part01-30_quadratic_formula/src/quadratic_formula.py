# Write your solution here
# Let's take the square root of math-module in use
from math import sqrt

# Note that the square root can also be calculated using power.
# sqrt(9) is equivalent to 9 ** 0.5
a = int(input("Value of a: "))
b = int(input("Value of b: "))
c = int(input("Value of c: "))

discriminant = sqrt(b**2 - 4*a*c)

root_1 = (-1 * b + discriminant) / (2 * a)
root_2 = (-1 * b - discriminant) / (2 * a)

print(f"\nThe roots are {root_1} and {root_2}")