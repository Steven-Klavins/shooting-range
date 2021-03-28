# Import pygame library
import pygame
# Initialize pygame
pygame.init()
# Create screen/canvas + resolution
screen = pygame.display.set_mode((1280, 720))

# While True is our continuous game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
           pygame.quit()   # This event allows us to close window, without this the window wont close
           sys.exit() # Finalises the closing of the game completely (kills all)

    pygame.display.update() # This event continuously updates frames