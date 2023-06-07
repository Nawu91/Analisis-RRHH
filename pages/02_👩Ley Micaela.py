import streamlit as st

import pandas as pd
import plotly.express as px

st.set_page_config(page_title='Ley Micaela',
                    layout='wide',
                    initial_sidebar_state='expanded')


@st.cache
def get_data():
    path =r'Ley micaela.xlsx'
    return pd.read_excel(path)

df = get_data()
colaborador = df[df['Rol']=='Colaborador']
lider = df[df['Rol']=='Líder']

st.header('Progreso total')
progreso = px.pie(
                data_frame=df,
                names='Status Micaela',
                color_discrete_sequence=px.colors.qualitative.Set2,
                height=500,
                width=600,
                hole=.4)
st.plotly_chart(progreso,theme="streamlit", use_conatiner_width=True)
