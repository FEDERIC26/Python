# Traitement.py

import os
import pandas as pd

dossier = "data"
fichiers = [f for f in os.listdir(dossier) if f.endswith(".xlsx")]

print(f"{len(fichiers)} fichiers trouvés\n")

# Lecture et concaténation
chunks = []
for fichier in fichiers:
    chemin = os.path.join(dossier, fichier)
    df = pd.read_excel(chemin)
    print(f"{fichier} → {len(df)} lignes")
    chunks.append(df)

df_total = pd.concat(chunks, ignore_index=True)
print(f"\nTotal avant nettoyage : {len(df_total)} lignes")

# Nettoyage
df_total.drop_duplicates(inplace=True)
df_total.dropna(subset=["ville"], inplace=True)
df_total["age"] = df_total["age"].astype(int)
df_total["score"] = df_total["score"].round(2)

print(f"Total après nettoyage : {len(df_total)} lignes")

# Export
df_total.to_excel("resultat_final.xlsx", index=False)
print("\nFichier resultat_final.xlsx exporté ✅")
