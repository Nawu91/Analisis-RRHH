import streamlit as st
from streamlit_extras.app_logo import add_logo
import pandas as pd
import plotly.express as px

st.set_page_config(page_title='Capacitaciones',
                    layout='wide',
                    initial_sidebar_state='collapsed')
add_logo("bavos-footer.png")



@st.cache_data
def get_data():
    path =r'Ley micaela.xlsx'
    return pd.read_excel(path)

def get_data_yolanda():
    path=r'Ley yolanda.xlsx'
    return pd.read_excel(path)

df_yolanda = get_data_yolanda()
colab_yolanda =df_yolanda[df_yolanda['Rol']=='Colaborador']
lid_yolanda = df_yolanda[df_yolanda['Rol']== 'Líder']

df = get_data()
colaborador = df[df['Rol']=='Colaborador']
lider = df[df['Rol']=='Líder']

st.header('Ley Micaela 👩')

col1, col2 = st.columns(2)

color_map = {
    'Aprobó': '#90EE90',  
    'No inscripto': '#20B2AA',
    'Nunca ingresó': '#FFB6C1',
    'Ingresó pero no finalizó': '#87CEFA'
    
}

with col1:

    st.subheader('Progreso total')
    progreso = px.pie(
                    data_frame=df,
                    names='Status Micaela',
                    color_discrete_map=color_map,
                    height=500,
                    width=700,
                    hole=.4)
    st.plotly_chart(progreso,theme="streamlit", use_conatiner_width=False)

with col2:
    st.subheader('Progreso por reparticiones')
    opcion = st.radio(
                    "Selecciona el rol:",
                    ('Colaborador', 'Lider'))

    grafico_col = px.bar(data_frame = colaborador,
                    y='Sigla',
                    color='Status Micaela',
                    
                    barmode= 'relative',
                    height=500,
                    width=700,
                    color_discrete_map=color_map)
    grafico_col.update_traces(textfont_size=15, textangle=0, textposition="inside", cliponaxis=True)

    grafico_lid = px.bar(
                        data_frame= lider,
                        y='Sigla',
                        color='Status Micaela',
                        labels={'variable':'Status','value':'Agentes'},
                        barmode= 'relative',
                        height=500,
                        width=700,
                        color_discrete_map=color_map)
    grafico_lid.update_traces(textfont_size=15, textangle=0, textposition="inside", cliponaxis=True)

    if opcion == 'Colaborador':
        st.plotly_chart(grafico_col, theme="streamlit",use_conatiner_width=False)
    else:
        st.plotly_chart(grafico_lid, theme="streamlit", use_conatiner_width=False)
st.divider() 
st.header('Ley Yolanda ♻️')

col3, col4 = st.columns(2)

with col3:

    st.subheader('Progreso total')
    progreso = px.pie(
                    data_frame=df_yolanda,
                    names='Status Ley Yolanda',
                    color_discrete_map=color_map,
                    height=500,
                    width=700,
                    hole=.4)
    st.plotly_chart(progreso,theme="streamlit", use_conatiner_width=False)

with col4:
    st.subheader('Progreso por reparticiones')
    opcion_yolanda = st.radio(
                    "Selecciona el rol:",
                    ('Colaboradores', 'Lideres'))

    grafico_col = px.bar(data_frame = colab_yolanda,
                    y='Sigla',
                    color='Status Ley Yolanda',
                    labels={'variable':'Status','value':'Agentes'},
                    barmode= 'relative',
                    height=500,
                    width=700,
                    color_discrete_map=color_map)
    grafico_col.update_traces(textfont_size=15, textangle=0, textposition="inside", cliponaxis=True)

    grafico_lid = px.bar(
                        data_frame= lid_yolanda,
                        y='Sigla',
                        color='Status Ley Yolanda',
                        labels={'variable':'Status','value':'Agentes'},
                        barmode= 'relative',
                        height=500,
                        width=700,
                        color_discrete_map=color_map)
    grafico_lid.update_traces(textfont_size=15, textangle=0, textposition="inside", cliponaxis=True)

    if opcion_yolanda == 'Colaboradores':
        st.plotly_chart(grafico_col, theme="streamlit",use_conatiner_width=False)
    else:
        st.plotly_chart(grafico_lid, theme="streamlit", use_conatiner_width=False)
