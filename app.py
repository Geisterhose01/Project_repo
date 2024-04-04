import streamlit as st
import pandas as pd
import numpy as np


st.title('Datefinder')
st.header('Finde deine passende Dateideen für den Sommer')
st.subheader('Beginnen wir mit einigen Angaben von dir..')
x = st.text_input('Wie heisst du?') #Eingabe Namen
st.write(f'Hallo {x}'', schön, dass du unsere App nutzt.')

alter = st.slider ('Wie alt bist du?', 0, 100, 25) #Altersangabe in einem slider
st.write('Ich bin', alter, 'Jahre alt.')


st.subheader('In welcher Kategorie möchtest du ein Date finden?')

st.link_button('Events', 'https://projectrepo-c4ukv9mberd3dykzagyjdq.streamlit.app/events') #hier haben wir die Seiten mit dem Button verlinkt
st.link_button('Food', 'https://projectrepo-c4ukv9mberd3dykzagyjdq.streamlit.app/food') #hier haben wir die Seiten mit dem Button verlinkt