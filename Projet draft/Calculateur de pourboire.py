# Projet 5 : Calculateur de pourboire
# Consignes :

    # Demande le montant total de l'addition (en euros)
    # Demande le pourcentage de pourboire que l'utilisateur veut laisser (10, 15, ou 20%)
    # Calcule le montant du pourboire
    # Calcule le montant total à payer (addition + pourboire)
    # Affiche les résultats arrondis à 2 chiffres après la virgule

# Formule :
    # Pourboire = addition × (pourcentage / 100)
    # Total = addition + pourboire
    
    
addition = float(input(" Entrez le montant total de l'addition: "))

pourcentage = float(input("Entrez le pourcentage de pourboire (10, 15, 20, ou 25): "))

total = float(addition + pourcentage)

print(f"Votre montant totale est : {round(total, 2)}")
