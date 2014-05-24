from itertools import combinations, permutations, combinations_with_replacement
from operator import add, sub, mul, truediv


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


def target_numbers(digits):
        results = set()
        for op_comb in op_combinations:
            for ops in permutations(op_comb):
                for digits in permutations(digits):
                    result1, result2 = 0, 0
                    try:
                        result1 = ops[0](digits[0],
                                         ops[1](digits[1],
                                                ops[2](digits[2],
                                                       digits[3])))
                    except ZeroDivisionError:
                        pass

                    try:
                        result2 = ops[0](ops[1](digits[0], digits[1]),
                                         ops[2](digits[2], digits[3]))
                    except ZeroDivisionError:
                        pass

                    if result1 > 0:
                        results.add(result1)
                    if result2 > 0:
                        results.add(result2)
        return list(results)
