from itertools import combinations, permutations, combinations_with_replacement
from operator import add, sub, mul, floordiv

DIGITS = list(range(1, 10))
OPS = [add, sub, mul, floordiv]

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
            for op_perm in permutations(op_comb):
                result = 0
                try:
                    result = op_comb[0](digits[0], 
                             op_comb[1](digits[1],
                             op_comb[2](digits[2],
                                        digits[3])))
                except ZeroDivisionError:
                    pass
                results.add(result)
        return list(results)


