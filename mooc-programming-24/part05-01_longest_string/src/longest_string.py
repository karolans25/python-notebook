# Write your solution here
def longest(strings: list):
    longer = ''
    for i in strings:
        if len(i) > len(longer):
            longer = i
    return longer

if __name__ == "__main__":
    strings = ["hi", "hiya", "hello", "howdydoody", "hi there"]
    print(longest(strings))