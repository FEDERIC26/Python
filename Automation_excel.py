# Automation_excel.py

import pandas as pd

# 1. Lire le fichier
df = pd.read_excel("ventes.xlsx")
print("=== DONNÉES BRUTES ===")
print(df)

# 2. Calculs automatiques
total = df["Ventes"].sum()
moyenne = df["Ventes"].mean()
meilleur = df.loc[df["Ventes"].idxmax(), "Nom"]

print(f"\n=== RAPPORT ===")
print(f"Total ventes : {total}€")
print(f"Moyenne : {moyenne}€")
print(f"Meilleur vendeur : {meilleur}")

# 3. Ventes par mois
par_mois = df.groupby("Mois")["Ventes"].sum()
print(f"\n=== PAR MOIS ===")
print(par_mois)

# 4. Sauvegarder le rapport
rapport = pd.DataFrame({
    "Métrique": ["Total", "Moyenne", "Meilleur vendeur"],
    "Valeur": [total, moyenne, meilleur]
})
rapport.to_excel("rapport.xlsx", index=False)
print("\nRapport sauvegardé ✓")