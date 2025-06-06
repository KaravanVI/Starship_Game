import pygame

class Gun:
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load(self.resource_path('images/pixil-frame-0.png'))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.moving_right = False
        self.moving_left = False
        self.speed = 5

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.centerx += self.speed
        if self.moving_left and self.rect.left > 0:
            self.rect.centerx -= self.speed

    def output(self):
        self.screen.blit(self.image, self.rect)

    def resource_path(self, relative):
        import os
        return os.path.join(os.path.dirname(__file__), relative)