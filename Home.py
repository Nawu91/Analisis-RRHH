import streamlit as st

st.set_page_config(
    page_title="Ex-stream-ly Cool App",
    page_icon=st.image(<a href="https://imgbb.com/"><img src="https://i.ibb.co/qpYvvHt/bavos-footer.png" alt="bavos-footer" border="0"></a>),
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)
