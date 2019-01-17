#!/usr/bin/python3
# -*- coding: Utf-8 -*

import random
import pygame
from pygame.locals import *

from ElementsFixes import *
from Personnage import *
from Niveau import *

def main():
    
    niveau1 = Niveau("level_2")
    niveau1.outils.placer(niveau1)
    niveau1.afficher()
    
    #BOUCLE PRINCIPALE
    continuer = True
    while continuer:
        
        deplacement = input(
            "Veuillez entrer une lettre pour déplacer Mac Gyver (d, q, z, s et p pour sortir) : "
        ).lower()
        if deplacement in list("dqzs"):
            
            pos_actuelle = niveau1.personnage.deplacer(deplacement)       
            niveau1.outils.ramasser(pos_actuelle)
            continuer = niveau1.personnage.combat(pos_actuelle)

            niveau1.afficher()
        elif deplacement == "p":
            print("Vous vous êtes perdu dans le labyrinthe du python !")
            continuer = False
        

main()
