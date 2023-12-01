import pygame


def draw_cake_layer(screen, cake_left, cake_middle, cake_right, number_of_tiles, tile_length, table_height):
    screen_width = screen.get_width()
    center_of_screen = screen_width / 2
        #draw left and right layers
    screen.blit(cake_left, (center_of_screen - (number_of_tiles / 2) * tile_length, table_height - tile_length * layer_number))
    screen.blit(cake_right, (center_of_screen + (number_of_tiles / 2 - 1) * tile_length, table_height - tile_length * layer_number))

    # Draw the middle of the layer
    for tile in range(int((number_of_tiles - 2) / 2)):
        screen.blit(cake_middle, (center_of_screen - (tile + 1) * tile_length, table_height - tile_length * layer_number))  # Middle tiles on the left of the screen
        screen.blit(cake_middle, (center_of_screen + tile * tile_length, table_height - tile_length * layer_number))  # Middle tiles on the right of the screen

