import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title='Prueba DGPSA',
                    layout='wide',
                    initial_sidebar_state="expanded")


components.iframe("https://app.powerbi.com/view?r=eyJrIjoiYTE5MThiZjctYjIxZC00OWQzLWI3ODAtNzA3OGYwM2EyMmMwIiwidCI6IjIzNzc0NzJlLTgwMDQtNDY0OC04NDU2LWJkOTY4N2FmYTE1MCIsImMiOjR9",width=1200, height=1600)
