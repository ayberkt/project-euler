def is_palindromic(n):
    if str(n) == str(n)[::-1]:
        return True
    return False


def is_lychrel(n):
    for i in range(50):
        n += int(str(n)[::-1])
        if is_palindromic(n):
            return False
    return True

total = 0
for i in range(10001):
    i += int(str(i)[::-1])
    if not is_palindromic(i):
        if is_lychrel(i):
            total += 1
print total