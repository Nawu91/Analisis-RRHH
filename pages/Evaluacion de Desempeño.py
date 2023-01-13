import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title='ED 2022',
                    layout='wide',
                    initial_sidebar_state="expanded")
st.header("Evaluacion de Desempeño 2022")

@st.cache
def get_data():
    path ='https://github.com/Nawu91/Analisis-RRHH/blob/f1279dc6c9ebf77152e1ab845358b7ac08ae892d/Ed%202022.xlsx'
    return pd.read_excel(path,engine='openpyxl')

df = get_data()

no_evaluable = int(df[(df['estado'] == 'No Evaluable')]['estado'].count())
rechazada = int(df[(df['estado'] == 'Rechazada')]['estado'].count())
validadas = int(df[(df['estado'] == 'Validada')]['estado'].count())

ind1, ind2, ind3 = st.columns(3)
graf1, graf2 = st.columns(2)

ind1.metric(label='No evaluables',
          value=str(no_evaluable))
ind2.metric(label='Rechazadas',
          value=str(rechazada))
ind3.metric(label='Validadas',
          value=str(validadas))

repas_ed = px.bar(df,
               x='institucional',
               color='estado',
               barmode= 'relative',
               color_discrete_sequence=px.colors.qualitative.Set2)

graf1.plotly_chart(repas_ed, theme="streamlit", use_conatiner_width=True)

progreso_ed = px.pie(
                data_frame=df,
                names='desempenio',
                color_discrete_sequence=px.colors.qualitative.Set2,
                hole=.4)
graf2.plotly_chart(progreso_ed,theme="streamlit", use_conatiner_width=True)
