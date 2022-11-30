import pygame

class Ship():
    """a class of Ship in game"""
    def __init__(self,screen):
        """init ship and set location"""
        self.screen = screen

        #load ship image(.bmp) and get rectangle
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #set new ship on the center bottom of screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        """blit the ship at the pointed position"""
        self.screen.blit(self.image,self.rect) 
