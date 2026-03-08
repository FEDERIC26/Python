import random
# Projet 4 : Jeu de devinette de nombre

# Consignes :

# Le programme génère un nombre aléatoire entre 1 et 20
# L'utilisateur a 3 essais pour deviner le nombre
# À chaque essai, le programme dit si le nombre est "trop grand", "trop petit" ou "correct"
# Si l'utilisateur trouve, afficher "Bravo !" avec le nombre d'essais utilisés
# Si l'utilisateur échoue après 3 essais, afficher "Perdu ! Le nombre était X"


nombre_secret = random.randint(1, 20)

for essai in range(1, 4):  # De 1 à 3
      
        
    nombre = int(input(" Entrez le nombre secret : "))

    if int(nombre >= nombre_secret):
        print(" Trop grand ")
    elif int(nombre <= nombre_secret):
        print(" Trop petit ")
    elif int(nombre == nombre_secret):
        print(" Correct ")
        print(" Bravo ! ")
else:
    print(f" Perdu!Le nombre était: {nombre_secret}")

