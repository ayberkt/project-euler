def is_palindromic(num_str):
    return num_str == num_str[::-1]

total = 0
for i in xrange(1, 10 ** 6):
    if isPalindromic(str(i)) and isPalindromic(bin(i)[2:]):
        total += i

print total
