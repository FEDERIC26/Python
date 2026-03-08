# Projet 14 : Calculatrice avec fonctions
# Consignes :

# Créer 4 fonctions : addition(), soustraction(), multiplication(), division()
# Chaque fonction prend 2 paramètres et retourne le résultat
# Afficher un menu comme avant
# Utiliser les fonctions selon le choix de l'utilisateur



def addition(a, b):
    return a + b

def soustraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    return a / b


# Menu
choix = input("Choix: ")
nombre1 = float(input("Premier nombre: "))
nombre2 = float(input("Deuxième nombre: "))

if choix == "1":
    resultat = addition(nombre1, nombre2)
    print(resultat)

if choix == "2":
    resultat = soustraction(nombre1, nombre2)
    print(resultat)
    
if choix == "3":
    resultat = multiplication(nombre1, nombre2)
    print(resultat)
    
if choix == "4":
    resultat = division(nombre1, nombre2)
    print(resultat)