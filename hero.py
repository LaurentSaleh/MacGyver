import pygame

class Hero(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.status = 0
        self.velocity = 40
        self.image = pygame.image.load('ressource/MacGyver.png')
        self.rect = self.image.get_rect()
        self.rect.x = 320
        self.rect.y = 0