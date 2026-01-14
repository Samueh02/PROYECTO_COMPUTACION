# codigo/preprocesamiento.py

import pandas as pd
import json
import os


def cargar_sintomas(ruta_mapeo="datos/procesados/mapeo_caracteristicas.json"):
    """
    Carga la lista de síntomas (columnas) usados por el modelo
    """
    with open(ruta_mapeo, "r", encoding="utf-8") as f:
        sintomas = json.load(f)
    return sintomas


def preparar_entrada_usuario(sintomas_usuario, sintomas_modelo):
    """
    Convierte los síntomas seleccionados por el usuario
    en un DataFrame compatible con el modelo
    """
    data = {s: 0 for s in sintomas_modelo}

    for sintoma in sintomas_usuario:
        if sintoma in data:
            data[sintoma] = 1

    return pd.DataFrame([data])
