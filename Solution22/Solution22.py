# This program implements a solution for the 22th Project Euler problem

import datetime

def strVal(word):
        word = word.translate(None, '"')
        result = 0
        for i in word:
                result += numValue[i]
        return result

timeInit = datetime.datetime.now()
abc = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
       'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
       'V', 'W', 'X', 'Y', 'Z']

numValue = dict(zip(abc, range(1, 27)))
names = sorted(str(open('names.txt', 'r').read()).split(','))

sum = 0
for i in names: sum += strVal(i)*(names.index(i)+1)
print sum
print datetime.datetime.now() - timeInit
