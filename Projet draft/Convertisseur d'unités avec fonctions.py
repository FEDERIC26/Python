# Projet 15 : Convertisseur d'unités avec fonctions
# Consignes :

# Créer 6 fonctions de conversion :

    #kg_vers_livres(kg) → retourne kg × 2.205
    #livres_vers_kg(livres) → retourne livres / 2.205
    #km_vers_miles(km) → retourne km × 0.621
    #miles_vers_km(miles) → retourne miles / 0.621
    #celsius_vers_fahrenheit(c) → retourne c × 9/5 + 32
    #fahrenheit_vers_celsius(f) → retourne (f - 32) × 5/9

# Afficher un menu avec ces 6 choix + quitter (7)
# Demander la valeur à convertir
# Appeler la bonne fonction et afficher le résultat arrondi à 2 chiffres


def kg_vers_livres(kg):
    return kg * 2.205
def livres_vers_kg(livres):
    return livres / 2.205
def km_vers_miles(km):
    return km * 0.621
def miles_vers_km(miles):
    return miles / 0.621
def celsius_vers_fahrenheit(c):
    return c * 9/5 + 32
def fahrenheit_vers_celsius(f):
    return (f - 32) * 5/9


print("1 → kg vers livres")
print("2 → livres vers kg")
print("3 → km vers miles")
print("4 → miles vers km")
print("5 → celsius vers fahrenheit")
print("6 → fahrenheit vers celsius")



while True:
    choix = input("Choix: ")
    if choix == "1":
        valeur = float(input("Kg: "))
        resultat = kg_vers_livres(valeur)
        print(f"{round(resultat, 2)} Livres")

    elif choix == "2":
        valeur = float(input("Livres: "))
        resultat = livres_vers_kg(valeur)
        print(f"{round(resultat, 2)} Kg")
            
    elif choix == "3":
        valeur = float(input("Km: "))
        resultat = km_vers_miles(valeur)
        print(f"{round(resultat, 2)} Miles")

    elif choix == "4":
        valeur = float(input("Miles: "))
        resultat = miles_vers_km(valeur)
        print(f"{round(resultat, 2)} Km")

    elif choix == "5":
        valeur = float(input("Celsius: "))
        resultat = celsius_vers_fahrenheit(valeur)
        print(f"{round(resultat, 2)} °F")

    elif choix == "6":
        valeur = float(input("Fahrenheit: "))
        resultat = fahrenheit_vers_celsius(valeur)
        print(f"{round(resultat, 2)} °C")

    elif choix == "7":
        break