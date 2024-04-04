import streamlit as st
import pandas as pd
import numpy as np


st.title('Datefinder')
st.header('Finde deine passende Dateideen für den Sommer')
st.subheader('Beginnen wir mit einigen Angaben von dir..')
x = st.text_input('Wie heisst du?')
st.write(f'Dein Name ist: {x}')

alter = st.slider ('Wie alt bist du?', 0, 100, 25)
st.write('Ich bin', alter, 'Jahre alt')

st.subheader('Welche Kategorie möchtest du nutzen?')

data = pd.read_csv('food.csv')
st.write(data)