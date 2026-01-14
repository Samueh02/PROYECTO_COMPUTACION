# codigo/evaluacion.py

import pandas as pd
import pickle
from sklearn.metrics import accuracy_score, classification_report


def evaluar_modelo(
    ruta_modelo="modelos/mejor_modelo.pkl",
    ruta_encoder="modelos/encoder.pkl",
    ruta_dataset="datos/procesados/enfermedades_sintomas_limpio.csv"
):
    df = pd.read_csv(ruta_dataset)

    X = df.drop(columns=["diseases"])
    y = df["diseases"]

    encoder = pickle.load(open(ruta_encoder, "rb"))
    y_encoded = encoder.transform(y)

    modelo = pickle.load(open(ruta_modelo, "rb"))
    y_pred = modelo.predict(X)

    accuracy = accuracy_score(y_encoded, y_pred)
    report = classification_report(
        y_encoded,
        y_pred,
        target_names=encoder.classes_,
        zero_division=0
    )

    return accuracy, report
