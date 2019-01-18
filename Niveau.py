#!/usr/bin/python3
# -*- coding: Utf-8 -*

class Niveau:
		
    def __init__(self, fichier):
        self.fichier = fichier
        self.couloirs = set()
        self.depart = set()
        self.arrivee = set()
        self.lire_fichier()
        self.personnage = Personnage(self) 
        self.outils = ElementsFixes()
        
		        
    def lire_fichier(self):
        """Méthode permettant de lire le fichier en créant un set contenant les tuples 
        des coordonnées des espaces vides (les couloirs)"""
        with open(self.fichier) as f:

            for i, ligne in enumerate(f):
                for j, col in enumerate(ligne):
                    if col == '0':
                        self.couloirs.add((i, j))
                    elif col == 'd':
                        self.depart.add((i,j))
                        self.couloirs.add((i, j))
                    elif col == 'a':
                        self.arrivee.add((i, j))
                        self.couloirs.add((i, j))

    
    def afficher(self):
        maze = ""
        for index_line in range(15):
            for index_col in range(15):
                if (index_line, index_col) in self.couloirs:
                    if (index_line, index_col) == self.personnage.obtenir_position():
                        maze += "P" # affichage du personnage #
                    elif (index_line, index_col) in self.outils.emplacement_outils:
                        maze += "O" # affichage de trois outils génériques #
                    elif (index_line, index_col) == self.pos_arrivee:
                        maze += "G" # affichage du gardien #
                    else:
                        maze += " " # affichage d'un couloir vide #
                else:
                    maze += "X" # affichage d'un mur #
            maze += "\n"
        
        print(maze)

    def est_permis(self, position):
        return  position in self.couloirs
    
    @property
    def pos_depart(self):
        return list(self.depart)[0]
    
    @property
    def pos_arrivee(self):
        return list(self.arrivee)[0]