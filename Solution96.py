# This script will eventually implement a solution for the 96th Project Euler problem.

class Sudoku(object):

	def __init__(self, sudokuText):
		self.id = int(sudokuText.split('\n', 1)[0])

		nums = '\n'.join(sudokuText.split('\n')[1:])
		lines = nums.splitlines()

		# Convert the lines string to a multi-dimensional array
		matrix = []
		for i in range(0,9):
			column = []
			for line in lines:
				if line[i] == '0':
					column.append(set([1,2,3,4,5,6,7,8,9]))
				else:
					column.append(set(int(line[i]))
			matrix.append(column)
		self.matrix = matrix
		for col in matrix:
			print col

	def getRows(self):
		rows = []
		for i in range (0,9):
			row = []
			for column in self.matrix:
				row.append(column[i])
			rows.append(row)
		return rows

	def getRegions(self):
		regions = [[],[],[],[],[],[],[],[],[]]
		for i in range(0,9):
			for j in range(0,9):
				regions[self.getRegionValue(i,j)].append(self.matrix[i][j])
		return regions

	def getRegionValue(self, i, j):
		if i <= 2:
			if j <= 2:
				return 0
			elif j <= 5:
				return 3
			else:
				return 6
		elif i <= 5:
			if j <= 2:
				return 1
			elif j <= 5:
				return 4
			else:
				return 7
		else:
			if j <= 2:
				return 2
			elif j <= 5:
				return 5
			else:
				return 8


sudokuFile = open('sudoku.txt', 'r').read()

sudokuTexts = sudokuFile.split('Grid')

sudoku = Sudoku(sudokuTexts[1])

for i in range(0,9):
	for j in range(0,9):
		col = self.matrix[i]
		if len(sudoku.matrix[i][j]) > 1:
			i - set(self.ma)

# for line in sudoku.lines: 
# 	print line + '/'
# 	print '***'

# for row in sudoku.rows: print 'Row ' + str(row)
# for column in sudoku.columns: print 'Column ' + str(column)
