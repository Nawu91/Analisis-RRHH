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

progreso, grafico_col, grafico_lid = st.columns(3)

st.header('Progreso total')
progreso = px.pie(
                data_frame=df,
                names='Status Micaela',
                color_discrete_sequence=px.colors.qualitative.Set2,
                height=500,
                width=1200,
                hole=.4)
st.plotly_chart(progreso,theme="streamlit", use_conatiner_width='centered')

st.header('Progreso por reparticiones')

opcion = st.radio(
                "Selecciona el rol:",
                ('Colaborador', 'Lider'))

grafico_col = px.bar(data_frame = colaborador,
                x='Sigla',
                color='Status Micaela',
                labels={'variable':'Status','value':'Agentes'},
                barmode= 'relative',
                color_discrete_sequence=px.colors.qualitative.Set2)
grafico_col.update_traces(textfont_size=15, textangle=0, textposition="inside", cliponaxis=True)

grafico_lid = px.bar(
                    data_frame= lider,
                    x='Sigla',
                    color='Status Micaela',
                    labels={'variable':'Status','value':'Agentes'},
                    barmode= 'relative',
                    color_discrete_sequence=px.colors.qualitative.Set2)
grafico_lid.update_traces(textfont_size=15, textangle=0, textposition="inside", cliponaxis=True)

if opcion == 'Colaborador':
    st.plotly_chart(grafico_col, theme="streamlit",use_conatiner_width='centered')
else:
    st.plotly_chart(grafico_lid, theme="streamlit", use_conatiner_width='centered')
