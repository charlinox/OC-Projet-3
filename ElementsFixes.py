#!/usr/bin/python3
# coding: utf-8
import random


class ElementsFixes:
    """ Gestion des outils représenté par un set de trois tuples contenant les 
    coordoonées des trois objets. """
    def __init__(self):
        self.emplacement_outils = None
        self.compteurObjets = 0
        
    def placer(self, niveau):
        """ Création d'un set contenant les coordoonées des trois outils à ramasser. """
        couloirs = niveau # Copie pour manipulation
        self.emplacement_outils = set(
            random.sample(
                niveau.couloirs - {niveau.pos_depart, niveau.pos_arrivee}, 
                3
            )
        )
        
    def ramasser(self, pos_actuelle):
        if pos_actuelle in self.emplacement_outils:
            self.emplacement_outils -= set(pos_actuelle)
            self.compteurObjets += 1