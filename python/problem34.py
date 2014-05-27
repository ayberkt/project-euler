from math import factorial


def digit_factorial_sum(num):
    global factorial_map
    total = 0
    for i in str(num):
        total += factorials[int(i)]
    return total


if __name__ == "__main__":
    total = 0
    num = 10

    global factorials

    factorials = [factorial(i) for i in range(0, 10)]

    for i in range(10, 10 ** 5):
        if i == digit_factorial_sum(i):
            total += i
    print total
