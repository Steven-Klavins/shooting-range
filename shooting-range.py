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
cloud1 = pygame.image.load('Cloud1.png') 
cloud2 = pygame.image.load('Cloud2.png') 

#Set animation variables 
land_position_y = 560 
land_speed = 1

# While True is our continuous game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
           # This event allows us to close window, without this the window wont close
           pygame.quit() 
           # Finalises the closing of the game completely (kills all)  
           sys.exit() 

    screen.blit(wood_bg,(0,0)) 

    # Here we place the image on to the surface with .blit
    # .blit takes two arguments, the image and the coordinates (0,0) which is the top left 
    screen.blit(land_bg,(0,land_position_y)) 

    # pygame renders images in layers the assets as the code is executed
    # This means the top layer is last in the code
    screen.blit(water_bg,(0,640))
    screen.blit(cloud1,(300,100))
    screen.blit(cloud1,(600,180))
    screen.blit(cloud2,(1080,120))
    screen.blit(cloud2,(40,120))
    screen.blit(cloud2,(420,20))
    screen.blit(cloud1,(800,40))

    land_position_y -= land_speed

    if land_position_y <= 520 or land_position_y >= 600:
        land_speed *= -1

    pygame.display.update() # This event continuously updates frames
    clock.tick(120) #Set frame rate to max of 120