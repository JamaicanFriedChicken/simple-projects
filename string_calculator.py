'''
Calculates a string of characters only for addition and subtraction
with parentheses, haven't added a function for multiplication and
division. This calculator utilizes the stack method.

#TODO
- Add multiplcation of strings
- Add a division function for strings
'''

import re

def calculate(s: str) -> int:

    s = re.sub(r'[A-Za-z\s\t]+', '', s)
    res = 0
    num = 0
    sign = 1
    stack = []
    for ss in s:
        # checks if each element is a digit
        if ss.isdigit():
            num = 10 * num + int(ss)
        # if not a digit, checks if its + or - sign
        elif ss in ["-", "+"]:
            res = res + sign * num
            num = 0
            sign = [-1, 1][ss == "+"]
            '''
            sign = [-1, 1][ss=="+"]  is the same as:
            # int(True) = 1, int(False) = 0. Hence,
            if ss == "+":
                        sign = 1
            else:
                        sign = -1
            '''
        elif ss == "(":
            stack.append(res)
            stack.append(sign)
            sign, res = 1, 0
        elif ss == ")":
            res = res + sign * num
            res = res * stack.pop()
            res = res + stack.pop()
            num = 0
    return res + num * sign

s = "(1+(4+5+2)-3)+(6+8)"

print(calculate(s))