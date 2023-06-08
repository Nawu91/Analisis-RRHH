import streamlit as st
import os
import pandas as pd
import numpy as np
import plotly.express as px

st.set_page_config(page_title='Dotacion RRHH',
                    layout='wide',
                    initial_sidebar_state="expanded")
@st.cache
def get_data2():
    path =r'acumulado.xlsx'
    return pd.read_excel(path)

df_anual = get_data2()

st.header('Dotacion anual')

st.line_chart(data=df_anual
)

files = os.listdir('dotaciones/')
sorted_files = sorted(files)
selected_file_index = st.selectbox('Selecciona el periodo', range(len(sorted_files)), format_func=lambda i: sorted_files[i])

@st.cache
def get_data(file_name):
    path = os.path.join('dotaciones', file_name)
    return pd.read_excel(path)

if selected_file_index is not None:
    selected_file = files[selected_file_index]
    df = get_data(selected_file)



st.header('Dotacion mensual')
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

st.header('Reparticiones')


areas = px.bar(data_frame= df,
                x='Reparticion General',
                color='Modalidad',
                barmode= 'relative',
                color_discrete_sequence=px.colors.qualitative.Set2,
                width=1450,
                height=500)
st.plotly_chart(areas,theme="streamlit", use_conatiner_width=True)

