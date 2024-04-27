 import streamlit as st
import requests
import pandas as pd

st.set_page_config(page_title="Tinder fuer Rezepte", page_icon="🍴")

st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url("https://4kwallpapers.com/images/walls/thumbs_3t/13973.jpg");
        background-attachment: fixed;
        background-size: cover
    }}
    table {{
        color: white;
        font-family: Arial, sans-serif;
        border-collapse: collapse;
        width: 100%;
        background-color: #262730;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

st.title("Tinder fuer Rezepte")

def get_recipes(ingredients, diet):
    # api_key = "<your-api-key"
    url = "https://api.spoonacular.com/recipes/complexSearch"
    params = {
        "apiKey": '7a1ecf36ae484c87bedbbae5c31ee4a5',
        "query": ingredients,
        "diet": diet,
        "number": 10,
        "addRecipeInformation": True
    }
    response = requests.get(url, params=params)
    return response.json()

def main():
    ingredients = st.text_input("Füge mit Komma ',' separiert die Zutaten hinzu. (z. B. chicken, rice, broccoli): ")
    diet = st.selectbox("Präferenzen", ["Keine", "Vegetarisch", "Vegan", "Glutenfrei", "Ketogen"])

    if st.button("Suche Rezepte"):
        if ingredients:
            response = get_recipes(ingredients, diet)
            results = response["results"]
            if len(results) == 0:
                st.write("Keine Rezepte gefunden.")
            else:
                df = pd.DataFrame(results)
                df = df[["title", "readyInMinutes", "servings", "sourceUrl"]]
                df['sourceUrl'] = df['sourceUrl'].apply(lambda x: f'<a href="{x}" target="_blank">{x}</a>')
                st.write(df.to_html(escape=False), unsafe_allow_html=True)
        else:
            st.write("Mindestens eine Zutat hinzufügen")

if __name__ == "__main__":
    main()
