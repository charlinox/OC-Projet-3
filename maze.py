#!/usr/bin/python3
# -*- coding: Utf-8 -*

import random

class Niveau:
		
    def __init__(self, fichier):
        self.fichier = fichier
        self.couloirs = set()
        self._depart = set()
        self.arrivee = set()
        self.lire_fichier()
        self.personnage = Personnage(self) 
        self.outils = ElementsFixes()
        
		        
    def lire_fichier(self):
        """Méthode permettant de lire le fichier en créant un set contenant les tuples des coordonnées des espaces vides (les couloirs)"""
        with open(self.fichier) as f:

            for i, ligne in enumerate(f):
                for j, col in enumerate(ligne):
                    if col == '0':
                        self.couloirs.add((i, j))
                    elif col == 'd':
                        self._depart.add((i,j))
                    elif col == 'a':
                        self.arrivee.add((i, j))

    
    def afficher(self):
        maze = ""
        for index_line in range(15):
            for index_col in range(15):
                if (index_line, index_col) in self.couloirs:
                    # print (self._outils.emplacement_outils)
                    if (index_line, index_col) == self.personnage.obtenir_position():
                        maze += "P" # affichage du personnage #
                    elif (index_line, index_col) in self.outils.emplacement_outils:
                        maze += "O" # affichage de trois outils génériques #
                    else:
                        maze += " " # affichage d'un couloir vide #
                else:
                    maze += "X" # affichage d'un mur #
            maze += "\n"
        
        print(maze)

    def est_permis(self, position):
        return  position in self._couloirs
    
    @property
    def pos_depart(self):
        print (self._depart)
        return list(self._depart)[0]
    
    @property
    def pos_arrivee(self):
        print (self.arrivee)
        return list(self.arrivee)[0]

class ElementsFixes:
    """ Gestion des outils représenté par un set de trois tuples contenant les coordoonées des trois objets. """
    def __init__(self):
        self.emplacement_outils = None
        self.compteurObjets = 0
        
    def placer(self, niveau):
        """ Création d'un set contenant les coordoonées des trois outils à ramasser. """
        couloirs = niveau #.couloirs  ? # Copie pour manipulation.  #
        self.emplacement_outils = set(
            random.sample(
                niveau.couloirs - {niveau.pos_depart, niveau.pos_arrivee}, 
                3
            )
        )
        
    def ramasser(self, pos_actuelle):
        if pos_actuelle in self.emplacement_outils:
            # self.compteurObjets +=
            self.emplacement_outils -= pos_actuelle()
            
            
class Personnage:
    
    def __init__(self, niveau):
        self.niveau = niveau
        self.posX, self.posY = self.niveau.pos_depart

    def deplacer(self, deplacement):
        actions = {
            "d": lambda: (pos_x + 1, pos_y),
            "q": lambda: (pos_x - 1, pos_y),
            "z": lambda: (pos_x, pos_y - 1),
            "s": lambda: (pos_x, pos_y + 1),
            #"p": lambda: (continuer = 0)
        }
        pos_x, pos_y = actions[deplacement]() # C'est quand même étrange cette construction avec les parenthèses aprés les crochets. Tu pourras m'expliquer ? #
        if self.niveau.est_permis(self.posX, self.posY):
            self.posX, self.posY = pos_x, pos_y
            return (self.posX, self.posY)
        else:
            # On ne bouge pas
            return (None)
        
    
    def combat(self, pos_actuelle):
        if pos_actuelle == self.pos_arrivee and mac_gyver.compteurObjets == 3:
            print("Vous avez tué le gardien. Vous êtes libre.")
        elif pos_actuelle == self.pos_arrivee and mac_gyver.compteurObjets < 3:
            print("Vous êtes mort !")
        continuer = 0
        return (continuer)

    def obtenir_position(self):
        return self.posX, self.posY
    
def main():
    
    niveau1 = Niveau("level_1")
    elements_fixes.placer(niveau1)
    niveau1.afficher()
    
    #BOUCLE PRINCIPALE
    continuer = 1 # et pourquoi pas plutot "true" ? #
    while continuer:
        
        deplacement = input(
            "Veuillez entrer une lettre pour déplacer Mac Gyver (d, q, z, s) "
            "ou 'p' pour sortir : "
        ).lower()
        
        pos_actuelle = mac_gyver.deplacer(deplacement)       
        elements_fixes.ramasser(pos_actuelle)
        mac_gyver.combat(pos_actuelle)
        
        niveau1.afficher()

main()
