import pandas as pd

def formatear_nombre(texto):
    return texto.replace("_", " ").capitalize()

def cargar_lista_sintomas(
    ruta_dataset="datos/procesados/enfermedades_sintomas_limpio.csv"
):
    df = pd.read_csv(ruta_dataset)
    return list(df.drop(columns=["diseases"]).columns)

def cargar_top_sintomas(
    ruta_dataset="datos/procesados/enfermedades_sintomas_limpio.csv",
    top_n=15
):
    df = pd.read_csv(ruta_dataset)
    conteo = df.drop(columns=["diseases"]).sum()
    return conteo.sort_values(ascending=False).head(top_n).index.tolist()

def cargar_traducciones():
    return {
        "cough": "Tos",
        "fever": "Fiebre",
        "shortness_of_breath": "Dificultad para respirar",
        "chest_pain": "Dolor en el pecho",
        "depression": "Depresión",
        "insomnia": "Insomnio",
        "palpitations": "Palpitaciones",
        "dizziness": "Mareos",
        "anxiety_and_nervousness": "Ansiedad y nerviosismo",
        "nasal_congestion": "Congestión nasal",
        "sore_throat": "Dolor de garganta",
        "fatigue": "Fatiga",
        "headache": "Dolor de cabeza",
        "nausea": "Náuseas",
        "vomiting": "Vómitos",
    }
