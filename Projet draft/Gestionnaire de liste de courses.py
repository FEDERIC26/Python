# Projet 6 : Gestionnaire de liste de courses
# Consignes :       

    # Créer une liste vide au départ
    # Demander à l'utilisateur d'ajouter des articles à la liste
    # L'utilisateur tape "fin" pour arrêter d'ajouter
    # Afficher la liste complète des articles
    # Afficher le nombre total d'articles dans la liste
    
liste = []

while True:
    articles = input("Entrez vos articles: ")
    if articles == "fin":
        break
    liste.append(articles)

print(f" Voici votre liste de courses:{liste} ")
print(f" Votre liste de course contient {len(liste)} articles. ")