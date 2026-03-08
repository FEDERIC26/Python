#Projet 8 : Convertisseur de températures
# Consignes :

# Afficher un menu avec 3 choix :

        # 1 → Celsius vers Fahrenheit
        # 2 → Fahrenheit vers Celsius
        # 3 → Celsius vers Kelvin
        # 4 → Fahrenheit vers Kelvin

# Demander à l'utilisateur son choix
# Demander la température à convertir
# Afficher le résultat arrondi à 2 chiffres


choix = int(input(" Entrez la température de votre choix : "))
tap= float(input(" Indiquer la valeur de température que vous voulez convertir: "))

if choix == 1:# calcul Celsius vers Fahrenheit
    tap = float(tap * 9/5 + 32)
    print(f" Le résultat est de {round(tap, 2)} Fahrenheit. ")
    
elif choix == 2:# calcul Fahrenheit vers Celsius
    tap = float((tap - 32) * 5/9)
    print(f" Le résultat est de {round(tap, 2)} Celsius. ")
    
elif choix == 3:# calcul Celsius vers Kelvin
    tap = float(tap + 273.15)
    print(f" Le résultat est de {round(tap, 2)} Kelvin. ")
    
elif choix == 4 :# calcul Fahrenheit vers Kelvin
    tap = float((tap - 32) * 5/9 + 273.15)
    print(f" Le résultat est de {round(tap, 2)} Kelvin. ")
    
    
