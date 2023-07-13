import streamlit as st
import pandas as pd
import json

def format_phone_number(phone):
    # Eliminar puntos del número de teléfono y convertirlo a entero
    phone = str(phone).replace(".", "")
    return int(phone)

def excel_to_dict(file_path):
    # Leer el archivo Excel
    df = pd.read_excel(file_path, converters={"Teléfono": format_phone_number})
    
    # Convertir las columnas de fechas a strings
    df["Rol_Desde"] = df["Rol_Desde"].astype(str)
    df["Rol_Hasta"] = df["Rol_Hasta"].astype(str)
    
    # Convertir el DataFrame de pandas a un diccionario
    data_dict = df.to_dict(orient='records')
    
    # Modificar el formato del diccionario
    modified_dict = []
    for row in data_dict:
        modified_row = {}
        for key, value in row.items():
            modified_row[key] = f'"{value}"'
        modified_dict.append(modified_row)
    
    # Convertir cada fila en un string separado por comas y entre llaves
    final_dict = [f"{{{', '.join([f'{k}: {v}' for k, v in d.items()])}}}" for d in modified_dict]
    
    return final_dict

# Configuración de la aplicación Streamlit
st.title("Conversión de Excel a Diccionario")
uploaded_file = st.file_uploader("Selecciona un archivo Excel", type=['xls', 'xlsx'])

# Verificar si se ha cargado un archivo
if uploaded_file is not None:
    # Convertir el archivo Excel a diccionario
    result_dict = excel_to_dict(uploaded_file)
    
    # Mostrar el diccionario resultante
    st.write("Diccionario resultante:")
    for row in result_dict:
        st.write(row)
    
    # Descargar el diccionario como archivo JSON
    json_data = json.dumps(result_dict)
    st.download_button("Descargar JSON", data=json_data, file_name="resultado.json", mime="application/json")
