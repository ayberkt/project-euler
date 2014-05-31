

def rotations(num):
    rotations = set()
    digit_array = list(str(num))

    for i in range(len(digit_array)):
        digit_array.insert(0, digit_array.pop())
        rotations.add(int(''.join(digit_array)))

    return list(rotations)
