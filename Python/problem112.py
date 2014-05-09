from enum import Enum

NumberType = Enum('NumberType', 'increasing decreasing bouncy')
 

def number_type(n):
    changes = []
    num_str = str(n)
    for i in range(len(num_str)):
        try:
            changes.append(int(num_str[i + 1]) < int(num_str[i]))
        except IndexError:
            break

    if False in changes and not True in changes:
        return NumberType.increasing
    elif True in changes and not False in changes:
        return NumberType.decreasing
    else:
        return NumberType.bouncy
