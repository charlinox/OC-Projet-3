import json
import random
from Constantes.py import *

class Niveau:
		
    def __init__(self, fichier):
		self.fichier = fichier
		self.couloirs = {}
		        
    def lecture(self, fichier):
        """Méthode permettant de lire le fichier en créant un set contenant les tuples des coordonnées des espaces vides (les couloirs)"""

        with open(fichier) as f:
            data = json.load(f)
            for entree in data:
                couloirs.append(entree)
    
    
        
    def afficher(self):

class Outils:
    """ Gestion des outils représenté par un set de trois tuples contenant les coordoonées des trois objets. """
    
    def placerObjets(self):
        """ Création d'un set contenant les coordoonées des trois outils à ramasser. """
        emplacementOutils = {} 
        couloirsDispo = couloirs # Copie pour manipulation #
        
        if couloirsDispo.get(posDepart or posArrivee):
            couloirsDispo.pop(posDepart or posArrivee) # Sauf départ et arrivée
            emplacementOutils = random.sample(couloirsDispo, 3)
        
				
		
class Personnage:
    
    def __init__(self):
        self.compteurObjets = 0
        self.posX = posDepart[1]
        self.posY = posDepart[2]
        
    def deplacer(self, deplacement):
        switch (deplacement) {
            case d: self.posX += 1;       
            case g: self.posX -= 1;
            case h: self.posY += 1;
            case b: self.posY -= 1;
        }
        
        
        
    def ramasser(self):
        
deplacement = input("Veuillez entrer une lettre pour déplacer Mac Gyver (D, G, H, B) :")