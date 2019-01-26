#!/usr/bin/python3
# coding: utf-8

import sys

import pygame
from pygame.locals import *


def inputs():
    """  Class handling keyboard and mouse inputs  """

    pygame.time.Clock().tick(30)
    for event in pygame.event.get():
        if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
            return K_p
        elif event.type == KEYDOWN:
            return event.key
