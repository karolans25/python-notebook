# Write your solution here
def seven_brothers():
    brothers = ["Simeoni", "Juhani", "Eero", "Lauri", "Aapo", "Tuomas", "Timo"]
    brothers.sort()
    for name in brothers:
        print(name)

# Write your main function within a block like this:
if __name__ == "__main__":
    seven_brothers()