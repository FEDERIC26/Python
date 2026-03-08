# Projet 11 : Gestion d'un magasin
# Consignes :

#1 Créer un dictionnaire avec 5 produits et leurs prix
#2 Afficher un menu avec 4 choix :

    # 1 → Afficher tous les produits et leurs prix
    # 2 → Rechercher le prix d'un produit
    # 3 → Ajouter un nouveau produit
    # 4 → Quitter

#3 Le menu tourne en boucle


magasin = {
    "pomme" : 1.50,
    "pain"  : 2.00,
    "lait"  : 0.99,
    "poire" : 1.99,
    "poulet": 2.50,
    "viande": 5.50,
    "vins"  : 10.50,
}

while True:
    choix = input(" Quel est votre choix: ")
    
    if choix == "1":
        # Afficher
        for articles, prix in magasin.items():
            print(f" {articles} : {prix} ")
        
    elif choix == "2":
        # Rechercher
        arcticles = input(" Nom de l'article: ")
        print(magasin[articles]) 

    elif choix == "3":
        # Ajouter un new produit
        articles = input(" Articles: ")
        prix = input(" Prix: ")
        magasin[articles] = prix

    elif choix == "4":
        # Quitter
        break
    