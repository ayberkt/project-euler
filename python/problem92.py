def sum_square_digits(number): return sum([int(digit) ** 2 for digit in str(number)])

def happy(number):
    original_number = number

    '''
    Before testing which sequence the number is in, it dramatically 
    improves the performance to sort the digits of the number and
    then conduct a control with sorted digits, since at some point it should
    have been controlled and its information saved to a one of the sequences.
    As an example when we reach 213, we may see that we have already
    tested 123, whose "sum_square_digits" is the same as 213 This omits the
    need to calculate the "sum_square_digits" for most of the numbers.
    '''
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

    # If we have not analyzed the number, we may go on and 
    # compute the sequence it requires to reach 89 or 1
    while True:
        number = sum_square_digits(number)

        if number in sequence_to_89:
            sequence_to_89.add(original_number)
            return True
        if number in sequence_to_1: 
            sequence_to_1.add(original_number)
            return False


if __name__ == "__main__":
    global sequence_to_89; sequence_to_89 = {89, 145, 42, 20, 4, 16, 37, 58}
    global sequence_to_1; sequence_to_1 = {1, 10, 100, 1000, 10000, 100000, 1000000}

    count = 0
    for number in range(1, 10000000):
        if happy(number): count += 1

    print(count)
