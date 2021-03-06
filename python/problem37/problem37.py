from math import sqrt


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


def truncations(num_str):

    truncations = set()
    length = len(num_str)

    for i in range(1, len(num_str)):
        truncations.add(num_str[:i])
        truncations.add(num_str[i:length])

    return [num for num in set(truncations) if len(num)]


def truncatable_prime(num):
    return is_prime(num) and all([is_prime(int(n))
                                  for n in truncations(str(num))])


if __name__ == '__main__':

    num = 13
    truncatable_primes = []
    while True:

        if truncatable_prime(num):
            truncatable_primes.append(num)

        if len(truncatable_primes) == 11:
            print(sum(truncatable_primes))
            break

        num += 2
