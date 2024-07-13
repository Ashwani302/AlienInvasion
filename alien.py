import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """This is to manage aliens"""
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        #importing image
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        #setting position of alien
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #Store a decimal value for the alien.
        self.x = float(self.rect.x)
    def check_edges(self):
        """Return True if alien is at edge of screen"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def update(self):
        """moving alien to the right"""
        self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.x = self.x
        
