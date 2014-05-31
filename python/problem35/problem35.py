from math import sqrt


def memoize(f):
    cache = {}

    def helper(x):
        if x not in cache:
            cache[x] = f(x)
        return cache[x]

    return helper


@memoize
def is_prime(n):
    if n == 2:
        return True
    if n == 1:
        return False

    test_nums = range(2, int(sqrt(n)) + 2)
    for i in test_nums:
        if n % i == 0:
            return False
    return True


@memoize
def rotations(num):
    rotations = set()
    digit_array = list(str(num))

    for i in range(len(digit_array)):
        digit_array.insert(0, digit_array.pop())
        rotations.add(int(''.join(digit_array)))

    return list(rotations)


def rotational_prime(num):
    if '5' in str(num) or '2' in str(num):
        return False

    return all([is_prime(n) for n in rotations(num)])


if __name__ == '__main__':
    rotational_primes = [2, 3, 5, 7] + [n for n in range(11, 1000000, 2)
                               if rotational_prime(n)]
    print(len(rotational_primes))
