import streamlit as st
import pandas as pd

@st.cache_data
def get_data():
    path =r'Funcionarios y UR MDHYH 2021.xlsx'
    return pd.read_excel(path)

df = get_data()

