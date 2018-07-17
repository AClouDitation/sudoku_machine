from termcolor import colored

class SudokuMap(object):

	def __init__(self, mfile):
		self.fix = [[False for j in range(9)] for i in range(9)]
		self.map = [[0 for j in range(9)] for i in range(9)]

		with open(mfile, 'r') as f:
			for i in range(9):
				line = f.readline()
				for j in range(9):
					if line[j] != ' ':
						self.fix[i][j] = True
						self.map[i][j] = line[j]
					else:
						self.map[i][j] = '-'


	
	def draw(self, cursor = [-1,-1]):
		for i in range(9):
			for j in range(9):
				if [i,j] == cursor:
					print(colored(self.map[i][j], 'red'), end = '')
				elif not self.fix[i][j]:
					print(colored(self.map[i][j], 'yellow'), end = '')
				else:
					print(self.map[i][j], end='')

				if j == 2 or j == 5:
					print('|', end = '')
				else:
					print(' ', end = '')

			print()
			if i == 2 or i == 5:
				print(('-' * 5 + ' ') * 3)
	

	def check(self):

		for i in range(9):
			for j in range(9):
				if self.map[i][j] == '-':
					return False

		# row check
		for i in range(9):
			flags = [False for x in range(9)]
			for j in range(9):
				if flags[int(self.map[i][j]) - 1] == True:
					return False
				flags[int(self.map[i][j]) - 1] = True

		# colomn check
		for j in range(9):
			flags = [False for x in range(9)]
			for i in range(9):
				if flags[int(self.map[i][j]) - 1] == True:
					return False
				flags[int(self.map[i][j]) - 1] = True

		# box check
		for b in range(9):
			r = b // 3
			c = b % 3
			flags = [False for x in range(9)]
			for i in range(r * 3, r * 3 + 3):
				for j in range(c * 3, c * 3 + 3):
					if flags[int(self.map[i][j]) - 1] == True:
						return False
					flags[int(self.map[i][j]) - 1] = True

		return True
	
	
	def change(self, pos, num):
		if self.fix[pos[0]][pos[1]]: return
		self.map[pos[0]][pos[1]] = num
	

	def restart(self):
		for i in range(9):
			for j in range(9):
				if not self.fix[i][j]:
					self.map[i][j] = '-'

EXAMPLE_1 = [[(x + 3 * y + y // 3) % 9 + 1 for x in range(9)] for y in range(9)]
# for testing purpose
if __name__ == '__main__':
	s = SudokuMap(EXAMPLE_1)
	s.draw()
	print(s.check())

