# Write your solution here
def read_input(text: str, down: int, up: int):
    while True:
        try:
            input_str = input(text)
            number = int(input_str)
            if down <= number <= up:
                return number
            else:
                print(f"You must type in an integer between {down} and {up}")
        except ValueError:
            print(f"You must type in an integer between {down} and {up}")

number = read_input("Please type in a number: ", 5, 10)
print("You typed in:", number)
