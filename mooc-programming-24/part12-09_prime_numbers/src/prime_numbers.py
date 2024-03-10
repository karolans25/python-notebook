# Write your solution here
def prime_numbers():
    number = 1
    while True:
        is_prime = False
        number += 1
        if number == 2:
            yield number
        else:
            for i in range(2, number):
                if number % i == 0:
                    is_prime = False
                    break
                if number == i+1:
                    is_prime = True
            if is_prime:
                yield number

                
if __name__ == "__main__":
    numbers = prime_numbers()
    for i in range(8):
        print(next(numbers))