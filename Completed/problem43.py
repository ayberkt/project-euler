from itertools import permutations

def sub_strings_divisible(num):
    global primes_dict
    has_sub_string_divisibility = True
    num_string = str(num)

    for index in range(1, 8):
        sub = int(num_string[index:index+3])

        if not sub % primes_dict[index] == 0:
            return False

    return True




perms = list(permutations(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']))

global primes_dict
primes_dict = {1:2, 2:3, 3:5, 4:7, 5:11, 6:13, 7:17}

total = 0
for perm in perms:
    num_string = "".join(perm)
    current_num = int(num_string)
    if sub_strings_divisible(current_num):
        total += current_num

print total