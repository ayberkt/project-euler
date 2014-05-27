def is_bouncy(n):
    '''In the changes list, "False" indicates a decrease and "True" indicates
    an increase thus in order the number to be either increasing or decreasing
    the "changes" should consist of same values at the end of the operations'''
    changes = []; num_str = str(n)
    for i in range(1, len(num_str)):
        current_num, preceding_num = int(num_str[i]), int(num_str[i - 1])
        if preceding_num == current_num:
            pass
        else:
            changes.append(preceding_num > current_num)

    if False in changes and True in changes:
        return True
    return False

if __name__ == '__main__':
    number, bouncy_count = 0, 0
    while True:
        number += 1
        if is_bouncy(number):
            bouncy_count += 1
        if bouncy_count / number == 99 / 100:
            print(number)
            break
