#!/usr/bin/python3
# coding: utf-8

import random

class Level:
    """ Class representing the level of the maze. """
		
    def __init__(self, file):
        self.file = file
        self.passages = set()
        self.start = set()
        self.exit = set()
        self.read_file()
        self.mac_gyver = Character(self) 
        self.tools = Items()
        
		        
    def read_file(self):
        """ Method for reading the file by creating a set containing the tuples of the coordinates of the empty spaces (the passages).
        """
        
        with open(self.file) as f:

            for i, ligne in enumerate(f):
                for j, col in enumerate(ligne):
                    if col == '0':
                        self.passages.add((i, j))
                    elif col == 'd':
                        self.start.add((i,j))
                        self.passages.add((i, j))
                    elif col == 'a':
                        self.exit.add((i, j))
                        self.passages.add((i, j))

    
    def display(self):
        """ Display the maze in consol. """
        
        maze = ""
        for index_line in range(15):
            for index_col in range(15):
                if (index_line, index_col) in self.passages:                    
                    if (index_line, index_col) == self.mac_gyver.get_position():
                        maze += "P" # affichage du mac_gyver #                 
                    elif (index_line, index_col) in self.tools.location_tools:
                        maze += "O" # affichage de trois tools génériques #
                    elif (index_line, index_col) == self.pos_exit:
                        maze += "G" # affichage du gardien #
                    else:
                        maze += " " # affichage d'un couloir vide #
                else:
                    maze += "X" # affichage d'un mur #
            maze += "\n"
        
        print(maze)

    def is_allowed(self, position):
        return  position in self.passages
    
    @property
    def pos_start(self):        
        return list(self.start)[0]
    
    @property
    def pos_exit(self):        
        return list(self.exit)[0]

class Items:
    """ Tool management represented by a set of three tuples containing the coordinates of the three objects.
    """
    
    def __init__(self):
        self.location_tools = None
        self.object_counter = 0
        
    def put(self, level):
        """ Creation of a set containing the coordinates of the three tools to pick_up. 
        """
        
        passages = level #.passages  ? # Copie pour manipulation.  #
        self.location_tools = set(
            random.sample(
                level.passages - {level.pos_start, level.pos_exit}, 
                3
            )
        )
        
    def pick_up(self, pos_current):
        if pos_current in self.location_tools:
            self.object_counter += 1
            self.location_tools -= {pos_current}
            

class Character:
    
    def __init__(self, level):
        self.level = level
        self.pos_x, self.pos_y = self.level.pos_start

    def move(self, movement):
        actions = {
            "d": lambda: (self.pos_x, self.pos_y+1),
            "q": lambda: (self.pos_x, self.pos_y-1),
            "z": lambda: (self.pos_x-1, self.pos_y),
            "s": lambda: (self.pos_x+1, self.pos_y),
        }
        pos_x, pos_y = actions[movement]()
        
        if self.level.is_allowed((pos_x, pos_y)):
            self.pos_x, self.pos_y = pos_x, pos_y
            return (self.pos_x, self.pos_y)
        else:
            # On ne bouge pas
            return (self.pos_x, self.pos_y)
        
    
    def fight(self, pos_current):
        if pos_current == self.level.pos_exit and self.level.tools.object_counter == 3:
            print("Vous avez tué le gardien. Vous êtes libre.")
            return False
        elif pos_current == self.level.pos_exit and self.level.tools.object_counter < 3:
            print("Vous êtes mort !")
            return False
        return True

    def get_position(self):        
        return self.pos_x, self.pos_y
    
def main():
    
    level1 = Level("level_2")
    level1.tools.put(level1)
    level1.display()
    
    stay = True
    while stay:
        
        movement = input(
            "Veuillez entrer une lettre pour déput Mac Gyver (d, q, z, s) : "
        ).lower()
        if movement in list("dqzs"):
            
            pos_current = level1.mac_gyver.move(movement)       
            level1.tools.pick_up(pos_current)
            stay = level1.mac_gyver.fight(pos_current)

            level1.display()
        elif movement == "p":
            print("Vous vous êtes perdu dans le labyrinthe du python !")
            stay = False
        

if __name__ == "__main__":
    main()
