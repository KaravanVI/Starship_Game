import pygame

class Bullet(pygame.sprite.Sprite):
    def __init__(self, screen, gun):
        super().__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, 4, 12)
        self.color = (255, 255, 0)
        self.speed = 5
        self.rect.centerx = gun.rect.centerx
        self.rect.top = gun.rect.top
        self.y = float(self.rect.y)

    def update(self):
        self.y -= self.speed
        self.rect.y = self.y

    @property
    def image(self):
        surface = pygame.Surface((self.rect.width, self.rect.height))
        surface.fill(self.color)
        return surface