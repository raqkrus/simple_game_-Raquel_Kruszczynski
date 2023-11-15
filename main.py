import pygame

pygame.init()
running = True

#set dimentions
screen_width = 800
screen_height = 600

def build_background():
    background_image = pygame.image.load("images/tilebackground.jpg")
    background = pygame.transform.scale(background_image, (screen_width, screen_height))
    return background

 # get screen size/width
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pygame Background")

#load the image
background_image= "images/tilebackground.jpg"

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
             running = False

    screen.blit(build_background(), (0,0))

    #WORKS ^^^^

    # set color for table and shelves
    light_brown = (196, 164, 132)
    lighter_brown = (213, 193, 170)

    # set size of table
    table_width = screen_width
    table_height = (2 / 3) * screen_height

    # set y pos for table
    table_y = (2 / 3) * screen_height

    # draw rectangle on screen
    pygame.draw.rect(screen, light_brown, (0, table_y, table_width, table_height))

    # set up shelves
    shelf_width = 200
    shelf_height = 200
    shelf_y = 200

    # set shelf x positions
    left_shelf_x = 0
    right_shelf_x = screen_width - shelf_width







    pygame.display.update()

pygame.quit()