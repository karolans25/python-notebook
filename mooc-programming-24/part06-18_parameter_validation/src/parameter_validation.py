# Write your solution here
def new_person(name: str, age: int):
    if name == '' or len(name.split(' ')) < 2 or len(name) > 40:
        raise ValueError("Invalid argument value for name: " + name)
    if not 0 < age < 150:
        raise ValueError("Invalid argument value for age:" + str(age))
    return (name, age)

if __name__ == "__main__":
    name = 'carolina rosa'
    age = 15
    print(new_person(name, age))