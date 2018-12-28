import json

class Niveau:
		
    def __init__(self, fichier):
		self.file = LEVEL_FILL # Faut il en faire une property pour l'utiliser dans la fonction suivante ?#
		
    def read_values_from_json(file):
    level = []
    with open(file) as f:
        data = json.load(f)
        for entry in data:
            level.append(entry)
    return values