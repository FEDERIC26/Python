#  Automatiseur de renommage de fichiers.py
# Bloc 1 : juste demander le chemin et vérifier
from datetime import datetime
from pathlib import Path

chemin = input("chemin du dossier : ")
dossier = Path(chemin)

if not dossier.exists():
    print("Le dossier n'existe pas.")
elif not dossier.is_dir():
    print("Ce n'est pas un dossier")
else:
    print("OK, dossier trouvé !")

    # X fichiers trouvés, les afficher
    fichiers = [f for f in dossier.iterdir() if f.is_file()]
    print(f"{len(fichiers)} fichiers trouvés :")
    for i, fichier in enumerate(fichiers, start=1):
        print(f"{i}. {fichier.name}")

    while True:
        print("Vos choix :")
        print("1. Ajouter un préfixe")
        print("2. Numéroter les fichiers")
        print("3. Remplacer du texte")
        print("4. Quitter")

        option = input("Que voulez-vous faire ? : ")

        if option == "1":
            # Ajouter un préfixe
            prefixe = input("Entrez le préfixe à ajouter aux fichiers : ")
            changements = []
            for fichier in fichiers:
                nouveau_nom = f"{prefixe}_{fichier.name}"
                nouveau_chemin = fichier.parent / nouveau_nom
                changements.append((fichier, nouveau_chemin))
                print(f"Renommé : {fichier.name} -> {nouveau_nom}")

            confirmer = input("Confirmer ? (o/n) : ")
            if confirmer == "o":
                with open(dossier / "log.txt", "a") as f:
                    for ancien, nouveau in changements:
                        ancien.rename(nouveau)
                        maintenant = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        f.write(f"[{maintenant}] {ancien.name} → {nouveau.name}\n")
                print("Renommage terminé !")
            else:
                print("Annulé.")

        elif option == "2":
            # Numéroter les fichiers
            changements = []
            for i, fichier in enumerate(fichiers, start=1):
                numéro = f"{i:03d}"  # Formatage pour avoir des numéros à trois chiffres
                nouveau_numérotation = f"{numéro}_{fichier.name}"
                nouveau_chemin = fichier.parent / nouveau_numérotation
                changements.append((fichier, nouveau_chemin))
                print(f"{fichier.name} → {nouveau_numérotation}")

            # Confirmation
            confirmer = input("Confirmer ? (o/n) : ")
            if confirmer == "o":
                # Boucle 2 : renommage
                with open(dossier / "log.txt", "a") as f:
                    for ancien, nouveau in changements:
                        ancien.rename(nouveau)
                        maintenant = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        f.write(f"[{maintenant}] {ancien.name} → {nouveau.name}\n")
            else:
                print("Annulé.")

        elif option == "3":
            # Remplacer du texte
            # Bloc 4 :  remplacer du texte
            ancien_texte = input("Texte à chercher : ")
            nouveau_texte = input("Année par la quelle voulez-vous la remplacer : ")

            changements = []
            for fichier in fichiers:
                nouveau_nom = fichier.name.replace(ancien_texte, nouveau_texte)
                nouveau_chemin = fichier.parent / nouveau_nom
                changements.append((fichier, nouveau_chemin))
                print(f"Renommé : {fichier.name} → {nouveau_nom}")
            # Confirmation
            confirmer = input("Confirmer ? (o/n) : ")
            if confirmer == "o":
                # Boucle 2 : renommage
                with open(dossier / "log.txt", "a") as f:
                    for ancien, nouveau in changements:
                        ancien.rename(nouveau)
                        maintenant = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        f.write(f"[{maintenant}] {ancien.name} → {nouveau.name}\n")
                print("Renommage terminé !")
            else:
                print("Annulé.")

        elif option == "4":
            # Quitter
            break
        else:
            print("Option invalide !")
