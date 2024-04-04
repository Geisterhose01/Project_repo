import streamlit as st

st.title('Food')

st.subheader('Hier sind einge Vorschläge aus der API')

data = pd.read_csv('food.csv')
st.write(data)