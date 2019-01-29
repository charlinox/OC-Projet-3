#!/usr/bin/python3
# coding: utf-8

import pygame
from pygame.locals import *

from graphic_level import GraphicLevel
from level import Level
from inputs import inputs


def screen_loop(picture):
    """ Welcome screen  """
    # Opening the Pygame window (900x1000 corresponds
    # to a maze of 15x15 squares of 60x60 pixels + tools banner)
    fenetre = pygame.display.set_mode((1000, 900))
    # !!! quand je veux mettre cette ligne dans main(), ca ne marche pas ?!?

    screen = pygame.image.load("images/" + picture).convert_alpha()
    pygame.display.set_caption("OC python project n°3")
    stay = True
    while stay:
        pygame.time.Clock().tick(100)
        fenetre.blit(screen, (0, 0))
        pygame.display.flip()
        if inputs() == "end":
            stay = False


def game_loop(level_num):
    """  The game !  """
    level_num.display()
    pygame.display.flip()

    stay = True
    while stay:
        move = inputs()
        if move in list((K_LEFT, K_UP, K_RIGHT, K_DOWN)):
            pos_current = level_num.mac_gyver.move(move)
            level_num.tools.pick_up(pos_current)
            stay = level_num.mac_gyver.fight(pos_current)                    
            if stay == "win":
                screen_loop("free.png")
                stay = False
            elif stay == "defeat":
                screen_loop("defeat.png")
                stay = False                    

            level_num.display()
            pygame.display.flip()
        elif move == "end":
            stay = False


def main():
    """  Main frame  """

    pygame.init()
    
    screen_loop("welcome_game.png")

    # Can choose a level and the console mode (Level) or graphic mode
    # (GraphicLevel) here
    level1 = GraphicLevel("level_2")

    # Setting up tools
    level1.tools.put(level1)

    game_loop(level1)


if __name__ == "__main__":
    main()
