# Write your solution here
letter_1 = input("1st letter: ")
letter_2 = input("2nd letter: ")
letter_3 = input("3rd letter: ")

middle_letter = letter_1

if (letter_1 > letter_2 and letter_3 < letter_2) or (letter_3 > letter_2 and letter_1 < letter_2):
    middle_letter = letter_2
elif (letter_1 > letter_3 and letter_2 < letter_3) or (letter_2 > letter_3 and letter_1 < letter_3):
    middle_letter = letter_3

print(f"The letter in the middle is {middle_letter}")
