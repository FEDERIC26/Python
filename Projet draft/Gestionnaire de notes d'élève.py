#Projet 7 : Gestionnaire de notes d'élève
#Consignes :

    #Créer une liste vide pour stocker les notes
    #Demander à l'utilisateur d'entrer des notes (entre 0 et 20)
    #L'utilisateur tape "fin" pour arrêter
    #Afficher toutes les notes entrées
    #Afficher la moyenne des notes
    #Afficher la note la plus haute et la note la plus basse

#Aide :
# max(liste)  # Note la plus haute
# min(liste)  # Note la plus basse
# sum(liste)  # Somme de tous les éléments
    
liste = []



while True:
    notes = (input("Entrez les notes des élèves: "))
    if notes == "fin":
        break
    liste.append(float(notes))
    
moyenne = round(sum(liste) / len(liste), 2)
    
print(f"La moyennes des notes est: {moyenne}")
print(f" la notes la plus haute est: {max(liste)}")
print(f" la notes la plus basse est: {min(liste)}")