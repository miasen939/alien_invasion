import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """a class that manage the bullet shot by ship"""
    def __init__(self, ai_settings, screen, ship):
        """create a bullte object at ship"""
        super(Bullet, self).__init__()
        self.screen = screen
    
        #set a rect at (0,0) as bullet first then set right positon
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width,
                ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        #the positon of bullet
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """update the location of bullet(upward)"""
        #update y
        self.y -=self.speed_factor
        #update the position of rect
        self.rect.y = self.y

    def draw_bullet(self):
        """draw bullet on screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)
