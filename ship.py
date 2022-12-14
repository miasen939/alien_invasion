import pygame


class Ship():
    """a class of Ship in game"""
    def __init__(self, ai_settings, screen):
        """init ship and set location"""
        self.screen = screen
        self.ai_settings = ai_settings

        #load ship image(.bmp) and get rectangle
        self.image = pygame.image.load('images/ship2.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #set new ship on the center bottom of screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        
        #load propety center
        self.center = float(self.rect.centerx)

        #sign of movment
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """adjust ships location according to sign"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor 
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        #update rect by center
        self.rect.centerx = self.center

    def blitme(self):
        """blit the ship at the pointed position"""
        self.screen.blit(self.image,self.rect) 
