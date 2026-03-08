# Projet 9 : Calculatrice simple
# Consignes :
 
# Afficher un menu avec 4 choix :

# 1 → Addition
# 2 → Soustraction
# 3 → Multiplication
# 4 → Division


# Demander deux nombres à l'utilisateur.
# Effectuer le calcul selon le choix.
# Afficher le résultat arrondi à 2 chiffres.
# Si l'utilisateur choisit la division par 0, afficher un message d'erreur.

nombre1 = float(input(" Que est le premier nombre du calcul: "))
nombre2 = float(input(" Que est le deuxième nombre du calcul: "))

choix = float(input("Quel est le choix de operation: "))

if choix == 1:
    résultat = float(nombre1 + nombre2)
    print(f"Le résultat est : {round(résultat , 2)}")
    
elif choix == 2:
    résultat = float(nombre1 - nombre2)
    print(f"Le résultat est : {round(résultat , 2)}")
    
elif choix == 3:
    résultat = float(nombre1 * nombre2)
    print(f"Le résultat est : {round(résultat , 2)}")
    
elif choix == 4:
    if nombre2 == 0:
        print("Erreur : division par zéro impossible !")
    else:
        résultat = float(nombre1 / nombre2)
        print(f"Le résultat est : {round(résultat , 2)}")
