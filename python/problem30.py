'''
This one's a quite ugly solution; instead of going through the thinking
to find the greatest number which can be the sum of the fifth powers of
its digits, I simply did an while loop and accepted the output after
about 10 secs as the answer.
'''
def sum_digits_power(n): return sum([int(digit) ** 5 for digit in str(n)])

total = 0
number = 2

while True:
    number += 1
    if number == sum_digits_power(number):
        total += number
    print(total)
