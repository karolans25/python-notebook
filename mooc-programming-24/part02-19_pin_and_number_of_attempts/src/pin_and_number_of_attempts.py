# Write your solution here
attemps = 0;
code = '0000'

while code != '4321':
    code = input("PIN: ")
    if code != '4321':
        print("Wrong")
    attemps += 1

if attemps == 1:
    print("Correct! It only took you one single attempt!")
else: 
    print(f"Correct! It took you {attemps} attempts")