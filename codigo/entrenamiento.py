# codigo/entrenamiento.py

import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
import os

def entrenar_modelos(
    ruta_dataset="datos/procesados/enfermedades_sintomas_limpio.csv",
    ruta_modelos="modelos"
):
    os.makedirs(ruta_modelos, exist_ok=True)

    print("📥 Cargando dataset...")
    df = pd.read_csv(ruta_dataset)

    X = df.drop(columns=["diseases"])
    y = df["diseases"]

    print("🔤 Codificando etiquetas...")
    encoder = LabelEncoder()
    y_encoded = encoder.fit_transform(y)

    print("✂️ Dividiendo train / test...")
    X_train, _, y_train, _ = train_test_split(
        X, y_encoded, test_size=0.2, random_state=42
    )

    print("🤖 Entrenando Regresión Logística (optimizada)...")
    modelo = LogisticRegression(
        max_iter=200,
        solver="lbfgs",
        n_jobs=1
    )
    modelo.fit(X_train, y_train)

    print("💾 Guardando modelo y encoder...")
    with open(f"{ruta_modelos}/mejor_modelo.pkl", "wb") as f:
        pickle.dump(modelo, f)

    with open(f"{ruta_modelos}/encoder.pkl", "wb") as f:
        pickle.dump(encoder, f)

    print("✅ Entrenamiento finalizado correctamente")

if __name__ == "__main__":
    entrenar_modelos()
