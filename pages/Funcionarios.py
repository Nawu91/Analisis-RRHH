import streamlit as st

@st.cache_data
def get_data():
    path =r'Funcionarios y UR MDHYH 2021.xlsx'
    return pd.read_excel(path,sheet_name ='Funcionarios MDHYH')
df = get_data()

df_editable = st.data_editor(df,num_rows='dynamic')