import sys

import pygame

def check_events(ship):
    """response keyboard and mouse event"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False

def update_screen(ai_settings, screen, ship):
    """refresh image on screen and switch into new screen"""
    #repainting screen every loop
    screen.fill(ai_settings.bg_color)
    ship.blitme()

    #set screen visible
    pygame.display.flip()
