#!/usr/bin/python3
# coding: utf-8

from pygame import *


class Character:
    """  Class of the character who can move and fight  """

    def __init__(self, level):
        self.level = level
        self.pos_x, self.pos_y = self.level.pos_start

    def move(self, movement):
        """  Moving the character  """
        actions = {
            K_RIGHT: lambda: (self.pos_x, self.pos_y + 1),
            K_LEFT: lambda: (self.pos_x, self.pos_y - 1),
            K_UP: lambda: (self.pos_x - 1, self.pos_y),
            K_DOWN: lambda: (self.pos_x + 1, self.pos_y),
        }
        pos_x, pos_y = actions[movement]()

        if self.level.is_allowed((pos_x, pos_y)):
            self.pos_x, self.pos_y = pos_x, pos_y
            return (self.pos_x, self.pos_y)
        else:
            #  No moves
            return (self.pos_x, self.pos_y)

    def fight(self, pos_current):
        """  The character wins the fight if he arrives on the guardian
        with the three tools in his possession  """
        if pos_current == self.level.pos_exit:
            if self.level.tools.object_counter == 3:
                return "win"
            elif self.level.tools.object_counter < 3:
                return "defeat"
        return True

    def get_position(self):
        """  Return the character position  """
        return self.pos_x, self.pos_y
