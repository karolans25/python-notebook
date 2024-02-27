# Write your solution here
from datetime import datetime

def is_it_valid(pic: str):
    valid = '0123456789ABCDEFHJKLMNPRSTUVWXY'
    century = pic[6:7]
    if century == '-':
        year = '18'
    elif century == '+':
        year = '19'
    elif century == 'A':
        year = '20'

    year += pic[4:6]
    year = int(year)
    month = int(pic[2:4])
    day = int(pic[0:2])

    if (0 < month <= 12):
        date = datetime(int(year), int(month), int(day))
        print(date)
    else: 
        return False
    
    identifier = int(pic[7:10])

    num = ( (year + month + day + identifier) // 31 ) % 31
    print(str(valid[ num ]))

    if pic[-1] == str(valid[ num ]):
        return True

    return False

if __name__ == "__main__":
    # print(is_it_valid('230827-906F'))
    # print(is_it_valid('120488+246L'))
    # print(is_it_valid('310823A9877'))
    print(is_it_valid('080842-720N'))
    # print(is_it_valid(''))