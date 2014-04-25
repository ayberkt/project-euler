from time import clock

def square_digits(number):
    return sum([int(digit) ** 2 for digit in str(number)])

def becomes_one(number):
    global becomes_one_dict
    original_number = number
    keys = becomes_one_dict.keys()

    while True:
        if number in keys:
            # print("Using dict value")
            became_one = becomes_one_dict[number]
            becomes_one_dict[original_number] = became_one
            return became_one
        else:
            # print("Value not found")
            number = square_digits(number)

        if number == 1:
            becomes_one_dict[original_number] = True
            return True
        elif number == 89:
            becomes_one_dict[original_number] = False
            return False


if __name__ == "__main__":
    clock()

    global becomes_one_dict
    becomes_one_dict = {}

    number, count = 1, 0

    while number < 10e6:
        if not becomes_one(number):
            count += 1
        number += 1

    print(count)
    print("Took " + str(clock()))