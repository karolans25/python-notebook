# Write your solution here
def search_by_name(filename: str, word: str):
    recipies = []
    
    with open(filename) as new_file:
        all_recipies = new_file.read().split('\n\n')
        for i in all_recipies:
            lines = i.split('\n')
            if lines[0].lower().find(word.lower()) != -1:
                recipies.append(lines[0])
    return recipies

def search_by_time(filename: str, prep_time: int):
    recipies = []
    
    with open(filename) as new_file:
        all_recipies = new_file.read().split('\n\n')
        for i in all_recipies:
            lines = i.split('\n')
            if int(lines[1]) <= prep_time:
                recipies.append(f"{lines[0]}, preparation time {lines[1]} min")
    return recipies

def search_by_ingredient(filename: str, ingredient: str):
    recipies = []
    
    with open(filename) as new_file:
        all_recipies = new_file.read().split('\n\n')
        for i in all_recipies:
            lines = i.split('\n')
            if ingredient in lines[2:]:
                recipies.append(f"{lines[0]}, preparation time {lines[1]} min")
    return recipies

if __name__ == "__main__":
    found_recipes = search_by_name("recipes1.txt", "cake")
    print(found_recipes)

    found_recipes = search_by_time("recipes1.txt", 20)
    print(found_recipes)

    found_recipes = search_by_ingredient("recipes1.txt", "eggs")
    print(found_recipes)
