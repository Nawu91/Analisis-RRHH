import streamlit as st
import streamlit.components.v1 as components
from streamlit_extras.app_logo import add_logo

st.set_page_config(page_title='Raps',
                    layout='wide',
                    initial_sidebar_state="collapsed")
add_logo("bavos-footer.png")

st.title('Raps - Datos de contacto')

with open("Raps.html", "r") as file:
    html_code = file.read()
components.html(html_code, width=1700, height=800, scrolling=True)
