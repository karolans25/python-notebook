# Write your solution here
password = input("Password: ")
confirm_password = ""

while password != confirm_password:
    confirm_password = input("Repeat password: ")
    if password != confirm_password:
        print("They do not match!")

print("User account created!")