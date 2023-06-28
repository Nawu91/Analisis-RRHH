import streamlit as st
import os
import pandas as pd
import numpy as np

@st.cache_data

def get_db():
    path =r'acumulado.xlsx'
    return pd.read_excel(path)
df = get_db()

df_edit = st.data_editor(df, num_rows="dynamic")