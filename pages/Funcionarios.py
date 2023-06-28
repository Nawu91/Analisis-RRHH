import streamlit as st
import pandas as pd

@st.cache_data
def get_data():
    path =r'acumulado.xlsx'
    return pd.read_excel(path)

df = get_data()

