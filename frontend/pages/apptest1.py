import streamlit as st

st.title('Rezeptideen')
st.header('')
st.write_steam('Hier sind ein paar Dateideen für den Sommer:')
x = st.text_input('schreibe deine Namen')
st.write(f'Dein Name ist: {x}')

st.text_input('wie alt bist du?')

st.text_input('woher kommst du?')
