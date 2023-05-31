import pandas as pd
import streamlit as st

st.set_page_config(page_title='Filtro',
                    layout='wide',
                    initial_sidebar_state="expanded")

def main():
    st.title("Aplicación de filtros")

    # Cargar archivo
    file = st.file_uploader("Cargar archivo Excel o CSV", type=["xlsx", "csv"])

    if file is not None:
        # Leer archivo
        df = read_data(file)

        st.subheader("Datos originales")
        st.write(format_dataframe(df))

        # Seleccionar columnas para aplicar filtros
        columnas = df.columns.tolist()
        columnas_filtro = st.multiselect("Seleccionar columnas para aplicar filtros", columnas)

        if columnas_filtro:
            # Filtros por contenido de las columnas seleccionadas
            filters = {}

            for columna in columnas_filtro:
                valores_unicos = df[columna].unique()
                filtro = st.multiselect(f"Filtro para columna '{columna}'", valores_unicos)
                filters[columna] = filtro

            # Aplicar filtros
            filtered_df = apply_filters(df, filters)

            st.subheader("Datos filtrados")
            st.write(format_dataframe(filtered_df))

            # Descargar archivo filtrado
            if st.button("Descargar archivo filtrado"):
                download_filtered_data(filtered_df)

def read_data(file):
    if file.name.endswith(".xlsx"):
        # Leer archivo Excel
        df = pd.read_excel(file)
    elif file.name.endswith(".csv"):
        # Leer archivo CSV
        df = pd.read_csv(file)
    else:
        st.error("Formato de archivo no válido. Por favor, carga un archivo Excel o CSV.")
        return None

    return df

def apply_filters(df, filters):
    filtered_df = df.copy()

    for columna, valores_filtro in filters.items():
        if valores_filtro:
            # Aplicar filtro a la columna
            filtered_df = filtered_df[filtered_df[columna].isin(valores_filtro)]

    return filtered_df

def download_filtered_data(df):
    # Convertir columnas numéricas a enteros y normalizar valores nulos
    df = convert_numeric_columns(df)

    # Guardar archivo filtrado en formato Excel
    filename = "archivo_filtrado.xlsx"
    df.to_excel(filename, index=False)

    with open(filename, "rb") as file:
        contents = file.read()
        st.download_button("Descargar archivo filtrado", data=contents, file_name=filename)

def convert_numeric_columns(df):
    numeric_cols = df.select_dtypes(include=[int, float]).columns

    for col in numeric_cols:
        # Normalizar valores nulos
        df[col] = df[col].fillna(0).astype(int)

    return df

def format_dataframe(df):
    # Convertir columnas numéricas a enteros y normalizar valores nulos
    df = convert_numeric_columns(df)

    return df

if __name__ == "__main__":
    main()





