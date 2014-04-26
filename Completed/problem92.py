from time import clock

def square_digits(number):
    return sum([int(digit) ** 2 for digit in str(number)])

def becomes_1(number):
    global sequence_to_89
    global sequence_to_1
    original_number = number
    traversed_nums = set()

    while True:
        traversed_nums.add(number)
        number = square_digits(number)
        if number in sequence_to_89:
            sequence_to_89.update(traversed_nums)
            return False
        if number in sequence_to_1:
            sequence_to_1.update(traversed_nums)
            return True

if __name__ == "__main__":
    clock()

    global sequence_to_89; sequence_to_89 = {89}
    global sequence_to_1; sequence_to_1 = {1}

    count = 0
    for number in range(1, int(10e6)):
        if not becomes_1(number): count += 1

    print(count)
    print clock()
