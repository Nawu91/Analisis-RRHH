import streamlit as st
from streamlit_themes import st_theme



st.set_page_config(page_title='Dotacion RRHH',
                    layout='wide',
                    initial_sidebar_state='expanded')

selected_theme = st.sidebar.selectbox(
    "Select Theme",
    ("Default", "Darkly", "Lightly", "Cheerful", "Dark", "Material")
)
st_theme(selected_theme)
