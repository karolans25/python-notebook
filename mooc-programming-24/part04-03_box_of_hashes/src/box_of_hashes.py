# Copy here code of line function from previous exercise
def line(times, text):
    character = '*'
    if text != '':
        character = text[0]
    print(times*character)


def box_of_hashes(height):
    count = height
    while count > 0:
        line(10, "#")
        count -= 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    box_of_hashes(5)
