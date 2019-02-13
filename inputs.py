#!/usr/bin/python3
# coding: utf-8

import pygame as pg


def inputs():
    """  Class handling keyboard and mouse inputs  """

    pg.time.Clock().tick(30)
    for event in pg.event.get():
        if event.type == pg.QUIT or event.type == pg.KEYDOWN and event.key in list(
                (pg.K_ESCAPE, pg.K_c)):
            return "end"
        elif event.type == pg.KEYDOWN:
            return event.key
