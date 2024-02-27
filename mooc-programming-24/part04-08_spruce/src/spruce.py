# Write your solution here
def spruce(number):
    print("a spruce!")
    count = 1
    while count <= number:
        spaces = (number - count) * ' '
        starts = (2 * count - 1) * '*'
        print(spaces + starts)
        count += 1
    print((number - 1) * ' ' + '*')

# You can test your function by calling it within the following block
if __name__ == "__main__":
    spruce(5)