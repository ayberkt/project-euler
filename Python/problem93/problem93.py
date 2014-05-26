from itertools import combinations, permutations, combinations_with_replacement, product
from operator import add, sub, mul, floordiv, truediv
from copy import copy


# div = floordiv
def div(a, b):
    return round(truediv(a, b))

DIGITS = list(range(1, 10))
OPS = [add, sub, mul, div]


def permutations_with_replacement(iterable, selection):
    return list(product(iterable, repeat=selection))


op_combinations = [list(op_comb) for op_comb
                   in permutations_with_replacement(OPS, 3)]
digit_combinations = [list(digit_comb) for digit_comb in combinations(DIGITS, 4)
                      if (lambda x: x[0] < x[1] < x[2] < x[3])(digit_comb)]


def consecutive_seq(l):
    l = sorted(l)
    prev_num = l[0]
    consecutive_seq = [prev_num]

    for num in l[1:]:
        if num - 1 == prev_num:
            consecutive_seq.append(num)
        else:
            return consecutive_seq
        prev_num = num

    return consecutive_seq


def target_numbers(digits):
        results = set()
        for ops in op_combinations:
            for digits in permutations(digits, 4):
                a, b, c, d = digits
                temp_results = set()

                # a + b + c + d
                try:
                    result = ops[2](ops[1](ops[0](a, b), c), d)
                except ZeroDivisionError:
                    pass
                temp_results.add(copy(result))

                # (a + b) + (c + d)
                try:
                    result = ops[1](ops[0](a, b), ops[2](c, d))
                except ZeroDivisionError:
                    pass
                temp_results.add(copy(result))

                # a + (b + c + d)
                try:
                    result = ops[0](a, ops[2](ops[1](b, c), d))
                except ZeroDivisionError:
                    pass
                temp_results.add(copy(result))

                # a + (b + c) + d
                try:
                    result = ops[2](ops[0](a, ops[1](b, c)), d)
                except ZeroDivisionError:
                    pass
                temp_results.add(copy(result))

                # a + b + (c + d)
                try:
                    result = ops[0](a, ops[1](b, ops[2](c, d)))
                except ZeroDivisionError:
                    pass
                temp_results.add(copy(result))

                results.update(temp_results)
        return [num for num in list(results) if num > 0]

if __name__ == '__main__':
    max = 0
    max_digit_comb = 0
    for digit_comb in digit_combinations:
        consec = len(consecutive_seq(target_numbers(digit_comb)))
        if  consec > max:
            max = consec
            max_digit_comb = digit_comb
    print(max_digit_comb)

