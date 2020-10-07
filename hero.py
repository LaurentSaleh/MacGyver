import pygame

class Hero(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.status = 0
        self.velocity = 40
        self.image = pygame.image.load('ressource/MacGyver.png')
        self.rect = self.image.get_rect()
        self.rect.x = 280
        self.rect.y = 0

    def move_right(self):
        self.rect.x += self.velocity

    def move_left(self):
        self.rect.x -= self.velocity

    def move_up(self):
        self.rect.y -= self.velocity

    def move_down(self):
        self.rect.y += self.velocity