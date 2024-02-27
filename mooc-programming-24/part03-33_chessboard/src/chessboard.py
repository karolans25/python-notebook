# Write your solution here
def chessboard(lines):
    count = 0
    while count < lines:
        if count % 2 == 0:
            row = '10'*lines
        else:
            row = '01'*lines
        print(row[0:lines])
        count += 1

# Testing the function
if __name__ == "__main__":
    chessboard(6)
