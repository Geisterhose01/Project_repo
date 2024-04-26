import streamlit as st
import pandas as pd
from apiController import searchByIngredients

st.title('Finde dein Traumrezept')
st.subheader('Welche Zutaten willst du verwenden?')

food_ingredients = [
    "Apples", "Bananas", "Carrots", "Dates", "Eggs", 
    "Fish", "Garlic", "Honey", "Ice cream", "Jam",
]

selected_ingredients = st.multiselect(
    label="Select food ingredients",
    options=food_ingredients,
    default=[],
    key=None,  
    help="Choose one or more food ingredients",
    disabled=False,
    label_visibility="visible"
)

def getFoodSuggestions(selected_ingredients): 
    result = searchByIngredients(selected_ingredients, 10)
    if result is None:
        return 'Keine Einträge gefunden'
    else:
        # Extract image URLs from the result
        image_urls = [recipe['image'] for recipe in result]
        return image_urls
        
        
if st.button('Get Suggestions'):
    getFoodSuggestions(selected_ingredients)

    
# Display the selected options
st.write(f"You selected: {', '.join(selected_ingredients)}")
