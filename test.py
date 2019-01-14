def lire():
    """Méthode permettant de lire le fichier en créant un set contenant les tuples des coordonnées des espaces vides (les couloirs)"""
    
    couloirs = set()
    depart = set()
    arrivee = set()
    with open("level_1") as f:
        for i, ligne in enumerate(f):
            for j, col in enumerate(ligne):
                if col == '0':
                    couloirs.add((i, j))
                elif col == 'd':
                    depart.add((i,j))
                elif col == 'a':
                    arrivee.add((i, j))
                    
    print (couloirs, depart, arrivee)

lire()
