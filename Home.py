import streamlit as st
import streamlit.components.v1 as components
from streamlit_extras.app_logo import add_logo

add_logo("BA.jpg")

sidebar_container = st.sidebar.container()
with sidebar_container:
    st.image('bavos-footer.png', caption='DGDIM-RRHH', use_column_width=True)
    
st.title('Gerencia Operativa Gestión de Recursos Humanos')
