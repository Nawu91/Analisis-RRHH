import streamlit as st
import streamlit.components.v1 as components


background = '''
    <style>
    body {
        background-image: url("BA.jpg");
        background-size: cover;
        color: red; /* Mensaje de prueba para verificar si el CSS se aplica correctamente */
    }
    </style>
'''

st.markdown(background, unsafe_allow_html=True)


sidebar_container = st.sidebar.container()

with sidebar_container:
    st.image('bavos-footer.png', caption='DGDIM-RRHH', use_column_width=True)


