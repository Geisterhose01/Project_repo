import streamlit as st
import requests
import pandas as pd

st.set_page_config(page_title="Tinder fuer Rezepte", page_icon="🍴") #Konfiguration der Standardeinstellungen der Seite

st.markdown( #1. Einfügen des Hintergrundbilds, 2. fixieren des Bildes, damit es beim Scrollen nicht weggeht, 3. Das Bild soll den ganzen Bildschirm decken -cover
            #4. die Schriftart in der Tabelle soll Weiss sein, 5. Definieren der Schriftart, 6. 100% Weite der Tabelle, 7. Farbcode für die graue Hintergrundfarbe der Tabelle
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
    unsafe_allow_html=True #Verwendung des HTML-Codes
)

st.title("Tinder fuer Rezepte") #Titel der Seite

def get_recipes(ingredients, diet): #Funktion zur API Anfrage
    # api_key = "<your-api-key"
    url = "https://api.spoonacular.com/recipes/complexSearch"
    params = { #Definierte Parameter, welche in der get-Anfrage berücksichtigt werden
        "apiKey": '7a1ecf36ae484c87bedbbae5c31ee4a5', #API-Schlüssel
        "query": ingredients, #Zutaten für die Rezeptsuche
        "diet": diet, #Diätpräferenz, welche angegeben wurden
        "number": 10, #Anzahl Ergebnisse, welche die API liefert
        "addRecipeInformation": True #API soll zusätzliche Informationen zu den Rezepten hinzufügen
    }
    response = requests.get(url, params=params) #get-Anfrage an die API mit URL & Parameter
    return response.json() #die response soll im json-format erfolgen

def main():
    ingredients = st.text_input("Füge mit Komma ',' separiert die Zutaten hinzu. (z. B. chicken, rice, broccoli): ") #Eingabefeld für die gewünschten Zutaten
    diet = st.selectbox("Präferenzen", ["Keine", "Vegetarisch", "Vegan", "Glutenfrei", "Ketogen"]) #Auswahl der Diätpräferenzen

    if st.button("Suche Rezepte"): #Button für die Rezeptsuche
        if ingredients: #Prüfen, ob eine Zutat hinzugefügt wurde
            response = get_recipes(ingredients, diet) #wenn eine Zutat hinzugefügt wurde, wird die Funktion get_recipes() ausgeführt
            results = response["results"]
            if len(results) == 0: #wenn die Länge von results == 0 ist, wurden keine Rezepte gefunden
                st.write("Keine Rezepte gefunden.")
            else:
                df = pd.DataFrame(results) #wenn Rezepte gefunden werden, sollen sie in einen DataFrame formatiert werden
                df = df[["title", "readyInMinutes", "servings", "sourceUrl"]] #der df besteht aus vier Spalten
                df['sourceUrl'] = df['sourceUrl'].apply(lambda x: f'<a href="{x}" target="_blank">{x}</a>') #durch die apply() Funktion und lambda soll sichergestellt werden, dass die URL der Rezepte funktionieren
                st.write(df.to_html(escape=False), unsafe_allow_html=True) #df wird zu HTML-Code & erlaubt es diesen anzuzeigen
        else: #wenn keine Zutat hinzugefügt wurde, wird der Benutzer aufgefordert dies zu tun
            st.write("Mindestens eine Zutat hinzufügen")

if __name__ == "__main__":
    main()
