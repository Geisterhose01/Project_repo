import requests
import streamlit as st
# This file manages access to the endpoints of the API

# Api key for https://spoonacular.com/ the key is needed
apiKey = '7a1ecf36ae484c87bedbbae5c31ee4a5'
spooncularBaseUrl = 'https://api.spoonacular.com/'
authenticationPart = '?apiKey=' + apiKey



def searchByIngredients(ingredients, maxNumberOfResults):

    textForIngridients = '&ingridients='

    # Split Ingridients into a single one and format it correctly for the api request.
    ingredientList = ', '.join( ingredients)

    test = 'https://api.spoonacular.com/recipes/findByIngredients?ingredients=apples,+flour,+sugar&number=2'

    # Building a request to the api
    request = spooncularBaseUrl + 'recipes/findByIngredients' + authenticationPart + textForIngridients + ingredientList + '&number=' + str(maxNumberOfResults)
    response = requests.get(test)
    st.write(request)

    # Checking if the request was successful

    if response.status_code == 200:
        return response.json()
    return print(f"Failed to fetch data: {response.status_code}")

