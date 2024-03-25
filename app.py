import streamlit as st

st.write('hello world')
st.text_input('schreibe deine Namen')

#Give me a list with all the files in the folder.streamlit

# Path: streamlit/__init__.py
import os

def list_files():
    return os.listdir()


