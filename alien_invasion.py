import sys

import pygame

from settings import Settings

def run_game():
    #init game and create a screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
            (ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion!")

    #set background clolor
    bg_color = (ai_settings.bg_color)

    #main loop of game
    while True:

        #monitor keyboard and mouse event
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                sys.exit()
        
        #flip screen for every loop
        screen.fill(bg_color)

        #set last paint screen visible
        pygame.display.flip()

run_game()

