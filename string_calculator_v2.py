import re


def calculate(string: str) -> int:
    """
    :param string: string of characters to be calculated
    :return: the total of the string entered
    character: represents each character in string
    """
    stack = []
    # a symbol is added to the end of the string to allow for the calculator to fully
    # calculate the entire string except the symbol.
    string = re.sub(r'[A-Za-z\s\t]+', '', string) + '?'
    number = 0
    operator = '+'
    for character in string:
        if character.isdigit():
            number = number * 10 + int(character)
        else:
            if operator == '+':
                stack.append(number)
            elif operator == '-':
                stack.append(-number)
            elif operator == '*':
                stack.append(stack.pop() * number)
            else:
                if number == 0:
                    return ''
                n = stack.pop()
                if n // number < 0 and n % number != 0:
                    stack.append(n // number + 1)
                else:
                    stack.append(n // number)
            number = 0
            operator = character
    return sum(stack)


string = "2 + 3 * 20"
print(calculate(string))
