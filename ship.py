
import pygame

class Ship:
    """This class is to manage ship"""
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
        

        

        #load the ship image and get its rect.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        #Start each new ship at the bottom of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        #Store a decimal value for the ship's horizontal position.
        self.x = float(self.rect.x)
        



        #Key Movement
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        

    def update(self):
        """update the ship positions"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        if self.moving_up and self.rect.top >0:
            self.rect.y -= self.settings.ship_speed1
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.y += self.settings.ship_speed1

        
        
        self.rect.x = self.x
        

    def blitme(self):
        """Draw ship at its current location"""
        self.screen.blit(self.image, self.rect)
    def center_ship(self):
        """ship at center"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)