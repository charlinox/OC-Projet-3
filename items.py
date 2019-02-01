#!/usr/bin/python3
# coding: utf-8
import random


class Items:
    """ Tool management represented by a set of three tuples
    containing the coordinates of the three objects.
    """

    def __init__(self):
        self.location_tools = None
        self.location_ether = None
        self.location_tube = None
        self.location_niddle = None
        self.pouch = ""
        self.object_counter = 0

    def put(self, level):
        """ Creation of a set containing the coordinates of the
        three tools to pick_up.
        """

        self.location_tools = set(
            random.sample(
                level.passages - {level.pos_start, level.pos_exit},
                3
            )
        )
        tools = iter(self.location_tools)
        self.location_ether = next(tools)
        self.location_tube = next(tools)
        self.location_niddle = next(tools)

    def pick_up(self, pos_current):
        """  The character picks up a tool while moving on it  """
        if pos_current in self.location_tools:
            if pos_current == self.location_ether:
                self.location_ether = None
                self.pouch += "E"
            elif pos_current == self.location_tube:
                self.location_tube = None
                self.pouch += "T"
            elif pos_current == self.location_niddle:
                self.location_niddle = None
                self.pouch += "N"
            self.object_counter += 1
            self.location_tools -= {pos_current}
