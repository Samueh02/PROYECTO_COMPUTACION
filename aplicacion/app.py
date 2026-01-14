import sys
import os

# --------------------------------------------------
# Añadir la raíz del proyecto al PYTHONPATH
# --------------------------------------------------
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if ROOT_DIR not in sys.path:
    sys.path.append(ROOT_DIR)

# --------------------------------------------------
# Imports normales
# --------------------------------------------------
import streamlit as st
import pandas as pd

from codigo.prediccion import predecir_enfermedad
from utils import (
    cargar_lista_sintomas,
    cargar_top_sintomas,
    cargar_traducciones,
    formatear_nombre
)

# --------------------------------------------------
# Configuración de la página
# --------------------------------------------------
st.set_page_config(
    page_title="Sistema de Predicción de Enfermedades",
    page_icon="🩺",
    layout="wide"
)

# --------------------------------------------------
# Título
# --------------------------------------------------
st.title("🩺 Sistema de Predicción de Enfermedades")
st.write(
    "Selecciona los síntomas que presenta el paciente y el sistema "
    "estimará la enfermedad más probable."
)

st.divider()

# --------------------------------------------------
# Carga de datos auxiliares
# --------------------------------------------------
sintomas_disponibles = cargar_lista_sintomas()
top_sintomas = cargar_top_sintomas()
traducciones = cargar_traducciones()

# Inglés -> Español
sintomas_es = {
    s: traducciones.get(s, formatear_nombre(s))
    for s in sintomas_disponibles
}

# Español -> Inglés
sintomas_en = {v: k for k, v in sintomas_es.items()}

# --------------------------------------------------
# TOP 15 síntomas más comunes
# --------------------------------------------------
st.subheader("⭐ Síntomas más frecuentes")

st.write("Pulsa para añadir rápidamente síntomas comunes:")

cols = st.columns(5)
sintomas_top_es = [sintomas_es[s] for s in top_sintomas]

if "seleccionados_es" not in st.session_state:
    st.session_state.seleccionados_es = []

for i, sintoma in enumerate(sintomas_top_es):
    with cols[i % 5]:
        if st.button(sintoma):
            if sintoma not in st.session_state.seleccionados_es:
                st.session_state.seleccionados_es.append(sintoma)

st.divider()

# --------------------------------------------------
# Buscador de síntomas
# --------------------------------------------------
st.subheader("🔍 Selección de síntomas")

with st.expander("📘 Ayuda rápida para buscar síntomas"):
    st.markdown("""
    **Respiratorio**
    - tos · congestión · dificultad respirar · dolor pecho

    **General**
    - fiebre · fatiga · mareos · escalofríos

    **Digestivo**
    - náuseas · vómitos · dolor abdominal · diarrea

    **Neurológico / Mental**
    - dolor cabeza · ansiedad · insomnio · depresión

    **Dolor**
    - dolor espalda · dolor cuello · dolor muscular

    💡 *Escribe solo una palabra clave y el sistema filtrará los síntomas disponibles.*
    """)


sintomas_seleccionados_es = st.multiselect(
    "Busca y selecciona los síntomas:",
    options=sorted(sintomas_es.values()),
    default=st.session_state.seleccionados_es,
    placeholder="Escribe para buscar síntomas..."
)

# Guardamos selección
st.session_state.seleccionados_es = sintomas_seleccionados_es

# Convertimos a inglés (modelo)
sintomas_seleccionados = [
    sintomas_en[s] for s in sintomas_seleccionados_es
]

# --------------------------------------------------
# Mostrar síntomas seleccionados
# --------------------------------------------------
if sintomas_seleccionados_es:
    st.success("✅ Síntomas seleccionados:")
    st.write(", ".join(sintomas_seleccionados_es))

st.divider()

# --------------------------------------------------
# Predicción
# --------------------------------------------------
if st.button("🔎 Predecir enfermedad"):
    if not sintomas_seleccionados:
        st.warning("⚠️ Selecciona al menos un síntoma.")
    else:
        with st.spinner("Analizando síntomas..."):
            enfermedad = predecir_enfermedad(sintomas_seleccionados)

        st.success("Predicción completada")

        st.markdown(
            f"""
            ## 📄 Enfermedad estimada:
            **{enfermedad}**
            """
        )

        st.warning(
            "⚠️ Este sistema es un apoyo informativo y **no sustituye** "
            "el diagnóstico médico profesional."
        )
