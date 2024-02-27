# Copy here code of line function from previous exercise
def line(times, text):
    character = '*'
    if text != '':
        character = text[0]
    print(times * character)

def square_of_hashes(size):
    count = size
    while count > 0:
        line(size, "#")
        count -= 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    square_of_hashes(5)
