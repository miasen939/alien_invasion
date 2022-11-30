import sys

import pygame

def run_game():
    #init game and create a screen object
    pygame.init()
    screen = pygame.display.set_mode((1200,800))
    pygame.display.set_caption("Alien Invasion!")

    #set background clolor
    bg_color = (230,230,230)

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

