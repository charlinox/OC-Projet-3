import json
import random
from Constantes.py import *

class Niveau:
		
    def __init__(self, fichier):
		self.fichier = FICHIER
		self.couloirs = {}
		        
    def lire_fichier(self, fichier):
        """Méthode permettant de lire le fichier en créant un set contenant les tuples des coordonnées des espaces vides (les couloirs)"""

        with open(fichier) as f:
            data = json.load(f)
            self.couloirs = set(data)    
    
        
    def afficher(self):

class Outils:
    """ Gestion des outils représenté par un set de trois tuples contenant les coordoonées des trois objets. """
    def __init__(self):
        self.emplacement_outils = None
    
    def placerObjets(self, niveau):
        """ Création d'un set contenant les coordoonées des trois outils à ramasser. """
        couloirs = niveau.couloirs # Copie pour manipulation #
        self.emplacement_outils = set(random.sample(couloirs - {POS_DEPART, POS_ARRIVEE}, 3))
        
				
		
class Personnage:
    
    def __init__(self):
        self.compteurObjets = 0
        self.posX, self.posY = posDepart
        
    def deplacer(self, deplacement):
        actions = {
            "d": lambda: (pos_x + 1, pos_y),
            "g": lambda: (pos_x - 1, pos_y),
            "h": lambda: (pos_x, pos_y - 1),
            "b": lambda: (pos_x, pos_y + 1),
        }
        
        
        
    def ramasser(self):
        
deplacement = input("Veuillez entrer une lettre pour déplacer Mac Gyver (D, G, H, B) :")