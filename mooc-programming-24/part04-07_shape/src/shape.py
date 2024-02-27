# Copy here code of line function from previous exercise and use it in your solution
def line(times, text):
    character = '*'
    if text != '':
        character = text[0]
    print(times * character)

def triangle(size, character):
    count = 1
    while count <= size:
        line(count, character)
        count += 1

def rectangle(size_x, size_y, character):
    count = size_y
    while count > 0:
        line(size_x, character)
        count -= 1

def shape(width, triangle_character, height, rectangle_character):
    triangle(width, triangle_character)
    rectangle(width, height, rectangle_character)

# You can test your function by calling it within the following block
if __name__ == "__main__":
    shape(5, "X", 3, "*")