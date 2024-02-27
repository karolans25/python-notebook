# Write your solution here
def line(times, text):
    character = '*'
    if text != '':
        character = text[0]
    print(times*character)

# You can test your function by calling it within the following block
if __name__ == "__main__":
    line(5, "x")