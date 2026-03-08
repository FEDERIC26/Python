# Projet 12 : Carnet de notes scolaires
# Consignes :

# 1.Créer un dictionnaire vide pour stocker les élèves et leurs notes
# 2.Afficher un menu avec 5 choix :

    # 1 → Ajouter un élève et sa note
    # 2 → Afficher tous les élèves et leurs notes
    # 3 → Afficher la moyenne de la classe
    # 4 → Afficher le meilleur élève
    # 5 → Quitter

# 2.Le menu tourne en boucle

    
Carnet = {}

while True: 
    choix = input(" Quelle est votre choix? : ")
    
    if choix == "1" : 
        # Ajouter
        élève = input(" Nom de l'élève :")
        note  = float(input(" Note : "))
        Carnet[élève] = note
        
    elif choix == "2" :
        # Afficher tout
        for élève, note in Carnet.items():
            print(f" {élève} : {note} ")
                  
    elif choix == "3" :
        # Afficher tout
        moyenne = sum((Carnet).values()) / len(Carnet)
        print(f" Moyenne : {round(moyenne, 2)} ")
    
    elif choix == "4" : 
        meilleur = max(Carnet, key=Carnet.get)
        print(f"Meilleur élève : {meilleur} avec {Carnet[meilleur]}")
    
    elif choix == "5" :
        #Quitter  
        break