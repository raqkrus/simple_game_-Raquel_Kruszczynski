import pygame

pygame.init()
running = True

# set dimensions
screen_width = 800
screen_height = 600

def welcome_screen():
    screen.fill((200,162,200))
    font = pygame.font.Font(None, 36)
    text1 = font.render("Chose a number of Layers for your Cake!", True, (255,255,255),(200,162,200))
    text2 = font.render("Welcome to the Bakery!", True, (255,255,255),(200,162,200))
    button1text = font.render("1", True, (204, 0, 102),(170,255,195))
    button2text = font.render("2", True, (204, 0, 102), (170, 255, 195))
    button3text = font.render("3", True, (204, 0, 102),(170,255,195))
    button_width = 100
    button_height = 50
    number_of_buttons = 3
    distance_from_bottom = 50
    button1_pos = (200-button_width/2,400)
    button2_pos = (400-button_width/2, 400)
    button3_pos = (600-button_width/2, 400)
    pygame.draw.rect(screen, (170, 255, 195), (button1_pos, (button_width, button_height))) # Replace with screen.blit("image", button1_pos)
    pygame.draw.rect(screen, (170, 255, 195), (button2_pos, (button_width, button_height)))
    pygame.draw.rect(screen, (170, 255, 195), (button3_pos, (button_width, button_height)))
    screen.blit(text1, (screen_width//2 - text1.get_width() // 2, screen_height // 2 - text1.get_height()//2))
    screen.blit(text2, (screen_width // 2 - text2.get_width() // 2, screen_height // 3 - text2.get_height() // 2))
    screen.blit(button1text, (240-button_width/2,410))
    screen.blit(button2text, (440 - button_width / 2, 410))
    screen.blit(button3text, (640 - button_width / 2, 410))
    start_game = False
    while start_game == False:
        mouse = pygame.mouse.get_pos()
        pygame.event.get()
        #If over button 1
        if button1_pos[0] < mouse[0] < button1_pos[0] + button_width and button1_pos[1] < mouse[1] < button1_pos[1] + button_height:
            print("Over Button 1!")
            if pygame.mouse.get_pressed()[0]: #0 and 1 for x and y pos, 0 for left mouse click
                start_game = True
                return 1
        if button2_pos[0] < mouse[0] < button2_pos[0] + button_width and button2_pos[1] < mouse[1] < button2_pos[1] + button_height:
            print("Over Button 2!")
            if pygame.mouse.get_pressed()[0]: #0 and 1 for x and y pos, 0 for left mouse click
                start_game = True
                return 2
        if button3_pos[0] < mouse[0] < button3_pos[0] + button_width and button3_pos[1] < mouse[1] < button3_pos[1] + button_height:
            print("Over Button 3!")
            if pygame.mouse.get_pressed()[0]: #0 and 1 for x and y pos, 0 for left mouse click
                start_game = True
                return 3

        pygame.display.update()

def build_background():
    background_image = pygame.image.load("images/purple_background.jpg")
    background = pygame.transform.scale(background_image, (screen_width, screen_height))
    return background


# get screen size/width
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pygame Background")

# load the image
# background_image = "images/purple_background.jpg"

# set color for table and shelves
light_brown = (196, 164, 132)
lighter_brown = (213, 193, 170)

# set size of table
table_width = screen_width
table_height = (2 / 3) * screen_height

# set y pos for table
table_y = (2 / 3) * screen_height

# set up shelves
shelf_width = 200
shelf_height = 200
shelf_y = 200

# set shelf x positions
left_shelf_x = 0
right_shelf_x = screen_width - shelf_width

# set up shelf dividers
divider_width = 10
divider_height = 200
divider_y = 200

# set vertical divider x positions
left_divider_x = shelf_width / 2
right_divider_x = screen_width - (shelf_width / 2)

# set up horizontal shelf dividers
h_divider_width = 200
h_divider_height = 10
h_divider_y = 300

# set divider x positions
left_h_divider_x = 0
right_h_divider_x = screen_width - shelf_width

# dictionary for toppings
toppings_info = [
    {"image_path": "images/candyBlue.png",
     "initial_position": (screen.get_width() // 2, screen.get_height() * 2 // 3),
     "scale_factor": 0.5}

]

toppings = pygame.sprite.Group()


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

        self.toppings_sprites = []
        for topping in toppings_info:
            self.toppings_sprites.append(
                Toppings(screen, topping["image_path"], topping["initial_position"], topping["scale_factor"])
            )

def draw_cake_layer(number_of_tiles, layer_number):
    center_of_screen = screen_width / 2
    # Draw the left and right of the layer
    screen.blit(cake_left, (center_of_screen - (number_of_tiles/2) * tile_length, table_height - tile_length * layer_number))
    screen.blit(cake_right, (center_of_screen + (number_of_tiles/2 - 1) * tile_length, table_height - tile_length * layer_number))
    # Draw the middle of the layer
    for tile in range(int((number_of_tiles - 2)/2)):  #-2 bc we already drew two tiles, divided by 2 bc were drawing two at same time
        screen.blit(cake_middle, (center_of_screen - (tile + 1) * tile_length, table_height - tile_length * layer_number))  # Middle tiles on the left of the screen
        screen.blit(cake_middle, (center_of_screen + (tile) * tile_length, table_height - tile_length * layer_number))  # Middle tiles on the right of the screen

number = welcome_screen()

topping = False  # I will remove this once I can draw toppings in the class

topping_positions = []

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    screen.blit(build_background(), (0, 0))

    # draw rectangle on screen
    pygame.draw.rect(screen, light_brown, (0, table_y, table_width, table_height))
    # draw shelves on screen
    pygame.draw.rect(screen, lighter_brown, (left_shelf_x, shelf_y, shelf_width, shelf_height))
    pygame.draw.rect(screen, lighter_brown, (right_shelf_x, shelf_y, shelf_width, shelf_height))
    # draw vertical dividers on screen
    pygame.draw.rect(screen, light_brown, (left_divider_x, divider_y, divider_width, divider_height))
    pygame.draw.rect(screen, light_brown, (right_divider_x, divider_y, divider_width, divider_height))
    # draw horizontal dividers on screen
    pygame.draw.rect(screen, light_brown, (left_h_divider_x, h_divider_y, h_divider_width, h_divider_height))
    pygame.draw.rect(screen, light_brown, (right_h_divider_x, h_divider_y, h_divider_width, h_divider_height))

    # Cake tiling system:
    cake_left = pygame.image.load("images/cakeLeft.png")
    cake_right = pygame.image.load("images/cakeRight.png")
    cake_middle = pygame.image.load("images/cakeMid.png")
    tile_length = cake_middle.get_height()
    candy_blue = pygame.image.load("images/candyBlue.png")
    candy_red = pygame.image.load("images/candyRed.png")
    candy_yellow = pygame.image.load("images/candyYellow.png")
    cherry = pygame.image.load("images/cherry.png")
    pinkcream = pygame.image.load("images/creamPink.png")
    vanillacream = pygame.image.load("images/creamVanilla.png")
    heart = pygame.image.load("images/heart.png")
    #load in other candy types here, then blit like below on other parts of shelf!

    # Draw toppings on shelves
    screen.blit(candy_blue, (20, 230))
    screen.blit(candy_red, (20, 330))
    screen.blit(candy_yellow, (120, 230))
    screen.blit(cherry, (620, 230))
    screen.blit(pinkcream, (720, 230))
    screen.blit(vanillacream, (620, 330))
    screen.blit(heart, (720, 330))
    if number >= 1:
        # Bottom Layer
        draw_cake_layer(6, 1)  # 6 = Number of tiles; 1 = 1st Layer
    if number >= 2:
        # Middle Layer
        draw_cake_layer(4, 2)
    if number >= 3:
        # Top Layer
        draw_cake_layer(2, 3)

    if pygame.key.get_pressed()[pygame.K_SPACE]:
        #toppings.add(Toppings(screen, "images/candyBlue.png", (200,200), 1))
        position = pygame.mouse.get_pos()
        position = (position[0] - candy_blue.get_width()/2, position[1] - candy_blue.get_height()/2) #positions candy to center of mouse click
        topping_positions.append(position)

    for i in topping_positions:
        print(topping_positions)
        screen.blit(candy_blue, i)


    pygame.display.update()

pygame.quit()
