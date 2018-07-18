from graphics import *
from random import choice, randint

# this function create a circle object of the circle, x velocity
# and y velocity
# @pt: center point of the circle
# @radius: radius of the circle
# @win: window to draw the circle on
# @dx:	x velocity
# @dy 	y velocity
def create(pt, radius, win, dx, dy):

	# create a circle object
	circle = Circle(pt, radius)

	# randomly choose a color
	color = choice(['red','blue','green','orange'])
	circle.setFill(color)	# fill the circle with the chosen color
	circle.draw(win)		# draw it on the window

	return [circle, dx ,dy]


# this function checks if a circle is colliding the bondary 
# of the given window, if so, bounce it back
# @circle: circle needs to check
# @win: window used to check
def check(circle, win):

	# get the circle object
	cir = circle[0]

	# check if the circle touch the bound on x axis
	if circle[0].getCenter().getX() + circle[0].getRadius() >= 500 or\
	circle[0].getCenter().getX() - circle[0].getRadius() <= 0:
		circle[1] *= -1

	# check if the circle touch the bound on y axis
	if circle[0].getCenter().getY() + circle[0].getRadius() >= 500 or\
	circle[0].getCenter().getY() - circle[0].getRadius() <= 0:
		circle[2] *= -1


# this function checks if a point is in a given circle
# @pt: point needs to check
# @circle: circle use to check
# if the point is in circle, return True
# else return Fasle
def inCircle(pt, circle):
	
	# calculate the distance between the given point and circle center
	dx = circle.getCenter().getX() - pt.getX()
	dy = circle.getCenter().getY() - pt.getY()
	dist = (dx ** 2 + dy ** 2) ** (1 / 2)
	
	# check if the point in the circle
	if dist < circle.getRadius():
		return True

	return False 


def main():

	# create a window
	win = GraphWin("Pop-em", 500, 500)

	# crate a empty circle list and append in to the list
	circles = []
	cir = create(Point(250,250),80, win, randint(-10, 10)/200, randint(-10, 10)/200)
	circles.append(cir)

	# draw text and wait for mouse cilck
	text = Text(Point(250,50),'Click anywhere to start')
	text.draw(win)
	win.getMouse()
	text.undraw()

	# loop until all circle are canceled
	while circles != []:
		# keep checking mouse click
		click = None
		click = win.checkMouse()

		for cir in circles:
			if click is not None:
				# if there is a click, check if it is in this circle
				if inCircle(click, cir[0]):

					# if so, undraw the circle and remove from the list
					cir[0].undraw()
					circles.remove(cir)

					# if the removed circle are large enough
					if cir[0].getRadius() >= 20:
						# split it in to two small circle and append them into the list
						circles.append(create(cir[0].getCenter(),\
							cir[0].getRadius() // 2, win, cir[1] * -1.2, cir[2]))
						circles.append(create(cir[0].getCenter(),\
							cir[0].getRadius() // 2, win, cir[1], cir[2] * -1.2))
					break

		
		# move every circle
		for cir in circles:
			check(cir, win)
			cir[0].move(cir[1], cir[2])

	# display text and wait for mouse click
	text.setText('Game Over')
	text.draw(win)
	win.getMouse()

	# close window
	win.close()


main()

