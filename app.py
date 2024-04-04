import streamlit as st
import pandas as pd
import numpy as np


st.title('Dateideen')
st.header('Dateideen für den Sommer')
st.subheader('Hier sind ein paar Dateideen für den Sommer:')
x = st.text_input('Wie heisst du?')
st.write(f'Dein Name ist: {x}')

alter = st.slider ('Wie alt bist du?', 0, 100, 25)
st.write('Ich bin', alter, 'Jahre alt')

data = pd.read_json('categories.php.json')
st.write(data)