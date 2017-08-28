# bring in the pygame module
import pygame

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
carImg = pygame.image.load('car.jpeg')

#function that will display car on screen
def car(x,y):
	gameDisplay.blit(carImg, (x,y))

# game runs in this loop function
def game_loop(): 

	#setting coordinates of where we want our car to be located at
	x = (display_width * 0.35)
	y = (display_height * 0.6)

	# car will start out not moving at position 0
	x_change = 0

	#still in game
	gameExit = False

	#loop that continues while we have not exited the game
	while not gameExit: 
		#iterating through events
		for event in pygame.event.get(): 
			# if user quits, set crashed to true to exit while loop
			if event.type == pygame.QUIT: 
				gameExit = True
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
		#loading car on screen
		car(x,y)
		# game will finish if the car hits either sides of the screen
		if x > display_width - car_width * 2 or x < 0:
			gameExit = True
			
		#update screen
		pygame.display.update()
		#frame will move at 60 frames per second
		clock.tick(60)

#runs game_loop function
game_loop()
#exit pygame
pygame.quit()
#quit python
quit()

