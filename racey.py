# bring in the pygame module
import pygame

#initialize pygame
pygame.init()

#set up display window to be a width of 800 and height of 600
gameDisplay = pygame.display.set_mode((800, 600))

#setting a title or description for our game
pygame.display.set_caption('Racey or Not')

#setting a clock for our game
clock = pygame.time.Clock()

#we have not crashed yet
crashed = False

#loop that continues while we have not crashed
while not crashed: 
	#iterating through events
	for event in pygame.event.get(): 
		# if user quits, set crashed to true to exit while loop
		if event.type == pygame.QUIT: 
			crashed = True
		#print to the console the frame by frame events
		print(event)
	#update screen
	pygame.display.update()
	#frame will move at 60 frames per second
	clock.tick(60)
#exit pygame
pygame.quit()
#quit python
quit()

