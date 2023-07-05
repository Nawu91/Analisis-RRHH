import streamlit as st
import streamlit.components.v1 as components

with open("org.html", "r") as file:
    html_code = file.read()
components.html(html_code, width=1200, height=600, scrolling=True)