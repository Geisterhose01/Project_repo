import requests
# This file manages acess to the endpoints of the API 

# APi key for https://spoonacular.com/ the key is needed 
apiKey = '7a1ecf36ae484c87bedbbae5c31ee4a5'
spooncularBaseUrl = 'https://api.spoonacular.com/'
authenticationPart = '?apiKey=' + apiKey



def searchByIngredients(ingredients, maxNumberOfResults):
    ingredientList = ''
    amountOfIngredients = len(ingredients)
    i = 0
    # Split Ingridients into a single one and format it correctly for the api request.
    for ingredient in ingredients:
        if(i < amountOfIngredients):
            ingredientList += ingredient + ",+"
        else:
            # Test if it is the last ingredients since it does not need the ,+
            ingredientList += ingredient
    #         
    response = requests.get(spooncularBaseUrl + 'recipes/findByIngredients?ingredients=' + ingredientList + '&number=' + maxNumberOfResults)

    # Checking if the request was successful
    if response.status_code == 200:
        return response.json()
    else:
        return None
        print(f"Failed to fetch data: {response.status_code}")

