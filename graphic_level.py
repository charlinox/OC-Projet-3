#!/usr/bin/python3
# coding: utf-8

import pygame
from pygame.locals import *

from character import Character
from items import Items
from level import Level


class GraphicLevel(Level):
    """ Class redefines the display() method based on the inheritance of the Level class """
    def __init__(self, file):
        super().__init__(file)
        self.items = {}

    def display(self):
        """  Method specifically redefined to display the maze graphically """ 
        
        """  Initializing and loading the background image  """        
        fenetre = pygame.display.get_surface()
        picture_background = pygame.image.load("images/background.jpg").convert()
        fenetre.blit(picture_background, (0,0))
        """  Loading sprites  """
        pic_mac_gyver = pygame.image.load("images/mac_gyver.png").convert_alpha()
        pic_gardian = pygame.image.load("images/gardian.png").convert_alpha()
        pic_wall = pygame.image.load("images/wall.png").convert()
        pic_ether = pygame.image.load("images/tube_plastique.png").convert()
        pic_ether.set_colorkey((255,255,255)) #Rend le blanc (valeur RGB : 255,255,255) de l'image transparent

        for index_line in range(15):
            y = index_line * 60
            for index_col in range(15):
                x = index_col * 60
                if (index_line, index_col) in self.passages:
                    if (index_line, index_col) \
                            == self.mac_gyver.get_position():                        
                        fenetre.blit(pic_mac_gyver, (x,y))                        
                    elif (index_line, index_col) in self.tools.location_tools:
                        fenetre.blit(pic_ether, (x,y))
                        #self.items[x, y] = pic_generic_tool
                    elif (index_line, index_col) == self.pos_exit:
                        fenetre.blit(pic_gardian, (x,y))
                else:
                    fenetre.blit(pic_wall, (x,y))