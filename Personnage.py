#!/usr/bin/python3
# -*- coding: Utf-8 -*

import Niveau

class Personnage:
    
    def __init__(self, niveau):
        self.niveau = niveau
        self.pos_x, self.pos_y = self.niveau.pos_depart

    def deplacer(self, deplacement):
        actions = {
            "d": lambda: (self.pos_x, self.pos_y+1),
            "q": lambda: (self.pos_x, self.pos_y-1),
            "z": lambda: (self.pos_x-1, self.pos_y),
            "s": lambda: (self.pos_x+1, self.pos_y),
        }
        pos_x, pos_y = actions[deplacement]()
        
        if self.niveau.est_permis((pos_x, pos_y)):
            self.pos_x, self.pos_y = pos_x, pos_y
            return (self.pos_x, self.pos_y)
        else:
            # On ne bouge pas
            return (self.pos_x, self.pos_y)
        
    
    def combat(self, pos_actuelle):
        if pos_actuelle == self.niveau.pos_arrivee:
            if self.niveau.outils.compteurObjets == 3:
                print("Vous avez tué le gardien. Vous êtes libre.")
                return False
            if self.niveau.outils.compteurObjets < 3:
                print("Vous êtes mort !")
                return False
            return True

    def obtenir_position(self):
        return self.pos_x, self.pos_y