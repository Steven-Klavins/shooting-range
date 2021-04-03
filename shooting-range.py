# Import pygame library
import pygame
import sys
import random
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
crosshair = pygame.image.load('crosshair.png')
duck_surface = pygame.image.load('duck.png')

# Set animation variables
land_position_y = 560
land_speed = 0.7
water_position_y = 640
water_speed = 2

duck_list = []
for duck in range(20):
    duck_position_x = random.randrange(50, 1200)
    duck_position_y = random.randrange(120, 600)
    duck_rect = duck_surface.get_rect(
        center=(duck_position_x, duck_position_y))
    duck_list.append(duck_rect)

# If the cursor is not on the display crosshair_rect will be None so I itialize the position centered here first
crosshair_rect = crosshair.get_rect(center=(640, 360))

# While True is our continuous game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # This event allows us to close window, without this the window wont close
            pygame.quit()
            # Finalises the closing of the game completely (kills all)
            sys.exit()

        # Continously check to see if the mouse has moved
        # We create a new variable called crosshair_rect to hold the x/y values
        # The values come from the center of rectangle we draw round the image with get_rect
        # We set the center of the rect/image using event.pos (center of rect mouse position)
        if event.type == pygame.MOUSEMOTION:
            crosshair_rect = crosshair.get_rect(center=event.pos)

    screen.blit(wood_bg, (0, 0))

    # Here we place the image on to the surface with .blit
    # .blit takes two arguments, the image and the coordinates (0,0) which is the top left
    screen.blit(land_bg, (0, land_position_y))

    for duck_rect in duck_list:
        screen.blit(duck_surface, duck_rect)

    # pygame renders images in layers the assets as the code is executed
    # This means the top layer is last in the code
    screen.blit(water_bg, (0, water_position_y))
    screen.blit(cloud1, (300, 100))
    screen.blit(cloud1, (600, 180))
    screen.blit(cloud2, (1080, 120))
    screen.blit(cloud2, (40, 120))
    screen.blit(cloud2, (420, 20))
    screen.blit(cloud1, (800, 40))

    # Here we add the crosshair image and our rectangle position
    screen.blit(crosshair, crosshair_rect)

    land_position_y -= land_speed
    water_position_y -= water_speed

    # Animate land position is below 520 or above 600 reverse direction
    if land_position_y <= 520 or land_position_y >= 600:
        land_speed *= -1

    # Sometimes objects can run past there stopping point so we use >= <= never ==
    if water_position_y <= 600 or water_position_y >= 680:
        water_speed *= -1

    pygame.display.update()  # This event continuously updates frames
    clock.tick(120)  # Set frame rate to max of 120
