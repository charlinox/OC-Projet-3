
#!/usr/bin/python3
# -*- coding: Utf-8 -*
import random

class Niveau:
    """ Le labyrinthe est généré à partir d'un fichier level_[x] """
		
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
    

class Personnage:
    """ Le personnage de Mac Gyver est le seul éléments mobile. """

    def __init__(self, niveau):
        self.niveau = niveau
        self.pos_x, self.pos_y = self.niveau.pos_depart

    def deplacer(self, deplacement):
        actions = {
            "d": lambda: (self.pos_x, self.pos_y+1),
            "q": lambda: (self.pos_x, self.pos_y-1),
            "z": lambda: (self.pos_x-1, self.pos_y),
            "s": lambda: (self.pos_x+1, self.pos_y),
        }
        pos_x, pos_y = actions[deplacement]()

        if self.niveau.est_permis((pos_x, pos_y)):
            self.pos_x, self.pos_y = pos_x, pos_y
            return (self.pos_x, self.pos_y)
        else:
            # On ne bouge pas
            return (self.pos_x, self.pos_y)


    def combat(self, pos_actuelle):
        if pos_actuelle == self.niveau.pos_arrivee:
            if self.niveau.outils.compteurObjets == 3:
                print("Vous avez tué le gardien. Vous êtes libre.")
                return False
            if self.niveau.outils.compteurObjets < 3:
                print("Vous êtes mort !")
                return False
            return True

    def obtenir_position(self):
        return self.pos_x, self.pos_y
    
    
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