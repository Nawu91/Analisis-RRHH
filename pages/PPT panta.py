import streamlit as st
import streamlit.components.v1 as components
from streamlit_extras.app_logo import add_logo

st.set_page_config(page_title='PPT',
                    layout='wide',
                    initial_sidebar_state="auto")
add_logo("bavos-footer.png")

st.title('Presentacion RRHH')

with open("org.html", "r") as file:
    html_code = file.read()


st.image("PPT GORRHH.jpg",width= 1700)

with st.expander("diagrama 1"):
   components.html(html_code, width=1700, height=800, scrolling=True)

with st.expander("diagrama 2"):
   components.html(html_code, width=1700, height=800, scrolling=True)

with st.expander("-"):
  st.image("PPT GORRHH 1.jpg",width= 1700)

with st.expander("-"):
  st.image("PPT GORRHH 2.jpg",width= 1700)

with st.expander("graf 1"):
  st.pyplot()

with st.expander("graf 2"):
  st.pyplot()

with st.expander("-"):
  st.image("PPT GORRHH 3.jpg",width= 1700)