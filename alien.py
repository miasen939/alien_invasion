import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """a single alien class"""

    def __init__(self, ai_settings, screen):
        """init alien set"""
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        #load alien image, set it as rect
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        #every alien first formed at (0,0) 
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #storge the right position of alien
        self.x = float(self.rect.x)

    def blitme(self):
        """paint alien at pointed position"""
        self.screen.blit(self.image, self.rect)
