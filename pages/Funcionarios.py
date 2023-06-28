import streamlit as st
import os
import pandas as pd
import numpy as np

@st.cache_data
def get_data():
    path =r'acumulado.xlsx'
    return pd.read_excel(path)
df = get_db()
