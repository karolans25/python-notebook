# Write your solution here
while True:
    print("1 - add an entry, 2 - read entries, 0 - quit")
    opt = int(input("Function: "))
    if opt == 0:
        break
    if opt == 1:
        entry = input("Diary entry: ")
        with open("diary.txt", "a") as file:
            file.write(f"{entry}\n")
        print("Diary saved")
    if opt == 2:
        print("Entries: ")
        with open("diary.txt") as file:
            for line in file:
                print(line.replace('\n', ''))

print("Bye now!")