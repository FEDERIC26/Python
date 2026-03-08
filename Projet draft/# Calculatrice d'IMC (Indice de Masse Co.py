# Calculatrice d'IMC (Indice de Masse Corporelle)

#Consignes :

    #Demande le poids (en kg) et la taille (en mètres) de l'utilisateur
    #Calcule l'IMC avec la formule : IMC = poids / (taille * taille)
    #Affiche l'IMC
    #Affiche la catégorie selon ces règles :#


    #IMC < 18.5 → "Insuffisance pondérale"
    #IMC entre 18.5 et 24.9 → "Poids normal"
    #IMC entre 25 et 29.9 → "Surpoids"
    #IMC >= 30 → "Obésité"

    #Note : La taille doit être en mètres (exemple : 1.75 pour 1m75)
    
    
# Calculateur de IMC
poids = float(input(" Enter votre poids en kilogramme: "))    
taille = float(input(" Entrer votre taille em mètres: "))

imc  = float(poids / (taille * taille))

print(f"Votre IMC est : {round(imc, 2)}")

# Conditions 
if imc < 18.5 :
    print(" Vous êtes en insuffisance pondérale ")
elif 18.5 < imc < 24.9 :
    print(" Vous êtes en poids normale ")
elif 25 < imc < 29.9 : 
    print(" Vous êtes en surpoids ")
elif imc >= 30: 
    print(" Vous êtes en obésité ")
    