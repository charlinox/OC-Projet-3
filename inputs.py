#!/usr/bin/python3
# coding: utf-8

import pygame
from pygame.locals import *


def inputs():
    """  Class handling keyboard and mouse inputs  """

    pygame.time.Clock().tick(30)
    for event in pygame.event.get():
        if event.type == QUIT or event.type == KEYDOWN and event.key in list(
                (K_ESCAPE, K_c)):
            return "end"
        elif event.type == KEYDOWN:
            return event.key
