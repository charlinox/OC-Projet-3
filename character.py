#!/usr/bin/python3
# coding: utf-8


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
            #  No moves
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