def lire(fichier):
        """Méthode permettant de lire le fichier en créant un set contenant les tuples des coordonnées des espaces vides (les couloirs)"""
    with open(level_1) as f:
        
        couloir = {}
        for i, ligne in enumerate(f):
            for j, col in enumerate(ligne):
                if col == 0:
                    couloir.add((i,j))

        self.couloirs =(couloir)

self.couloirs = {}
self.depart = {}
self.arrivee = {}

for i, ligne in enumerate(f):
    for j, col in enumerate(ligne):
        if col == '0':
            self.couloirs.add((i, j))
        elif col == 'd':
            self.depart.add((i,j))
        elif col == 'a':
            self.arrivee.add((i, j))

