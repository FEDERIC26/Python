# Projet 13 : Gestionnaire de mots de passe
# Consignes :

# 1-Créer un dictionnaire vide pour stocker les sites et leurs mots de passe.
# 2-Afficher un menu avec 4 choix :

        # 1 → Ajouter un site et son mot de passe
        # 2 → Rechercher le mot de passe d'un site
        # 3 → Supprimer un site
        # 4 → Quitter


# 3-Le menu tourne en boucle.
# 4-Si on recherche ou supprime un site qui n'existe pas, afficher un message d'erreur au lieu de crasher.

web = {}

while True:
    print("1 → Ajouter un site")
    print("2 → Rechercher")
    print("3 → Supprimer")
    print("4 → Quitter")
    choix = input(" Quelle est votre choix? : ")

    if choix == "1":
        sites = input(" Sites: ")
        mdp = input(" Mot de passe: ")
        web[sites] = mdp

    elif choix == "2":
        sites = input(" Nom du sites: ")
        if sites in web:
            print(web[sites])
        else:
            print("Site introuvable !")

    elif choix == "3":
        sites = input(" Site à supprimer ")
        if sites in web:
            del web[sites]
        else:
            print("Site introuvable !")

    elif choix == "4":
        break