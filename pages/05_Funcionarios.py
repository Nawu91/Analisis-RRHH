import streamlit as st
import streamlit.components.v1 as components


def main():
    # Cargar el código HTML
    with open("org.html") as file:
        html_code = file.read()

    # Agregar el componente HTML al Streamlit
    components.html(html_code, width=800, height=600, scrolling=True)