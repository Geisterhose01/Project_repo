import streamlit as st
import pandas as pd
import numpy as np


st.title('Datefinder')
st.header('Finde deine passende Dateideen für den Sommer')
st.subheader('Beginnen wir mit einigen Angaben von dir..')
x = st.text_input('Wie heisst du?')
st.write(f'Hallo {x}'', schön, dass du unsere App nutzt')

alter = st.slider ('Wie alt bist du?', 0, 100, 25)
st.write('Ich bin', alter, 'Jahre alt.')


st.subheader('Welche Kategorie möchtest du nutzen?')

st.link_button('Events', 'https://projectrepo-c4ukv9mberd3dykzagyjdq.streamlit.app/events')
st.link_button('Food', 'https://projectrepo-c4ukv9mberd3dykzagyjdq.streamlit.app/food')