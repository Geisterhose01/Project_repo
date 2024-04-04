import streamlit as st
import pandas as pd
import numpy as np


st.title('Food')

st.subheader('Hier sind einge Vorschläge aus der API')

data = pd.read_json('categories.php.json')
st.write(data)