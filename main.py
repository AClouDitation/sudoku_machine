from sudoku	import *
from control import *
import os

def prompt():
	print("-----COMMANDS-----")
	print("q\tquit")
	print("n\tnew game")
	print("r\trestart")
	print("c\tcheck")
	print()


if __name__ == '__main__':
	
	game_map = None

	# hide cursor
	sys.stdout.write('\033[?25l')

	# main loop
	game_map = newgame()
	while True:
		# draw frame
		os.system('clear')
		prompt()
		if game_map is not None:
			game_map.draw(CRUSOR)

		# control
		cmd = getkey()
		
		if cmd == 'q':
			break
		elif cmd == 'n':
			print('are you sure to start a new game?(y):')
			cmd = getkey()
			if cmd == 'y':
				game_map = newgame()
			else:
				continue
		elif cmd == 'c':
			if game_map.check():
				print("Congratulations! You win!")
				break
			else:
				print("looks like there is something wrong")
				print("Press any key to continue")
				getkey()
			
		elif cmd == 'r':
			game_map.restart()


		elif '1' <= cmd <= '9' or cmd == '-':
			game_map.change(CRUSOR, cmd)
		else:
			move(cmd)
	
	# show cursor
	sys.stdout.write('\033[?25h')
