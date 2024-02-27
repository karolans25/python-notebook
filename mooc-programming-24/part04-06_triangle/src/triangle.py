# Copy here code of line function from previous exercise
def line(times, text):
    character = '*'
    if text != '':
        character = text[0]
    print(times * character)

def triangle(size):
    count = 1
    while count <= size:
        line(count, '#')
        count += 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    triangle(5)
