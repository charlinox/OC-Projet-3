#!/usr/bin/python3
# coding: utf-8

import pygame
from pygame.locals import *

from level import GraphicLevel
from inputs import Inputs


def main():
    pygame.init()
    fenetre = pygame.display.set_mode((900, 900))
    picture_background = pygame.image.load("images/background.jpg").convert()
    pygame.display.set_icon(picture_background)
    pygame.display.set_caption("OC python project n°3")
    level1 = GraphicLevel("level_2") # choix d'un mode console ou graphique ici ?
    level1.tools.put(level1)
    level1.display()
    
    stay = True
    while stay:
        movement = inputs()
        if movement in list(K_LEFT, K_UP, K_RIGHT, K_DOWN ):
            pos_current = level1.mac_gyver.move(movement)
            level1.tools.pick_up(pos_current)
            stay = level1.mac_gyver.fight(pos_current)
            level1.display()
            pygame.display.flip()
        elif movement == K_p:
            print("Vous vous êtes perdu dans le labyrinthe du python !")
            stay = False


if __name__ == "__main__":
    main()