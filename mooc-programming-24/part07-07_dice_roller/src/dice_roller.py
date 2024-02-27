# Write your solution here
def roll(die: str):

def play(die1: str, die2: str, times: int):
    # Die A has the sides 3, 3, 3, 3, 3, 6
    # Die B has the sides 2, 2, 2, 5, 5, 5
    # Die C has the sides 1, 4, 4, 4, 4, 4
    print(die1, die2, times)

if __name__ == "__main__":
    for i in range(20):
        print(roll("A"), " ", end="")
    print()
    for i in range(20):
        print(roll("B"), " ", end="")
    print()
    for i in range(20):
        print(roll("C"), " ", end="")
    
    result = play("A", "C", 1000)
    print(result)
    result = play("B", "B", 1000)
    print(result)