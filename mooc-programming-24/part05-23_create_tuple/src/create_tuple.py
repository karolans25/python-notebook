# Write your solution here
def create_tuple(x: int, y: int, z: int):
    minimum = min([x, y, z])
    maximum = max([x, y, z])

    sum = x + y + z
    
    return (minimum, maximum, sum)

if __name__ == "__main__":
    print(create_tuple(5, 3, -1))