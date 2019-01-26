#!/usr/bin/python3
# coding: utf-8

import pygame
from pygame.locals import *

from graphic_level import GraphicLevel
from inputs import inputs


def welcome_loop():
    """ Welcome screen  """
    pygame.init()
    # Opening the Pygame window (900x1000 corresponds
    # to a maze of 15x15 squares of 60x60 pixels + tools banner)
    fenetre = pygame.display.set_mode((900, 1000))
    welcome_game = pygame.image.load("images/welcome_game.png").convert()
    pygame.display.set_caption("OC python project n°3")
    stay = True
    while stay:
        pygame.time.Clock().tick(100)
        fenetre.blit(welcome_game, (0, 0))
        pygame.display.flip()
        if stay:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    stay = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        stay = False
                    elif event.key == pygame.K_c:
                        stay = False
                elif event.type == pygame.MOUSEBUTTONDOWN \
                        and event.button == 1:
                    stay = False


def game_loop(level1):
    """  The game !  """
    #picture_background = pygame.image.load("images/background.jpg").convert()
    level1.display()
    pygame.display.flip()

    stay = True
    while stay:
        movement = inputs()
        if movement in list((K_LEFT, K_UP, K_RIGHT, K_DOWN)):
            pos_current = level1.mac_gyver.move(movement)
            level1.tools.pick_up(pos_current)
            stay = level1.mac_gyver.fight(pos_current)
            level1.display()
            pygame.display.flip()
        elif movement == K_p:
            print("Vous vous êtes perdu dans le labyrinthe du python !")
            stay = False


def main():
    """  Main frame  """

    # Can choose a level and the console mode (Level) or graphic mode
    # (GraphicLevel) here
    level1 = GraphicLevel("level_2")
    # Setting up tools
    level1.tools.put(level1)

    welcome_loop()
    game_loop(level1)


if __name__ == "__main__":
    main()
