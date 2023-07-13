import pandas as pd
import streamlit as st
import json

def excel_to_json(file):
    # Leer el archivo Excel
    df = pd.read_excel(file)

    # Convertir los valores Timestamp a cadenas de texto
    df = df.applymap(lambda x: x.strftime('%Y-%m-%d %H:%M:%S') if isinstance(x, pd.Timestamp) else x)

    # Reemplazar los valores NaT con None
    df = df.where(pd.notnull(df), None)

    # Convertir a JSON con claves y valores sin comillas
    json_data = [{str(k): str(v) for k, v in record.items()} for record in df.to_dict(orient='records')]

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
    json_string = json.dumps(json_data, ensure_ascii=True)  # Convertir a JSON sin comillas en las claves y valores
    st.download_button("Descargar JSON", json_string, file_name=json_filename)





