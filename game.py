#!/usr/bin/python3
# coding: utf-8

import pygame
from pygame.locals import *

from graphic_level import GraphicLevel
from level import Level
from inputs import inputs


class Game:
    """ Class redefines the display() method based on the inheritance of the Level class """

    def __init__(self, level_path):
        pygame.init()
        self.level_path = level_path

    def screen_loop(self, picture):
        """ Welcome screen  """

        windows = pygame.display.get_surface()
        screen = pygame.image.load("images/" + picture).convert_alpha()
        pygame.display.set_caption("OC python project n°3")
        stay = True
        while stay:
            pygame.time.Clock().tick(100)
            windows.blit(screen, (0, 0))
            pygame.display.flip()
            if inputs() == "end":
                stay = False


    def game_loop(self, level_num):
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
                level_num.display()
                pygame.display.flip()
                if stay == "win":
                    self.screen_loop("free.png")
                    stay = False
                elif stay == "defeat":
                    self.screen_loop("defeat.png")
                    stay = False
            elif move == "end":
                stay = False

    def start(self):
        """  Main frame  """
        
        # Opening the Pygame window (660x600 corresponds
        # to a maze of 15x15 squares of 40x40 pixels + tools banner)
        windows = pygame.display.set_mode((660, 600))

        self.screen_loop("welcome_game.png")

        # Can choose a level and the console mode (Level) or graphic mode
        # (GraphicLevel) here
        game_level = GraphicLevel(self.level_path)

        # Setting up tools
        game_level.tools.put(game_level)

        self.game_loop(game_level)