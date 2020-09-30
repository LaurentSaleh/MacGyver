#! /usr/bin/env python3
# -*- coding: utf-8 -*-
import pygame
pygame.init()

# 1 Setting the scene
# open window
pygame.display.set_caption("Aaahmazeiiing !")
screen = pygame.display.set_mode((600, 600))

# load the maze frame
background = pygame.image.load('/Users/laurentsaleh1/Documents/GitHub/MacGyver/ressource/maze.png')

# display the maze frame
frame = True

# A while loop to keep the window open and up to date (So called "game loop")
while frame:

    # load background
    screen.blit(background, (0,0))

    # Update the screen
    pygame.display.flip()

    # if the player close the window
    if event in pygame.event.get():
        # event being closure of the window
        if event.type == pygame.QUIT:
            frame = False
            pygame.quit()


# close maze when Quit

# 1 - Créer le cadre de départ
# Commencez par créer le labyrinthe sans l’interface graphique. Quand la logique de votre labyrinthe est faite, utilisez le module PyGame pour dessiner l’interface graphique.
# La fenêtre du jeu sera un carré pouvant afficher 15 sprites sur la longueur.
# La structure (départ, emplacement des murs, arrivée), devra être enregistrée dans un fichier pour la modifier facilement au besoin.

# Puis intéressez-vous aux trois éléments principaux du jeu : le gardien, MacGyver et les objets. Comment les représenter dans votre programme ? Où sont-ils placés au commencement du jeu ?
# Les objets seront répartis aléatoirement dans le labyrinthe et changeront d’emplacement si l'utilisateur ferme le jeu et le relance.

# 2 - Animer le personnage. Le seul élément mouvant est MacGyver. Créez les méthodes de classe qui permettent de l'animer et de trouver la sortie. Pour l'instant, faites une version simplifiée du jeu dans laquelle MacGyver gagne en arrivant face au gardien.
# MacGyver sera contrôlé par les touches directionnelles du clavier.

# 3 - Récupérer les objets Ajoutez la gestion des objets. Comment MacGyver les ramasse-t-il ?  Ajoutez également un compteur qui les listera.
# Il récupèrera un objet simplement en se déplaçant dessus.

# 4 - Gagner ! Enfin, changez la fin du jeu : MacGyver gagne s'il a bien ramassé tous les objets et endormi le garde. Sinon, il perd.
# Le programme s'arrête uniquement si MacGyver a bien récupéré tous les objets et trouvé la sortie du labyrinthe. S'il n'a pas tous les objets et qu'il se présente devant le garde, il meurt (la vie est cruelle pour les héros).
