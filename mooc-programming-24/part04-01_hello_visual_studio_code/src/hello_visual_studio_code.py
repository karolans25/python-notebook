# Write your solution here
MY_STRING = "Visual Studio CODE"

editor = ''

while editor.lower() != MY_STRING.lower():
    editor = input("Editor: ")

    if editor.lower() == MY_STRING.lower():
        print("an excellent choice!")
    elif editor.lower() == 'notepad' or editor.lower() == 'word':
        print("awful")
    else:
        print("not good")