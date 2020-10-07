import pygame
from hero import Hero
from badguy import Badguy

class Game:

    def __init__(self):
        self.hero = Hero()
        self.badguy = Badguy()
        self.pressed = { }