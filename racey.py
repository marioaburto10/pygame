# bring in the pygame module
import pygame
# bring in time module 
import time
# import python's random module
import random

#initialize pygame
pygame.init()
#width of display screen
display_width = 800
#height of display screen
display_height = 600

# width of car is 72 px
car_width = 72

# creating variables to assign them color values using rgb
black = (0,0,0)
white = (255, 255, 255)
red = (255, 0, 0)

#set up display window 
gameDisplay = pygame.display.set_mode((display_width, display_height))

#setting a title or description for our game
pygame.display.set_caption('Racey or Not')

#setting a clock for our game
clock = pygame.time.Clock()

#bringing in our car image
carImg = pygame.image.load('car.png')

#function that will display car on screen
def car(x,y):
	gameDisplay.blit(carImg, (x,y))
# function that will render an object on the screen
def renderThings(thing_x, thing_y, thing_w, thing_h, color):
	pygame.draw.rect(gameDisplay, color, [thing_x, thing_y, thing_w, thing_h])

# function that produces the surface of the message.
def text_objects(text, font):
	textSurface = font.render(text, True, red)
	return textSurface, textSurface.get_rect()

# sets up text surface and text rectangle to render a message on the screen
def message_display(text):
	# style of font to use
	fontStyle = pygame.font.Font('freesansbold.ttf', 115)
	# set the text surface and rectangle equal to the rendered message
	TextSurf, TextRect = text_objects(text, fontStyle)
	# position message box in the center of the screen
	TextRect.center = ((display_width/2) , (display_height/2))
	# does the actual displaying of the message onto the screen
	gameDisplay.blit(TextSurf, TextRect)

	# updates the screen
	pygame.display.update()
	# message will be up for 3 seconds
	time.sleep(3)
	# begin game again
	game_loop()

# function to display a message if the user crashes on either sides of the screen
def crash():
	message_display('You crashed')

# game runs in this loop function
def game_loop(): 

	#setting coordinates of where we want our car to be located at
	x = (display_width * 0.45)
	y = (display_height * 0.6)

	# car will start out not moving at position 0
	x_change = 0

	# start object at random x position
	thing_start_x = random.randrange(0, display_width)
	# start object off the screen
	thing_start_y = -600 
	# speed of 7 px per second
	thing_speed = 7
	# dimensions of object
	thing_width = 100
	thing_height = 100

	#still in game
	gameExit = False

	#loop that continues while we have not exited the game
	while not gameExit: 
		#iterating through events
		for event in pygame.event.get(): 
			# if user quits, exit game
			if event.type == pygame.QUIT: 
				pygame.quit()
				quit()
			# if the type of event is a keypress
			if event.type == pygame.KEYDOWN:
				# move car -5 to left if left arrow key is pressed
				if event.key == pygame.K_LEFT:
					x_change = -5
				# move car 5 to left if left arrow key is pressed
				elif event.key == pygame.K_RIGHT:
					x_change = 5
			#if the type of event is a key left or key right, stop changing the position of car
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
					x_change = 0
		# the position of the car x is affected by key presses
		x += x_change

		#setting background of white before displaying car
		gameDisplay.fill(white)


		# render an object to the screen
		renderThings(thing_start_x, thing_start_y, thing_width, thing_height, black)
		#give the object an appearance of motion
		thing_start_y += thing_speed

		#loading car on screen
		car(x,y)
		# will run crash function if the car hits either sides of the screen
		if x > display_width - car_width * 1.5 or x < 0:
			crash()
		# once the object is off the screen, restart it back up on the screen at a random x value
		if thing_start_y > display_height:
			thing_start_y = 0 - thing_height
			thing_start_x = random.randrange(0, display_width - 100)
			
		#update screen
		pygame.display.update()
		#game will move at 60 frames per second
		clock.tick(75)

#runs game_loop function
game_loop()
#exit pygame
pygame.quit()
#quit python
quit()

