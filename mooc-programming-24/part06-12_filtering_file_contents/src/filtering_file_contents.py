# Write your solution here
def filter_solutions():
    with open("solutions.csv") as data, open("correct.csv", "w") as correct_file, open("incorrect.csv", "w") as incorrect_file:
        for line in data:           
            name, calc, result = line.strip().replace('\n', '').split(';')
            if '+' in calc:
                nums = calc.split('+')
                is_correct = int(nums[0]) + int(nums[1]) == int(result)
            elif '-' in calc:
                nums = calc.split('-')
                is_correct = int(nums[0]) - int(nums[1]) == int(result)
            else:
                continue

            if is_correct:
                correct_file.write(line)
            else:
                incorrect_file.write(line)

if __name__ == "__main__":
    filter_solutions()