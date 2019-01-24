#!/usr/bin/python3
# coding: utf-8

from level import GraphicLevel


def main():

    level1 = GraphicLevel("level_2")
    level1.tools.put(level1)
    level1.display()
    
    stay = True
    while stay:
        movement = Inputs() # Insérer un masque pour enlever "K_"
            if movement in list("K_LEFT", "K_UP", "K_RIGHT", "K_DOWN" ):
                pos_current = level1.mac_gyver.move(movement)
                level1.tools.pick_up(pos_current)
                stay = level1.mac_gyver.fight(pos_current)
                level1.display()
            elif movement == "p":
                print("Vous vous êtes perdu dans le labyrinthe du python !")
                stay = False

if __name__ == "__main__":
    main()