import streamlit as st
import pandas as pd
import json

def excel_to_dict(file_path):
    # Leer el archivo Excel
    df = pd.read_excel(file_path)
    
    # Convertir el DataFrame de pandas a un diccionario
    data_dict = df.to_dict(orient='records')
    
    # Modificar el formato del diccionario
    modified_dict = []
    for row in data_dict:
        modified_row = {}
        for key, value in row.items():
            modified_row[key] = str(value)
        modified_dict.append(modified_row)
    
    return modified_dict

# Configuración de la aplicación Streamlit
st.title("Conversión de Excel a Diccionario")
uploaded_file = st.file_uploader("Selecciona un archivo Excel", type=['xls', 'xlsx'])

# Verificar si se ha cargado un archivo
if uploaded_file is not None:
    # Convertir el archivo Excel a diccionario
    result_dict = excel_to_dict(uploaded_file)
    
    # Mostrar el diccionario resultante
    st.write("Diccionario resultante:")
    st.write(result_dict)
    
    # Descargar el diccionario como archivo JSON
    json_data = json.dumps(result_dict)
    st.download_button("Descargar JSON", data=json_data, file_name="resultado.json", mime="application/json")
