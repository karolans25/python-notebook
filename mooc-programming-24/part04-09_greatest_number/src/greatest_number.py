# Write your solution here
# You can test your function by calling it within the following block
def greatest_number(num_1, num_2, num_3):
    numbers = [num_1, num_2, num_3]
    numbers.sort()
    return numbers[2]

if __name__ == "__main__":
    greatest = greatest_number(5, 4, 8)
    print(greatest)