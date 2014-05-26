from itertools import combinations, permutations, combinations_with_replacement
from operator import add, sub, mul, truediv
from copy import copy


def div(x, y):
    return round(truediv(x, y))


DIGITS = list(range(1, 10))
OPS = [add, sub, mul, div]

op_combinations = [list(op_comb) for op_comb
                   in combinations_with_replacement(OPS, 3)]
digit_combinations = [list(digit_comb) for digit_comb in combinations(DIGITS, 4)
                      if (lambda x: x[0] < x[1] < x[2] < x[3])(digit_comb)]


def consecutive(l):
    l = list(set(l))
    for i in range(len(l) - 1):
        if l[i+1] - l[i] != 1:
            return False
    return True


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
