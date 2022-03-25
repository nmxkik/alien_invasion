import pygame
class Ship():

    def __init__(self, ai_settings, screen):
        #initialize spaceship and its location
        self.screen = screen
        self.ai_settings = ai_settings

        # load bmp image and get rectangle
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #put spaceship on the bottom of window
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.center = float(self.rect.centerx)

        #flag moving
        self.moving_right = False
        self.moving_left = False

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
        
        self.rect.centerx = self.center

    def blitme(self):
        #buld the spaceship at the specific location
        self.screen.blit(self.image,self.rect)