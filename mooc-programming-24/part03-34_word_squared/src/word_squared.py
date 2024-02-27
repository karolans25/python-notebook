# Write your solution here
def squared(text, number):
    result = (number // len(text) + 1) * number * text
    
    count = number
    while count > 0:
        print(result[:number])
        result = result[number:]
        count -= 1

# Testing the function
if __name__ == "__main__":
    squared("ab", 3)
    print()
    squared("aybabtu", 5)