def gcd(a, b):
    r = a % b
    if r == 0:
        return b
    return gcd(b, r)


def lcm(a, b):
    return a * b // gcd(a, b)

print reduce(lcm, range(1, 21))
