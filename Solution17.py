# This script implements a solution for the 17th Project Euler problem.

def wordNum(num):
	onesDict = {'1': 'one', '2': 'two', '3': 'three', '4': 'four',
	'5': 'five', '6':'six', '7': 'seven', '8': 'eight', '9': 'nine'}

	tensDict = {'2': 'twenty', '3': 'thirty', '4': 'forty', 
	'5': 'fifty', '6': 'sixty', '7':'seventy', '8': 'eighty',
	'9': 'ninety'}

	uniqueDict = {'10': 'ten', '11': 'eleven', '12': 'twelve', '13': 'thirteen',
	'14': 'fourteen', '15': 'fifteen', '16': 'sixteen',
	'17': 'seventeen', '18':'eighteen', '19':'nineteen'}

	numString = str(num)

	if num == 1000:
		return 'onethousand'

	count = 0
	word = ''
	for i in numString:
		count += 1
		if len(numString) == 3:
			if count == 1:
				word = word + onesDict[i] + 'hundred' + 'and'
			if count == 2:
				if i != '0':
					if i != '1':
						word += tensDict[i]
					else:
						index = i + numString[2]
						word += uniqueDict[index]
			if count == 3:
				if i != '0' and numString[1] != '1':
					word += onesDict[i]
				else:
					if numString[1] == '0':
						word = word.replace(' ', '')[:-3].upper()
		if len(numString) == 2:
			if count == 1:
				if i != '1':
					word = word + tensDict[i]
				else:
					key = i + numString[1]
					word += uniqueDict[key]
					return word

			if count == 2:
				if i != '0':
					word += onesDict[i]

		if len(numString) == 1:
			return onesDict[i]


	return word

# letterCount = 0
# for i in range(1, 1001):
# 	letterCount += len(wordNum(i))
# print letterCount