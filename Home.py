import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Analisis RRHH",
    page_icon='',
    layout="wide",
    initial_sidebar_state="expanded")

background = '''
    <style>
    body {
        background-image: url("BA.jpg");
        background-size: cover;
    }
    </style>
'''

st.markdown(background, unsafe_allow_html=True)


sidebar_container = st.sidebar.container()

with sidebar_container:
    st.image('bavos-footer.png', caption='DGDIM-RRHH', use_column_width=True)


