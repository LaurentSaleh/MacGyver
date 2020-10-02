#! /usr/bin/env python3
# -*- coding: utf-8 -*-
import pygame
pygame.init()
from game import Game   

# 1 Setting the scene
# open window
pygame.display.set_caption("Aaahmazeiiing !")
screen = pygame.display.set_mode((600, 600))

# load the maze frame
background = pygame.image.load('ressource/maze.png')

# load hero
hero = Hero()

# display the maze frame
frame = True

# A while loop to keep the window open and up to date (So called "game loop")
while frame:

    # load background
    screen.blit(background, (0,0))

    # load hero
    screen.blit(game.hero.image, game.hero.rect)

    # Update the screen
    pygame.display.flip()

    # if the player close the window
    if event in pygame.event.get():
        # event being closure of the window
        if event.type == pygame.QUIT:
            frame = False
            pygame.quit()


# close maze when Quit

#2 - Setting the caracters
    #2-1 Create class hero
        #load hero on the screen at starting point
        #enable hero movements
        #calculate hero status
        #Update the screen
    #2-2 Create class badguy
        # load hero on the screen at finish
        # Update the screen

# 3 Create class tools
        # Upload tools (sringe, needle, ether) at random place, start and finish excluded
        # Update the screen

# 4 Create class game
        # Load maze matrix
        # Set hero position rect
        # Compare hero position from badguy and if status = 3 AND rect <= 1, then display "win" screen, if not display "RIP" screen (end game)
        # Compare hero position from tools and if rect <= 1, then gives tools (update hero status)