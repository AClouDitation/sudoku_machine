import sys
import tty, termios
import curses
from sudoku import *

def getkey():

	fd = sys.stdin.fileno()
	old_settings = termios.tcgetattr(fd)

	try:
		tty.setraw(fd)
		ch = sys.stdin.read(1)
	finally:
		termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

	return ch


def newgame():	
	s = SudokuMap(EXAMPLE_1) 
	return s


CRUSOR = [0,0]
def move(cmd):
	if cmd == '\x1b':
		getkey()
		direction = getkey()
		if direction == 'B':
			CRUSOR[0] += 1
			CRUSOR[0] %= 9
		elif direction == 'A':
			if CRUSOR[0] == 0:CRUSOR[0] = 8
			else:CRUSOR[0] -= 1
		elif direction == 'D':
			if CRUSOR[1] == 0:CRUSOR[1] = 8
			else:CRUSOR[1] -= 1
		elif direction == 'C':
			CRUSOR[1] += 1	
			CRUSOR[1] %= 9


if __name__ == '__main__':
	ch = ''
	while ch != 'q':
		ch = getkey()
		if ch == 'h':
			print('\033[H')
		move(ch)
