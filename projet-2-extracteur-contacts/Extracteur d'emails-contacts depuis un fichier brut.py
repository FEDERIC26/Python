# Extracteur d'emails/contacts depuis un fichier brut.py

import csv
import re
from pathlib import Path

chemin = input("Merci de entrer le chemin du fichier : ")
fichier = Path(chemin)

if not fichier.exists():
    print("Le fichier n'existe pas. ")
else:
    with open(fichier, "r") as f:
        contenu = f.read()
    print(contenu)

    emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", contenu)

    telephones = re.findall(r"0[1-9][\s.-]?(?:\d{2}[\s.-]?){4}", contenu)

    emails_uniques = list(set(emails))
    print(emails_uniques)

    telephones_uniques = list(set(telephones))
    telephones_uniques = [t.strip(".\n ") for t in telephones_uniques]
    telephones_uniques = [re.sub(r"[\s.-]", "", t) for t in telephones_uniques]
    print(telephones_uniques)

    with open("contacts.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["type", "valeur"])

        for email in emails_uniques:
            writer.writerow(["email", email])

        for telephone in telephones_uniques:
            writer.writerow(["telephone", telephone])

    print("--- Résumé ---")
    print(f"Emails trouvés : {len(emails)}")
    print(f"Emails uniques : {len(emails_uniques)}")
    print(f"Doublons supprimés : {len(emails) - len(emails_uniques)}")
    print(f"Téléphones trouvés : {len(telephones)}")
    print(f"Téléphones uniques : {len(telephones_uniques)}")
    print("Export : contacts.csv")
