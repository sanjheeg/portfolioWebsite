import streamlit as sl

# sl.set_page_config(layout="wide")

col1, col2 = sl.columns(2)
#col2 = sl.columns(2)

with col1:
    sl.image("venv/images/me.jpg")


with col2:
    sl.title("Sanjhee Gupta")
    abt_me = "Hello! I am Sajhee, a sophomore studying Computer Science and Data Science at Pudrdue University"
    sl.info(abt_me)