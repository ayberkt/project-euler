def is_palindromic(num_str):
    return num_str == num_str[::-1]

total = 0
for i in range(1, 10 ** 6):
    if is_palindromic(str(i)) and is_palindromic(bin(i)[2:]):
        total += i

print(total)
