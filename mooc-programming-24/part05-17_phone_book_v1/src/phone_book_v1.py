# Write your solution here
def search(dictionary: dict):
    name = input("name: ")   
    if name in dictionary:
        print(dictionary[name])
    else:
        print('no number')
    
def add(dictionary: dict):
    name = input("name: ")
    number = input("number: ")
    dictionary[name] = number
    print('ok!')

def main():
    dictionary = {}
    while True:
        option = int(input("command (1 search, 2 add, 3 quit): "))
        if option == 1:
            search(dictionary)
        if option == 2:
            add(dictionary)
        if option == 3:
            break
    print('quitting...')

main()