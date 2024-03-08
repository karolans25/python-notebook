def get_m(point1: tuple, point2: tuple):
    return (point2[1] - point1[1])/(point2[0] - point1[0])

def balanced_brackets(my_string: str):
    if len(my_string) == 0:
        return True

    f_cp_closed = my_string.find(')')    
    f_sp_closed = my_string.find(']')    
    c_p = ( my_string.find('(') , my_string.rfind(')')) # circular parenthesis
    s_p = ( my_string.find('[') , my_string.rfind(']')) # sqare parenthesis

    if c_p == (-1, -1) and s_p == (-1, -1):
        return True
    if c_p[0] * c_p[1] < 0:
        return False
    if s_p[0] * s_p[1] < 0:
        return False
    if f_cp_closed < c_p[0]:
        return False
    if f_sp_closed < s_p[0]:
        return False

    valid_cp = c_p[0] * c_p[1] >= 0 and c_p != (-1, -1)
    valid_sp = s_p[0] * s_p[1] >= 0 and s_p != (-1, -1)
    if valid_cp and valid_sp:
        simb = '(' if c_p[0] < s_p[0] else '['
        m = get_m(c_p, s_p) if c_p[0] < s_p[0] else get_m(s_p, c_p)
        if m < 0:
            if simb == '(':
                return balanced_brackets(my_string[c_p[0] + 1: c_p[1]])
            if simb == '[':
                return balanced_brackets(my_string[s_p[0] + 1: s_p[1]])
        else:
            return False
    elif valid_cp:
        simb = '('
        return balanced_brackets(my_string[c_p[0] +1 : c_p[1]])
    elif valid_sp:
        simb = '['
        return balanced_brackets(my_string[s_p[0] +1 : s_p[1]])


if __name__ == '__main__':
    ok = balanced_brackets("(((())))")
    print(ok) # True

    # there is one closing bracket too many, so this produces False
    ok = balanced_brackets("()())")
    print(ok) # False

    # this one starts with a closing bracket, False again
    ok = balanced_brackets(")()")
    print(ok) # False

    # this produces False because the function only handles entirely nested brackets
    ok = balanced_brackets("()(())")
    print(ok) # False

    ok = balanced_brackets("([([])])")
    print(ok) # True

    ok = balanced_brackets("(python version [3.7]) please use this one!")
    print(ok) # True

    # this is no good, the closing bracket doesn't match
    ok = balanced_brackets("(()]")
    print(ok) # False

    # different types of brackets are mismatched
    ok = balanced_brackets("([bad egg)]")
    print(ok) # False
