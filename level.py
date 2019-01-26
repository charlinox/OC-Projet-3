#!/usr/bin/python3
# coding: utf-8

from character import Character
from items import Items


class Level:

    def __init__(self, file):
        self.file = file
        self.passages = set()
        self.start = set()
        self.exit = set()
        self.read_file()
        self.mac_gyver = Character(self)
        self.tools = Items()

    def read_file(self):
        """  Read the maze file by creating a set containing
        the tuples of the coordinates of empty spaces (passages)  """
        with open(self.file) as f:

            for i, ligne in enumerate(f):
                for j, col in enumerate(ligne):
                    if col == '0':
                        self.passages.add((i, j))
                    elif col == 'd':
                        self.start.add((i, j))
                        self.passages.add((i, j))
                    elif col == 'a':
                        self.exit.add((i, j))
                        self.passages.add((i, j))

    def display(self):
        """  Display the maze in console mode  """
        maze = ""
        for index_line in range(15):
            for index_col in range(15):
                if (index_line, index_col) in self.passages:
                    if (index_line, index_col) \
                            == self.mac_gyver.get_position():
                        maze += "P"  # Display of the charachter
                    elif (index_line, index_col) in self.tools.location_tools:
                        maze += "O"  # Display of the three generic tools
                    elif (index_line, index_col) == self.pos_exit:
                        maze += "G"  # Diplay of the gardian
                    else:
                        maze += " "  # Dislay of a empty passage
                else:
                    maze += "X"  # Display of a wall
            maze += "\n"
        print(maze)

    def is_allowed(self, position):
        """  Wall collision test  """
        return position in self.passages

    @property
    def pos_start(self):
        return list(self.start)[0]

    @property
    def pos_exit(self):
        return list(self.exit)[0]
