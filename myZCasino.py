# -*-coding:utf-8 -*
import os
import random
import math

cagnote = 1000
print("Vous avez", cagnote, "$ au départ.")

rejouer = "o"
while rejouer == "o": 
    nombre_mise = 1
    while !nombre_mise in range(50):
        nombre_mise = input("Tapez le nombre sur lequel vous voulez miser (entre 0 et 49) : ")
    
    mise = input("Quelle somme allez vous miser ?")
    if mise >= cagnote
        mise = cagnote
        print("Tapie !")
        
    roulette = random.randrange(50)

    if nombre_mise == roulette:
        cagnote += math.ceil(mise * 3)
        print("Vous avez gagner. Recevez trois fois la mise.")S
    elif nombre_mise % 2 == roulette % 2:
        cagnote += math.ceil((mise /2))
        print("Vous avez la bonne couleur. Recevez 50% de la mise")
    else
        cagnote -= mise
        print("Vous avez perdu votre mise.")
    
    
    if cagnote <= 0:
        print("Vous êtes ruiné. Adios")
    else
        rejouer = input("Votre cagnote est de "+ cagnote +". Voulez vous rejouer ? o/n")
    
os.system("pause")

