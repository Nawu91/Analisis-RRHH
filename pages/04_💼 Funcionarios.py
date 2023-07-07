import streamlit as st
import streamlit.components.v1 as components
from streamlit_extras.app_logo import add_logo

st.set_page_config(page_title='Funcionarios',
                    layout='wide',
                    initial_sidebar_state="auto")
add_logo("bavos-footer.png")

st.title('Organigrama MDHYHGC')

with open("org.html", "r") as file:
    html_code = file.read()
components.html(html_code, width=1100, height=2500, scrolling=True)