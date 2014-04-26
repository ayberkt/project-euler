from time import clock
from itertools import permutations

def sum_square_digits(number):
    return sum([int(digit) ** 2 for digit in str(number)])

def happy(number):
    traversed = set()
    original_number = number

    digits_sorted_num = ""
    for num_str in sorted(list(str(number))):
        digits_sorted_num += num_str
    digits_sorted_num = int(digits_sorted_num)

    if int(digits_sorted_num) in sequence_to_89:
        sequence_to_89.add(original_number)
        return True
    if int(digits_sorted_num) in sequence_to_1:
        sequence_to_1.add(original_number)
        return False

    while True:
        number = sum_square_digits(number)

        if number in sequence_to_89:
            sequence_to_89.add(original_number)
            return True
        if number in sequence_to_1: 
            sequence_to_1.add(original_number)
            return False


if __name__ == "__main__":
    clock()

    global sequence_to_89; sequence_to_89 = {89, 145, 42, 20, 4, 16, 37, 58}
    global sequence_to_1; sequence_to_1 = {1, 10, 100, 1000, 10000, 100000, 1000000}

    number = "12345600"

    count = 0
    for number in range(1, 10000000):
        # print(number)
        if happy(number): count += 1

    # count = 0
    # for number in range(1, int(10e6)):
    #     if not becomes_1(number): count += 1

    print(count)
    print(clock())
