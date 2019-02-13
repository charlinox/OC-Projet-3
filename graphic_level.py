#!/usr/bin/python3
# coding: utf-8

import pygame as pg

from level import Level


class GraphicLevel(Level):
    """  Class redefines the display() method based
    on the inheritance of the Level class  """

    def __init__(self, file):
        super().__init__(file)

    def display(self):
        """  Method specifically redefined to display the maze graphically """

        """  Initializing and loading pictures  """
        windows = pg.display.get_surface()
        picture_background = pg.image.load(
            "images/background.jpg").convert()
        windows.blit(picture_background, (0, 0))
        """  Loading sprites  """
        pic_mac_gyver = pg.image.load(
            "images/mac_gyver.png").convert_alpha()
        pic_gardian = pg.image.load("images/gardian.png").convert_alpha()
        pic_wall = pg.image.load("images/wall.png").convert()
        pic_ether = pg.image.load("images/ether.png").convert()
        pic_tube = pg.image.load("images/tube.png").convert()
        pic_niddle = pg.image.load("images/niddle2.png").convert_alpha()
        pic_syringe = pg.image.load("images/syringe.png").convert()
        mask_wall = pg.image.load("images/mask_wall2.jpg").convert()
        pic_tube.set_colorkey((255, 255, 255))
        pic_syringe.set_colorkey((255, 255, 255))
        pic_ether.set_colorkey((1, 1, 1))

        for index_line in range(15):
            y = index_line * 40
            for index_col in range(15):
                x = index_col * 40
                if (index_line, index_col) in self.passages:
                    if (index_line, index_col) \
                            == self.mac_gyver.get_position():
                        windows.blit(pic_mac_gyver, (x, y))
                    elif (index_line, index_col) == self.tools.location_ether:
                        windows.blit(pic_ether, (x, y))  # Display of the ether
                    elif (index_line, index_col) == self.tools.location_tube:
                        windows.blit(pic_tube, (x, y))  # Display of the tube
                    elif (index_line, index_col) == self.tools.location_niddle:
                        # Display of the niddle
                        windows.blit(pic_niddle, (x, y))
                    elif (index_line, index_col) == self.pos_exit:
                        # Display of the guardian
                        windows.blit(pic_gardian, (x, y))
                else:
                    windows.blit(pic_wall, (x, y))

        # Pouch management
        windows.blit(mask_wall, (600, 0))
        if len(self.tools.pouch) < 3:
            if "E" in list(self.tools.pouch):
                windows.blit(pic_ether, (610, 50))
            if "T" in list(self.tools.pouch):
                windows.blit(pic_tube, (610, 100))
            if "N" in list(self.tools.pouch):
                windows.blit(pic_niddle, (610, 150))
        elif len(self.tools.pouch) == 3:
            windows.blit(mask_wall, (600, 0))
            windows.blit(pic_syringe, (600, 200))
