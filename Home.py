import streamlit as st
from streamlit_extras.app_logo import add_logo

st.set_page_config(page_title='App RRHH',
                    layout='wide',
                    initial_sidebar_state="auto")
add_logo("bavos-footer.png")
   
st.title('Gerencia Operativa Gestión de Recursos Humanos')
page_bg_img ="""<style>
body {
background-image: url("BA.jpg");
}
</style>"""

components.html(page_bg_img, width=1100, height=1800, scrolling=True)