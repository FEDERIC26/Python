#DEVINE LE NOMBRE

#1. importation du module random
import random

#2. générer un nombre aléatoire
#choisissez un nombre entre 1 et 20
nombre_secret = random.randint(1, 20)

#3. interaction avec l'utilisateur
# indique  si l'utilisateur a deviné
devine = False
# compte le nb d'essais
essais = 0

print("Devinez le nombre entre 1 et 20.")

while not devine:
    essai = int(input("Entrez votre nombre:")) # demande à l'utilisateur de  deviner le nombre secret
    essais += 1 # incrémente la variable essais
    
    if essai == nombre_secret:
        devine = True
        print(f" Bravo ! vous avez trouver le nombre en {essais} coups. ")
    elif essai > nombre_secret:
        print(f"Trop grand ! ")
    elif essai < nombre_secret:
        print(f"Trop petit ! ")
  