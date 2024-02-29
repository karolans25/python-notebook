# Write your solution here
def change_case(orig_string: str) -> str:
    return orig_string.swapcase()

def split_in_half(orig_string: str) -> tuple:
    div = len(orig_string) // 2
    return (orig_string[:div], orig_string[div:])

# def check(character: str) -> bool: 
#     return character.isalnum() or character == ' '

def remove_special_characters(orig_string: str) -> str:
    ## Option 1: Using filter
    # return ''.join(filter(check, list(orig_string)))
    ## Option 2: Using for
    # res = ''
    # for character in orig_string:
    #     if character.isalnum() or character == ' ':
    #         res += character
    # return res
    ## Option 3: Using for in the same line
    return ''.join([char for char in orig_string if char.isalnum() or char == ' '])
    
if __name__ == "__main__":
    print(change_case('CaroPulidoG'))
    print(split_in_half('CarolinaRosa'))
    print(split_in_half('CarolinaRosas'))
    print(remove_special_characters('Cárt ik3? öhm!'))
