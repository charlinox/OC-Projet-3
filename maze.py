#!/usr/bin/python3
# coding: utf-8

from level import Level


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