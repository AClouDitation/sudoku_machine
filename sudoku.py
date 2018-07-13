from termcolor import colored

class SudokuMap(object):

	def __init__(self, m = None):
		if m is None:
			self.map = [[0 for j in range(9)] for i in range(9)]	
		else:
			self.map = m
		self.fix = [[False for j in range(9)] for i in range(9)]

	
	def draw(self, cursor = [-1,-1]):
		for i in range(9):
			for j in range(9):
				if [i,j] == cursor:
					print(colored(self.map[i][j], 'red'), end = '')
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

		# row check
		for i in range(9):
			flags = [False for x in range(9)]
			for j in range(9):
				if flags[self.map[i][j] - 1] == True:
					return False
				flags[self.map[i][j] - 1] = True

		# colomn check
		for j in range(9):
			flags = [False for x in range(9)]
			for i in range(9):
				if flags[self.map[i][j] - 1] == True:
					return False
				flags[self.map[i][j] - 1] = True

		# box check
		for b in range(9):
			r = b // 3
			c = b % 3
			flags = [False for x in range(9)]
			for i in range(r * 3, r * 3 + 3):
				for j in range(c * 3, c * 3 + 3):
					if flags[self.map[i][j] - 1] == True:
						return False
					flags[self.map[i][j] - 1] = True

		return True
	
	
	def change(self, pos, num):
		if self.fix[pos[0]][pos[1]]: return
		self.map[pos[0]][pos[1]] = num


EXAMPLE_1 = [[(x + 3 * y + y // 3) % 9 + 1 for x in range(9)] for y in range(9)]
# for testing purpose
if __name__ == '__main__':
	s = SudokuMap(EXAMPLE_1)
	s.draw()
	print(s.check())

