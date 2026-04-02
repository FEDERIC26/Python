# Bot de monitoring de prix.py

import csv
import smtplib
import time
from datetime import datetime
from email.mime.text import MIMEText

from bs4 import BeautifulSoup

# Envoyer un email d'alerte


def envoyer_alerte(prix, seuil):
    expediteur = "ballyfederic@gmail.com"
    destinataire = "ballyfederic@gmail.com"
    mot_de_passe = "skhlrglrubwkaocc"

    message = MIMEText(f"Le prix est tombé à {prix}€, sous votre seuil de {seuil}€ !")
    message["Subject"] = "ALERTE PRIX"
    message["From"] = expediteur
    message["To"] = destinataire
    try:

        with smtplib.SMTP("smtp.gmail.com", 587) as serveur:
            serveur.starttls()
            serveur.login(expediteur, mot_de_passe)
            serveur.sendmail(expediteur, destinataire, message.as_string())
        print("Email d'alerte envoyé !")

    except Exception as e:
        print(f"Erreur envoi email : {e}")


seuil = float(input("Seuil d'alerte (€) : "))

# Scraper un prix
while True:
    with open("boutique.html", "r", encoding="utf-8") as f:
        html = f.read()

    soup = BeautifulSoup(html, "html.parser")

    prix_list = soup.find_all("span", class_="price")
    noms = soup.find_all("h2")
    print(prix_list)

    for nom, prix in zip(noms, prix_list):
        print(f"{nom.text} → {prix.text}")

    for nom, prix in zip(noms, prix_list):
        prix_nombre = float(prix.text.replace("€", ""))
        print(f"{nom.text} → {prix_nombre}€")
        if prix_nombre < seuil:
            print(f"  ALERTE : {nom.text} est sous le seuil !")
            envoyer_alerte(prix_nombre, seuil)

    # Stocker l'historique des prix dans un CSV
    maintenant = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("historique_prix.csv", "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([maintenant, nom.text, prix_nombre])

    #  Comparer avec un seuil

    if prix_nombre < seuil:
        print(f"ALERTE : Le prix ({prix_nombre}€) est sous le seuil de {seuil} € ! ")
        envoyer_alerte(prix_nombre, seuil)
    else:
        print(f"Le prix ({prix_nombre}€) est au-dessus du seuil de {seuil}€. ")

    # Afficher l'historique des prix
    with open("historique_prix.csv", "r") as f:
        reader = csv.reader(f)
        for ligne in reader:
            print(f"{ligne[0]} → {ligne[1]} : {ligne[2]}€")

print("Prochaine vérification dans 60 secondes...")
time.sleep(60)
