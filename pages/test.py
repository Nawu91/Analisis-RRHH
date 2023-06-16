import streamlit as st
import os
import pandas as pd
import numpy as np
import plotly.express as px

st.set_page_config(page_title='Dotacion RRHH',
                    layout='wide',
                    initial_sidebar_state="auto")
@st.cache_data
def get_data2():
    path =r'acumulado.xlsx'
    return pd.read_excel(path)
df_anual = get_data2()

selected_periodo = st.selectbox('Selecciona el periodo', lista_periodo)
lista_periodo = periodos.unique().tolist()
periodos = df_anual['Periodo']

df_filtrado = df_anual[df_anual['Periodo'] == selected_periodo]


st.header('Anual 2023')

lineas = px.bar(df_anual, 
                x="Periodo", 
                y="Count", 
                color='Modalidad',
                barmode='group',
                width=1450,
                height=400,
                color_discrete_sequence=px.colors.qualitative.Set2,
                text_auto=True)
st.plotly_chart(lineas,theme="streamlit", use_conatiner_width=True)







st.header('Dotacion del periodo seleccionado')
ausup = df[(df["Modalidad"] == "Autoridades Superiores")]["Modalidad"].count()
cg = df[(df["Modalidad"] == "Carrera Gerencial")]["Modalidad"].count()
gab = df[(df["Modalidad"] == "Gabinete")]["Modalidad"].count()
pp = df[(df["Modalidad"] == "Planta Permanente")]["Modalidad"].count()
pt = df[(df["Modalidad"] == "Plantas Transitorias")]["Modalidad"].count()
conls = df[(df["Modalidad"] == "CLS")]["Modalidad"].count()
at = df[(df["Modalidad"] == "AT")]["Modalidad"].count()

ausup_ta = df[(df["Modalidad"] == "Autoridades Superiores")]["Total Asig"].sum()
cg_ta = df[(df["Modalidad"] == "Carrera Gerencial")]["Total Asig"].sum()
gab_ta = df[(df["Modalidad"] == "Gabinete")]["Total Asig"].sum()
pp_ta = df[(df["Modalidad"] == "Planta Permanente")]["Total Asig"].sum()
pt_ta = df[(df["Modalidad"] == "Plantas Transitorias")]["Total Asig"].sum()
conls_ta = df[(df["Modalidad"] == "CLS")]["Total Asig"].sum()
at_ta = df[(df["Modalidad"] == "AT")]["Total Asig"].sum()

ind1, ind2, ind3 = st.columns(3)
ind4, ind5, ind6, ind7 = st.columns(4)


ind1.metric(label='Autoridades Superiores',
                value=int(ausup),
                delta='$' + format(ausup_ta,'0,.2f'),
                delta_color="normal",)
ind2.metric(label='Carreras Gerenciales',
                value=int(cg),
                delta='$' + format(cg_ta,'0,.2f'),
                delta_color="normal",)
ind3.metric(label='Gabinetes',
                value=int(gab),
                delta='$' + format(gab_ta,'0,.2f'),
                delta_color="normal",)
ind4.metric(label='Plantas Permanentes',
                value=int(pp),
                delta='$' + format(pp_ta,'0,.2f'),
                delta_color="normal",)
ind5.metric(label='Plantas Transitorias',
                value=int(pt),
                delta='$' + format(pt_ta,'0,.2f'),
                delta_color="normal",)
ind6.metric(label='CLS',
                value=int(conls),
                delta='$' + format(conls_ta,'0,.2f'),
                delta_color="normal",)
ind7.metric(label='AT',
                value=int(at),
                delta='$' + format(at_ta,'0,.2f'),
                delta_color='normal',)

st.header('Dotacion por reparticiones')


areas = px.bar(data_frame= df_graf,
                x='Reparticion General',
                y='Contador',
                color="Modalidad",
                barmode='relative',
                color_discrete_sequence=px.colors.qualitative.Set2,
                width=1450,
                height=700,
                text_auto=True)
areas.update_traces(textposition='outside')
sorted_df = df_graf.sort_values('Contador', ascending=False)
x_sorted = sorted_df['Reparticion General']
areas.update_layout(
    xaxis={'categoryorder': 'array', 'categoryarray': x_sorted})

st.plotly_chart(areas,theme="streamlit", use_conatiner_width=True)
