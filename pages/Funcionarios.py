import streamlit as st
import os
import pandas as pd
import numpy as np

@st.cache_data

def get_db():
    path =r'Funcionarios y UR MDHYH 2021.xlsx'
    return pd.read_excel(path,sheet_name='Funcionarios MDHYH')
df = get_db()

df_edit = st.data_editor(df, num_rows="dynamic")