#!/usr/bin/python3
# coding: utf-8
import random


class Items:
    """ Tool management represented by a set of three tuples
    containing the coordinates of the three objects.
    """

    def __init__(self):
        self.location_tools = None
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

    def pick_up(self, pos_current):
        """  The character picks up a tool while moving on it  """
        if pos_current in self.location_tools:
            self.object_counter += 1
            self.location_tools -= {pos_current}
