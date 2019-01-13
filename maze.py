import json
import random
#from Constantes.py import *
#import Constantes.py

FICHIER_NIVEAU1 = "Level_1_List.json"

POS_DEPART = (0, 0)
POS_ARRIVEE = (15, 15)

class Niveau:
		
    def __init__(self, fichier): # Pas besoin du paramètre "fichier" ? #
        self.fichier = fichier # du coup j'au intégrer le paramètre.
        self.couloirs = {}
        self.personnage = Personnage(self) 
        self.outils = ElementsFixes()
        #self.outils.placer()
		        
    def lire_fichier(self, fichier):
        """Méthode permettant de lire le fichier en créant un set contenant les tuples des coordonnées des espaces vides (les couloirs)"""
        with open(fichier) as f:
            data = json.load(f)
            self.couloirs = set(data)    
    
    def afficher(self, couloirs, outils):
        maze = ""
        for index_col in range(15):
            for index_line in range(15):
                if (index_line, index_col) in self.couloirs:
                    # print (self._outils.emplacement_outils)
                    if (index_line, index_col) in self._outils.emplacement_outils:
                        maze += "O" # affichage de trois outils génériques #
                    elif (index_line, index_col) == self._personnage.obtenir_position():
                        maze += "P" # affichage du personnage #
                    else:
                        maze += " " # affichage d'un couloir vide #
                else:
                    maze += "X" # affichage d'un mur #
            maze += "\n"
        
        print (maze)

    def est_permis(self, position):
        return  position in self._couloirs
    

class ElementsFixes:
    """ Gestion des outils représenté par un set de trois tuples contenant les coordoonées des trois objets. """
    def __init__(self):
        self.emplacement_outils = None
        self.compteurObjets = 0
        
    def placer(self, niveau):
        """ Création d'un set contenant les coordoonées des trois outils à ramasser. """
        couloirs = niveau #.couloirs  ? # Copie pour manipulation.  #
        self.emplacement_outils = set(random.sample(couloirs - {POS_DEPART, POS_ARRIVEE}, 3))
        
    def ramasser(self, pos_actuelle):
        if pos_actuelle in self.emplacement_outils:
            # self.compteurObjets +=
            self.emplacement_outils -= pos_actuelle()
            
            
class Personnage:
    
    def __init__(self, niveau):
        self.posX, self.posY = POS_DEPART  
        self.niveau = niveau      
        
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
        if pos_actuelle == POS_ARRIVEE and mac_gyver.compteurObjets == 3:
            print("Vous avez tué le gardien. Vous êtes libre.")
        elif pos_actuelle == POS_ARRIVEE and mac_gyver.compteurObjets < 3:
            print("Vous êtes mort !")
        continuer = 0
        return (continuer)

    def obtenir_position(self):
        return self.posX, self.posY
    
def main():
    
    niveau1 = Niveau("Level_1_List.json")
    mac_gyver = Personnage(niveau1)
    elements_fixes = ElementsFixes()
    
    niveau1.lire_fichier(FICHIER_NIVEAU1)
    elements_fixes.placer(niveau1.couloirs)
    niveau1.afficher(niveau1.couloirs)
    
    #BOUCLE PRINCIPALE
    continuer = 1 # et pourquoi pas plutot "true" ? #
    while continuer:
        
        deplacement = lower(input("Veuillez entrer une lettre pour déplacer Mac Gyver (d, q, z, s) ou 'p' pour sortir :"))
        
        pos_actuelle = mac_gyver.deplacer(deplacement)       
        elements_fixes.ramasser(pos_actuelle)
        mac_gyver.combat(pos_actuelle)
        
        niveau1.afficher(niveau1.couloirs)

main()
