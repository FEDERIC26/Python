# Generer_fichiers.py

import os

import numpy as np
import pandas as pd

os.makedirs("data", exist_ok=True)

for i in range(1, 6):
    df = pd.DataFrame(
        {
            "id_patient": range(1, 10001),
            "nom": [f"Patient_{j}" for j in range(1, 10001)],
            "age": np.random.randint(18, 90, 10000),
            "ville": np.random.choice(["Paris", "Lyon", "Bordeaux", None], 10000),
            "score": np.random.uniform(0, 100, 10000),
        }
    )
    df.to_excel(f"data/fichier_{i}.xlsx", index=False)
    print(f"fichier_{i}.xlsx créé")

print("Tous les fichiers sont prêts.")
