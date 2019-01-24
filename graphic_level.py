#!/usr/bin/python3
# coding: utf-8

import pygame
from pygame.locals import *

from character import Character
from items import Items


class GraphicLevel(Level):
    """ Classe redéfinisant la méthode d'affichage dysplay() en s'appuyant sur l'héritage de la classe Level. """
    def __init__(self, file):
        super().__init__(file)
        self.items = {}



    def display(self):
        """  Méthode spécifiquement redéfinie pour afficher graphiquement le maze. """ 
        
        """  Initialisation et chargement de l'image de fond.  """ 
        
        #Ouverture de la fenêtre Pygame (900 par 900 correspond à un maze 15x15 de cases de 60x60)
        fenetre = pygame.display.get_surface()
        picture_background = pygame.image.load("images/background.jpg").convert()
        fenetre.blit(picture_background, (0,0))


        """  Chargement des sprite  """
        pic_character = pygame.image.load("images/MacGyver.png").convert()
        pic_gardian = pygame.image.load("images/gardian.png").convert()
		pic_wall = pygame.image.load("images/wall.png").convert()
		pic_start = pygame.image.load("images/start.png").convert()
		pic_generic_tool = pygame.image.load("images/generic_tool.png").convert()
        # empty = pygame.image.load(empty.png).convert() probablement pas à définir

        # maze = ""
        for index_line in range(15):
            x = index_line * 60
            for index_col in range(15):
                y = index_col * 60
                if (index_line, index_col) in self.passages:
                    if (index_line, index_col) \
                            == self.mac_gyver.get_position():                        
                        fenetre.blit(pic_character, (x,y))                        
                    elif (index_line, index_col) in self.tools.location_tools:
                        fenetre.blit(pic_generic_tool, (x,y))
                        self.items[x, y] = pic_generic_tool
                    elif (index_line, index_col) == self.pos_exit:
                        fenetre.blit(pic_gardian, (x,y))
                    # else:                        
                        # Dislay of a empty passage
                        # fenetre.blit(empty, (x,y))
                else:
                    fenetre.blit(pic_wall, (x,y))
            # maze += "\n"

        # fenetre.blit(picture_background, (0,0))