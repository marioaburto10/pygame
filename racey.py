# bring in the pygame module
import pygame

#initialize pygame
pygame.init()
#width of display screen
display_width = 800
#height of display screen
display_height = 600

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

#setting coordinates of where we want our car to be located at
x = (display_width * 0.35)
y = (display_height * 0.6)

#we have not crashed yet
crashed = False

#loop that continues while we have not crashed
while not crashed: 
	#iterating through events
	for event in pygame.event.get(): 
		# if user quits, set crashed to true to exit while loop
		if event.type == pygame.QUIT: 
			crashed = True

	#setting background of white before displaying car
	gameDisplay.fill(white)
	#loading car on screen
	car(x,y)
		
	#update screen
	pygame.display.update()
	#frame will move at 60 frames per second
	clock.tick(60)
#exit pygame
pygame.quit()
#quit python
quit()

