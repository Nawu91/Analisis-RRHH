import streamlit as st
from streamlit_extras.app_logo import add_logo

st.set_page_config(page_title='App RRHH',
                    layout='wide',
                    initial_sidebar_state="auto")
add_logo("bavos-footer.png")
   
st.title('Gerencia Operativa Gestión de Recursos Humanos')
page_bg_img = '''
<style>
body {
background-image: url("BA.jpg");
background-size: cover;
}
</style>
'''
st.markdown(page_bg_img, unsafe_allow_html=False)