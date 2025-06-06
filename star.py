import pygame
import random

class Star(pygame.sprite.Sprite):
    def __init__(self, screen):
        super().__init__()
        self.screen = screen
        self.image = pygame.image.load(self.resource_path('images/star.png'))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, screen.get_width() - self.rect.width)
        self.rect.y = random.randint(-100, -40)
        self.speed = random.uniform(1.5, 3.0)

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > self.screen.get_height():
            self.kill()

    def resource_path(self, relative):
        import os
        return os.path.join(os.path.dirname(__file__), relative)