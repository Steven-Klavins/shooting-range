# Import pygame library
import pygame
import sys
# Initialize pygame
pygame.init()
# Create clock to measure framerates 
clock = pygame.time.Clock()
# Create screen/canvas + resolution
screen = pygame.display.set_mode((1280, 720))

# Import images
wood_bg = pygame.image.load('Wood_BG.png') 
land_bg = pygame.image.load('Land_BG.png') 
water_bg = pygame.image.load('Water_BG.png') 

# While True is our continuous game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
           pygame.quit()   # This event allows us to close window, without this the window wont close
           sys.exit() # Finalises the closing of the game completely (kills all)

    screen.blit(wood_bg,(0,0)) # Here we place the image on to the surface with .blit
    # .blit takes two arguments, the image and the coordinates (0,0) which is the top left 

    screen.blit(land_bg,(0,560)) # pygame renders images in layers the assets as the code is executed
    # This means the top layer is last in the code
    screen.blit(water_bg,(0,640))

    pygame.display.update() # This event continuously updates frames
    clock.tick(120) #Set frame rate to max of 120