# Write your solution here
from string import ascii_uppercase as upper, ascii_lowercase as lower, digits as dig

def print_action(data: list, var: dict) -> str:
    # PRINT [value]: prints the value
    printed = var.get(data[0]) if var.get(data[0]) != None else data[0]
    print(printed)
    return printed

def mov_action(data: list, var: dict):
    # MOV [variable] [value]: assigns the value to the variable
    var[data[0]] = int(data[1])

def add_action(data: list, var:dict):
    # ADD [variable] [value]: adds the value to the variable
    if var.get(data[0]) != None:
        if var.get(data[1]) != None:
            var[data[0]] += var[data[1]]
        else:
            var[data[0]] += int(data[1])

def sub_action(data: list, var:dict):
    # SUB [variable] [value]: subtracts the value from the variable
    if var.get(data[0]) != None:
        if var.get(data[1]) != None:
            var[data[0]] -= var[data[1]]
        else:
            var[data[0]] -= int(data[1])

def mul_action(data, var):
    # MUL [variable] [value]: multiplies the variable by the value
    if var.get(data[0]) != None:
        if var.get(data[1]) != None:
            var[data[0]] *= var[data[1]]
        else:
            var[data[0]] *= int(data[1])

def add_location_action(action, var):
    # [location]:: names a line of code, so it can be jumped to from elsewhere
    for i in action[:-1]:
        if i not in lower and i not in dig:
            break
    else:
        var[action] = ''
    print('---------')

def if_action(data, var):
    # IF [condition] JUMP [location]: if the condition is true, jump to the location specified
    comparisson = ['==', '!=', '<', '<=', '>', '>=']
    if data[1] in comparisson:
        exp = str(var.get(data[0])) + data[1] + str(var.get(data[2]))
        print(data[4])
        if eval(exp):
            print('TRUE')
        else:
            print('FALSE')

def run(*the_args: tuple):
    # JUMP [location]: jumps to the location specified
    # END: finish execution
    var = {}
    for letter in upper:
        var[letter] = 0
    # print(var)
    result = []

    steps = the_args[0]
    for line in steps:
        train, *data = line.split()
        print(train, data)
        if train == 'PRINT' and len(data) == 1:
            result.append(print_action(data, var))
        elif train == 'MOV' and len(data) == 2:
            mov_action(data, var)
        elif train == 'ADD' and len(data) == 2:
            add_action(data, var)
        elif train == 'SUB' and len(data) == 2:
            sub_action(data, var)
        elif train == 'MUL' and len(data) == 2:
            mul_action(data, var)
        elif train.endswith(':') and len(data) == 0:
            add_location_action(train, var)
        elif train == 'JUMP':
            pass
        elif train == 'IF':
            if_action(data, var)
        elif train == 'END':
            break
    
    print(var)

    return result

if __name__ == '__main__':
    # program1 = []
    # program1.append("MOV A 1")
    # program1.append("MOV B 2")
    # program1.append("PRINT A")
    # program1.append("PRINT B")
    # program1.append("ADD A B")
    # program1.append("PRINT A")
    # program1.append("END")
    # print(program1)
    # result = run(program1)
    # print(result)

    program2 = []
    program2.append("MOV A 1")
    program2.append("MOV B 10")
    program2.append("begin:")
    program2.append("IF A >= B JUMP quit")
    program2.append("PRINT A")
    program2.append("PRINT B")
    program2.append("ADD A 1")
    program2.append("SUB B 1")
    program2.append("JUMP begin")
    program2.append("quit:")
    program2.append("END")
    result = run(program2)
    print(result)