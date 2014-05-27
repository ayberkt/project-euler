from itertools import combinations, permutations, product
from operator import add, sub, mul, floordiv

def div(a, b):
    try:
        if a % b == 0:
            return round(a / b)
    except ZeroDivisionError: pass
    return 0


DIGITS = list(range(1, 10))
OPS = [add, sub, mul, div]


def permutations_with_replacement(iterable, selection):
    return list(product(iterable, repeat=selection))


op_combinations = [list(op_comb) for op_comb
                   in permutations_with_replacement(OPS, 3)]

digit_combinations = [list(digit_comb) for digit_comb
                      in permutations(DIGITS, 4)
                      if (lambda x: x[0] < x[1] < x[2] < x[3])(digit_comb)]


def consecutive_seq(l):
    l = sorted(l)
    prev_num = 1
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
        for f, g, h in op_combinations:
            for a, b, c, d in permutations(digits, 4):

                # a + b + c + d
                results.add(h(g(f(a, b), c), d))

                # (a + b) + (c + d)
                results.add(g(f(a, b), h(c, d)))

                # a + (b + c + d)
                results.add(f(a, h(g(b, c), d)))

                # a + (b + c) + d
                results.add(h(f(a, g(b, c)), d))

                # a + b + (c + d)
                results.add(f(a, g(b, h(c, d))))

        return [num for num in list(results) if num and num > 0]

if __name__ == '__main__':
    max = 0
    max_digit_comb = 0
    for digit_comb in digit_combinations:
        consec = consecutive_seq(target_numbers(digit_comb))
        len_consec = len(consec)
        if len_consec > max:
            max = len_consec
            max_digit_comb = digit_comb
        elif len_consec == max:
            print(digit_comb)
    print(max_digit_comb)
