import pygame

pygame.init()
running = True

# set dimentions
screen_width = 800
screen_height = 600


def build_background():
    background_image = pygame.image.load("images/tilebackground.jpg")
    background = pygame.transform.scale(background_image, (screen_width, screen_height))
    return background


# get screen size/width
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pygame Background")

# load the image
background_image = "images/tilebackground.jpg"

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

# draw shelves on screen
pygame.draw.rect(screen, lighter_brown, (left_shelf_x, shelf_y, shelf_width, shelf_height))
pygame.draw.rect(screen, lighter_brown, (right_shelf_x, shelf_y, shelf_width, shelf_height))

# set up shelf dividers
divider_width = 10
divider_height = 200
divider_y = 200

# set vertical divider x positions
left_divider_x = shelf_width / 2
right_divider_x = screen_width - (shelf_width / 2)

# draw vertical dividers on screen
pygame.draw.rect(screen, light_brown, (left_divider_x, divider_y, divider_width, divider_height))
pygame.draw.rect(screen, light_brown, (right_divider_x, divider_y, divider_width, divider_height))

# set up horizontal shelf dividers
h_divider_width = 200
h_divider_height = 10
h_divider_y = 300

# set divider x positions
left_h_divider_x = 0
right_h_divider_x = screen_width - shelf_width

# draw horizontal dividers on screen
pygame.draw.rect(screen, light_brown, (left_h_divider_x, h_divider_y, h_divider_width, h_divider_height))
pygame.draw.rect(screen, light_brown, (right_h_divider_x, h_divider_y, h_divider_width, h_divider_height))

# dictionary for toppings
toppings_info = [
    {"image_path": "images/candy.blue.png",
     "initial_position": (screen.get_width() // 2, screen.get_height() * 2 // 3),
     "scale_factor": 0.5}

]


class Toppings(pygame.sprite.Sprite):
    def __init__(self, screen, image, initial_position, scale_factor):
        super().__init__()

        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (
            int(self.image.get_width() * scale_factor), int(self.image.get_height() * scale_factor)))

        self.rect = self.image.get_rect()
        self.rect.center = initial_position
        self.screen = screen

        def draw(self):
            self.screen.blit(self.image, self.rect.topleft)

        toppings_sprites = []
        for topping in toppings_info:
            toppings_sprites.append(
                Toppings(screen, topping["image_path"], topping["initial_position"], topping["scale_factor"])
            )

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.blit(build_background(), (0, 0))

        for topping in toppings_sprites:    #error RIGHT HERE wtf
            topping.draw()

    pygame.display.update()


pygame.quit()
