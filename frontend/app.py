
import streamlit as st #pip install streamlit
import pandas as pd #pip install pandas
import numpy as np #pip install numpy                                   

# Titel
st.title('Rezeptideen')
st.header('Finde deine passende Rezepte für jeden Anlass')

#Beschreibung
st.subheader('Beginnen wir mit einigen Angaben von dir..')
x = st.text_input('Wie heisst du?') #Eingabe Namen
st.write(f'Hallo {x}'', schön, dass du unsere App nutzt.')

alter = st.slider ('Wie alt bist du?', 0, 100, 25) #Altersangabe in einem slider
st.write('Ich bin', alter, 'Jahre alt.')

#Button um zur richtigen Seite zu kommen
st.subheader('Klicke auf den Button um zu deinem passenden Rezept zu gelangen')

st.link_button('Food', 'https://projectrepo-c4ukv9mberd3dykzagyjdq.streamlit.app/food') #hier haben wir die Seiten mit dem Button verlinkt





                             