import streamlit as st
import streamlit.components.v1 as components
from streamlit_extras.app_logo import add_logo

st.set_page_config(page_title='PPT',
                    layout='wide',
                    initial_sidebar_state="auto")
add_logo("bavos-footer.png")

st.title('Presentacion RRHH')

with st.expander("-"):
  st.image("PPT GORRHH.jpg",width= 1700)

