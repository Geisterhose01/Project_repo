import streamlit as st
import pandas as pd
import numpy as np


st.title('Datefinder')
st.header('Finde deine passende Dateideen für den Sommer')
st.subheader('Beginnen wir mit einigen Angaben von dir..')
x = st.text_input('Wie heisst du?')

alter = st.slider ('Wie alt bist du?', 0, 100, 25)

st.write(f'Hallo {x}'', schön, dass du unsere App nutzt')

st.subheader('Welche Kategorie möchtest du nutzen?')

data = pd.read_csv('food.csv')
st.write(data)