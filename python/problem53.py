from math import factorial


def nCr(n, r):
    combination = factorial(n) / (factorial(r) * factorial(n - r))
    return combination

if __name__ == '__main__':
    count = 0
    for i in range(1, 101):
        for j in range(1, i + 1):
            if nCr(i, j) > 1000000:
                count += 1

    print(count)
