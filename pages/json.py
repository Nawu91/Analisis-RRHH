import pandas as pd
import streamlit as st
import json

def excel_to_json(file):
    # Leer el archivo Excel
    df = pd.read_excel(file)

    # Reemplazar los valores NaT con None
    df = df.where(pd.notnull(df), None)

    # Crear una estructura de diccionarios personalizada
    json_data = []
    for index, row in df.iterrows():
        item = {}
        for column in df.columns:
            item[column] = row[column]
        json_data.append(item)

    return json_data

# Configurar la aplicación Streamlit
st.title("Convertir Excel a JSON")
uploaded_file = st.file_uploader("Cargar archivo Excel", type=["xlsx"])

if uploaded_file is not None:
    # Convertir el archivo Excel a JSON
    json_data = excel_to_json(uploaded_file)

    # Mostrar el resultado
    st.write("Resultado en JSON:")
    st.json(json_data)

    # Descargar el archivo JSON resultante
    json_filename = "resultado.json"
    json_string = json.dumps(json_data, ensure_ascii=False)  # Convertir a JSON sin comillas en las claves
    st.download_button("Descargar JSON", json_string, file_name=json_filename)



