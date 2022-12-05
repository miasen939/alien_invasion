import sys

import pygame

from bullet import Bullet

from alien import Alien

def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """reponse to keydown"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()

def fire_bullet(ai_settings, screen, ship, bullets):
    """if dont reach limit shot one"""
    #create new bullet, add it into group
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

def check_keyup_events(event, ship):
    """reponse to keyup"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(ai_settings, screen, ship, bullets):
    """response keyboard and mouse event"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

def update_screen(ai_settings, screen, ship, aliens,bullets):
    """refresh image on screen and switch into new screen"""
    #repainting screen every loop
    screen.fill(ai_settings.bg_color)
    #repaint all bullet at ship and alien
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)

    #set screen visible
    pygame.display.flip()

def update_bullets(bullets):
    """update position of bullets and delete the out-of-screen bulles"""
    #update the position
    bullets.update()
    
    #delete bullets
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

def get_number_rows(ai_settings, ship_height, alien_height):
    """caculate how many aliens screen can contain"""
    avaliable_space_y = (ai_settings.screen_height - 
            (3 * alien_height) - ship_height)
    number_rows = int(avaliable_space_y / (2 * alien_height))
    return number_rows

def get_number_aliens_x(ai_settings, alien_width):
    """caculate how mant aliens can one line cotains"""
    avaliable_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(avaliable_space_x / (2 * alien_width))
    return number_aliens_x

def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    """create an alien and add it into line"""
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)

def create_fleet(ai_settings, screen, ship, aliens):
    """create a fleet of aliens"""
    #create an alien and calculate how manys aliens can one line cotains
    #the distance of near aliens is the width of one alien
    alien = Alien(ai_settings, screen)
    number_alien_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)
    #create fleet
    for row_number in range(number_rows):
        for alien_number in range(number_alien_x):
            #create an alien and add it into the right line
            create_alien(ai_settings, screen, aliens, alien_number, row_number)
