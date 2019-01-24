#!/usr/bin/python3
# coding: utf-8

import sys

import pygame
from pygame.locals import *

class Inputs:
    """  Classe gérant les entrées clavier et souris.  """

    def __init__(self, level):
        stay = True

    while stay:
        pygame.time.Clock().tick(30)
		for event in pygame.event.get():		
			if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
				sys.exit()
			elif event.type == KEYDOWN:
                keyboard = event.key
                return (keyboard)