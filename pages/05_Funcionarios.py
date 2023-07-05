import streamlit as st
from streamlit import components

def main():
    with open("org.html", "r") as file:
        html_code = file.read()
    components.html(html_code, width=800, height=600, scrolling=True)