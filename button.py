import pygame.font

class Button:
    def __init__(self, ai_game, msg):
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        #dimensions and settinbgs of button
        self.width, self.height = 200, 50
        self.button_color = (0,255,0)
        self.text_color = (255,255,255)
        self.font = pygame.font.SysFont(None,48) #None = default font style and 48 is size

        #Building button of rect object and in centre
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        #the button msg needs to be popped only once
        self._prep_msg(msg)
    def _prep_msg(self, msg):
        self.msg_image = self.font.render(msg, True, self.text_color, 
        self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center
    def draw_button(self):
        #Draw blank button then msg
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
