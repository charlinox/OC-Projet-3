import json
import random
from Constantes.py import *

class Niveau:
		
    def __init__(self, fichier):
		self.fichier = FICHIER_NIVEAU1
		self.couloirs = {}
		        
    def lire_fichier(self, fichier):
        """Méthode permettant de lire le fichier en créant un set contenant les tuples des coordonnées des espaces vides (les couloirs)"""

        with open(fichier) as f:
            data = json.load(f)
            self.couloirs = set(data)    
    
    def afficher(self, couloirs):
        maze = ""
        for index_col in range(15):
            for index_line in range(15):
                if index_line, index_col in couloirs:
                    if index_line, index_col in Outils.emplacement_outils:
                        maze += "O" # affichage de trois outils génériques #
                    elif index_line, index_col in set(self.posX, self.posY):
                        maze += "P" # affichage du personnage #
                    else:
                        maze += " " # affichage d'un couloir vide #
                else:
                    maze += "X" # affichage d'un mur #
            ligne_maze += "/n"
        
        print (ligne_maze)
            
            

class ElementsFixes:
    """ Gestion des outils représenté par un set de trois tuples contenant les coordoonées des trois objets. """
    def __init__(self):
        self.emplacement_outils = None
        # "self.posX_garde, self.posY_garde = POS_ARRIVEE" sans interet finalement # 
        
    def placer(self, niveau):
        """ Création d'un set contenant les coordoonées des trois outils à ramasser. """
        couloirs = niveau #.couloirs  ? # Copie pour manipulation.  #
        self.emplacement_outils = set(random.sample(couloirs - {POS_DEPART, POS_ARRIVEE}, 3))
        
class Personnage:
    
    def __init__(self):
        self.compteurObjets = 0
        self.posX, self.posY = POS_DEPART        
        
    def deplacer(self, deplacement):
        actions = {
            "d": lambda: (pos_x + 1, pos_y),
            "q": lambda: (pos_x - 1, pos_y),
            "z": lambda: (pos_x, pos_y - 1),
            "s": lambda: (pos_x, pos_y + 1),
            "p": lambda: (continuer = 0) # pas de virgule ici non ? #
        }
        pos_x, pos_y = actions[deplacement]() # C'est quand même étrange cette construction avec les parenthèses aprés les crochets. Tu pourras m'expliquer ? #
        return (pos_x , pos_y) # On fait bien comme ca ? #
    
    def ramasser(self):
        
        
def main():
    
    mac_gyver = Personnage()
    niveau1 = Niveau()
    elements_fixes = ElementsFixes()
    
    niveau1.lire_fichier(FICHIER_NIVEAU1)
    elements_fixes.placer(niveau1.couloirs)
    niveau1.afficher(niveau1.couloirs)
    
    #BOUCLE PRINCIPALE
    continuer = 1 # et pourquoi pas plutot "true" ? #
    while continuer:
        deplacement = lower(input("Veuillez entrer une lettre pour déplacer Mac Gyver (d, q, z, s) ou 'p' pour sortir :"))
        
        pos_actuelle = mac_gyver.deplacer(deplacement)
        
        if pos_actuelle in elements_fixes.emplacement_outils:
            mac_gyver.compteurObjets +=
            # comment on enlève un élément d'un set ? En créant une liste pour le supprimer puis en le retransformant la liste en set à nouveau ? #
        if pos_actuelle == POS_ARRIVEE and mac_gyver.compteurObjets == 3:
            continuer = 0
        elif pos_actuelle == POS_ARRIVEE and mac_gyver.compteurObjets < 3:
            print("Vous êtes mort !")
        
        
            
        
        
        
        