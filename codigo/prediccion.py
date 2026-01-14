# codigo/prediccion.py
import pickle
import pandas as pd

def cargar_modelo():
    with open("modelos/mejor_modelo.pkl", "rb") as f:
        return pickle.load(f)

def cargar_encoder():
    with open("modelos/encoder.pkl", "rb") as f:
        return pickle.load(f)

def predecir_enfermedad(sintomas_seleccionados):
    modelo = cargar_modelo()
    encoder = cargar_encoder()

    df = pd.read_csv(
        "datos/procesados/enfermedades_sintomas_limpio.csv",
        nrows=1
    )

    X = pd.DataFrame(
        [[0] * (len(df.columns) - 1)],
        columns=[c for c in df.columns if c != "diseases"]
    )

    for s in sintomas_seleccionados:
        if s in X.columns:
            X.at[0, s] = 1

    pred = modelo.predict(X)[0]
    enfermedad = encoder.inverse_transform([pred])[0]

    return enfermedad
