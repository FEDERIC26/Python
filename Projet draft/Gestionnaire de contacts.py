# Projet 10 : Gestionnaire de contacts

# Consignes :
# Créer un dictionnaire vide pour stocker les contacts
# Afficher un menu avec 4 choix :

# 1 → Ajouter un contact (nom + numéro)
# 2 → Rechercher un contact par nom
# 3 - Suppirmer le contact 
# 4 → Afficher tous les contacts
# 5 → Quitter

# Le menu tourne en boucle jusqu'à ce que l'utilisateur choisisse 4



contacts = {}

while True:
    choix = input(" Entrez votre choix: ")
    
    if choix == "1":
        # Ajouter un contact
        nom = input(" Nom: ")
        numéro = input(" Numéro: ")
        contacts[nom] = numéro    
        
    elif choix == "2":
        # Rechercher
        nom = input(" Nom à chercher: ")
        print(contacts[nom])   
        
    elif choix == "3":
        # Supprimer
        nom = input(" Nom à supprimer: ")
        del contacts[nom]  
        
    elif choix == "4":
        # Afficher tout
        for nom, numero in contacts.items():
            print(f"{nom} : {numero}")         
        
    elif choix == "5":
        # Quitter
        break  