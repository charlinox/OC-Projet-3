
# -*- coding: Utf-8 -*

"""
Jeu Mac Gyver Labyrinthe
Jeu dans lequel on doit déplacer Mac Gyver afin de ramasser 3 objets (une aiguille, un petit tube en plastique et de l'éther) dispersé à travers un labyrinthe avant de gagner en affrontant le gardien.

Script Python
Fichiers : à compléter
"""


class Niveau:
		
    def __init__(self, fichier):
		self.file = LEVEL_FILL # LEVEL_FILL est une constante définie dans constantes.py #
        #Faut il en faire une property pour l'utiliser dans la fonction suivante ?#


    def generer(self):
		
		with open(self.fichier, "r") as fichier:
			level = []
			
			for line in fichier:
				line_level = []				
				for sprite in line:					
					if sprite != '\n':						
						line_level.append(sprite)
				level.append(line_level)
			self.structure = level