#!/usr/bin/python3
# coding: utf-8

import pygame as pg

from graphic_level import GraphicLevel
from inputs import inputs


class Game:
    """ class integrating the initialization and the main frames of the game """

    def __init__(self, level_path):
        pg.init()
        self.level_path = level_path

    def screen_loop(self, picture):
        """ Welcome screen  """

        windows = pg.display.get_surface()
        screen = pg.image.load("images/" + picture).convert_alpha()
        pg.display.set_caption("OC python project n°3")
        stay = True
        while stay:
            pg.time.Clock().tick(100)
            windows.blit(screen, (0, 0))
            pg.display.flip()
            if inputs() == "end":
                stay = False

    def game_loop(self, level_num):
        """  The game !  """
        level_num.display()
        pg.display.flip()

        stay = True
        while stay:
            move = inputs()
            if move in list((pg.K_LEFT, pg.K_UP, pg.K_RIGHT, pg.K_DOWN)):
                pos_current = level_num.mac_gyver.move(move)
                level_num.tools.picpg.K_UP(pos_current)
                stay = level_num.mac_gyver.fight(pos_current)
                level_num.display()
                pg.display.flip()
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

        # Opening the pg window (660x600 corresponds
        # to a maze of 15x15 squares of 40x40 pixels + tools banner)
        pg.display.set_mode((660, 600))

        self.screen_loop("welcome_game.png")

        # Can choose a level and the console mode (Level) or graphic mode
        # (GraphicLevel) here
        game_level = GraphicLevel(self.level_path)

        # Setting up tools
        game_level.tools.put(game_level)

        self.game_loop(game_level)
