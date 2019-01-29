#!/usr/bin/python3
# coding: utf-8

import pygame
from pygame.locals import *

from character import Character
from items import Items
from level import Level
from inputs import inputs

#from maze import screen_loop


class GraphicLevel(Level):
    """ Class redefines the display() method based on the inheritance of the Level class """

    def __init__(self, file):
        super().__init__(file)
        #self.items = {}

    def display(self):
        """  Method specifically redefined to display the maze graphically """

        """  Initializing and loading pictures  """
        fenetre = pygame.display.get_surface()
        picture_background = pygame.image.load(
            "images/background.jpg").convert()
        fenetre.blit(picture_background, (0, 0))
        """  Loading sprites  """
        pic_mac_gyver = pygame.image.load(
            "images/mac_gyver.png").convert_alpha()
        pic_gardian = pygame.image.load("images/gardian.png").convert_alpha()
        pic_wall = pygame.image.load("images/wall.png").convert()
        pic_ether = pygame.image.load("images/ether.png").convert()
        pic_tube = pygame.image.load("images/tube.png").convert()
        pic_niddle = pygame.image.load("images/niddle.png").convert_alpha()
        pic_syringe = pygame.image.load("images/syringe.png").convert()
        pic_free = pygame.image.load("images/free.png").convert_alpha()
        pic_defeat = pygame.image.load("images/defeat.png").convert_alpha()
        # Makes transparent the color white (RGB value: 255,255,255) of the picture
        pic_tube.set_colorkey((255, 255, 255))
        pic_syringe.set_colorkey((255, 255, 255))
        pic_ether.set_colorkey((1, 1, 1))


        for index_line in range(15):
            # Inversion of x and y in graphical representation
            y = index_line * 40
            for index_col in range(15):
                x = index_col * 40
                if (index_line, index_col) in self.passages:
                    if (index_line, index_col) \
                            == self.mac_gyver.get_position():
                        fenetre.blit(pic_mac_gyver, (x, y))
                    # elif (index_line, index_col) in self.tools.location_tools:
                    #     fenetre.blit(pic_ether, (x, y))
                        #self.items[x, y] = pic_generic_tool
                    elif (index_line, index_col) == self.tools.location_ether:
                        fenetre.blit(pic_ether, (x, y))  # Display of the ether
                    elif (index_line, index_col) == self.tools.location_tube:
                        fenetre.blit(pic_tube, (x, y))  # Display of the tube
                    elif (index_line, index_col) == self.tools.location_niddle:
                        fenetre.blit(pic_niddle, (x, y))  # Display of the niddle
                    elif (index_line, index_col) == self.pos_exit:
                        fenetre.blit(pic_gardian, (x, y))  # Display of the guardian
                else:
                    fenetre.blit(pic_wall, (x, y))

        #if "E" in list(self.tools.pouch):


        # if self.mac_gyver.fight == "win":
        #     fenetre.blit(pic_free, (0, 0))  # you win
        #     #pygame.time.Clock().tick(300)
        #     while stay:
        #         if inputs() == "end":
        #             stay = False
        #     #screen_loop("images/free.png")

        # elif self.mac_gyver.fight == "defeat":
        #     fenetre.blit(pic_defeat, (0, 0))  # you loose
        #     #pygame.time.Clock().tick(300)
        #     while stay:
        #         if inputs() == "end":
        #             stay = False
