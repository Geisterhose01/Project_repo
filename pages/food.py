import streamlit as st
import pandas as pd

st.title('Food')

st.subheader('Hier sind einge Vorschläge aus der API')

data = pd.read_json('categories.php.json') #Verwendung der Food API
st.write(data) #Wiedergabe der Food API, müssen noch schöner dargestellt werden!