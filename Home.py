import streamlit as st

st.set_page_config(
    page_title="Analisis RRHH",
    page_icon='',
    layout="wide",
    initial_sidebar_state="expanded")

sidebar_container = st.sidebar.container()
with sidebar_container:
    st.image('bavos-footer.png', caption='DGDIM-RRHH', use_column_width=True)

st.markdown('<style src="styles.css"></style>', unsafe_allow_html=True)
