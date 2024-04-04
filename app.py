import streamlit as st
import pandas as pd
import numpy as np


st.title('Dateideen')
st.header('Dateideen für den Sommer')
st.write_steam('Hier sind ein paar Dateideen für den Sommer:')
st.text_input('Wie heisst du?')
x = st.text_input('Wie heisst du?')
st.write(f'Dein Name ist: {x}')

alter = st.slider ('Wie alt bist du?', 0, 100, 25)
st.write('Ich bin', alter, 'Jahre alt')

st.text_input('woher')