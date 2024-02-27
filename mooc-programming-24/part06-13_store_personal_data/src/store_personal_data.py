# Write your solution here
def store_personal_data(person: tuple):
    with open("people.csv", "a") as store:
        store.write(f"{person[0]};")
        store.write(f"{person[1]};")
        store.write(f"{person[2]}\n")

if __name__ == "__main__":
    store_personal_data(("Paul Paulson", 37, 175.5))