import streamlit as st
import pandas as pd
import pickle
import funkcje as f

st.title('Predykcja cen mieszkań')
lasy_losowe_tab, lasy_losowe_grid_tab= st.tabs(
    ["Predykcja cen za pomocą RandomForestRegressor", "Predykcja cen za pomocą XGBRegressor"]
)


# Wczytanie modelu
@st.cache_resource
def load_model():
    with open('model.pkl', 'rb') as file:
        return pickle.load(file)
    
@st.cache_resource
def load_model_grid():
    with open('model_grid.pkl', 'rb') as file_grid:
        return pickle.load(file_grid)


with lasy_losowe_tab:
    model = load_model()

    # Sekcja Prognozowania
    st.header('Wprowadź dane mieszkania')

    # Formularz do wprowadzania danych

    address = st.text_input('Adres', 'Rakowicka 20, Kraków')
    floor = st.number_input('Piętro', min_value=0, step=1, value=1)
    rooms = st.number_input('Liczba pokoi', min_value=1, step=1, value=2)
    sq = st.number_input('Powierzchnia (m²)', min_value=15.0, step=1.0, value=50.0)
    year = st.number_input('Rok budowy', min_value=1800, max_value=2100, step=1, value=2024)

    # Przycisk do obliczenia ceny
    submit_button = st.button(label='Oszacuj cenę za pomocą RandomForestRegressor')

    if submit_button:
        with st.spinner('Przetwarzanie...'):
            latitude, longitude, city = f.get_coordinates(address)
            
            if latitude is not None and longitude is not None and city is not None:
                # Sprawdzenie, czy miasto jest wspierane
                city_supported = f.extract_city_supported(city)
                
                # Przygotowanie danych do predykcji
                input_data = pd.DataFrame({
                    'city': [city_supported],
                    'latitude': [latitude],
                    'longitude': [longitude],
                    'floor': [floor],
                    'rooms': [rooms],
                    'sq': [sq],
                    'year': [year]
                })
                
                try:
                    # Predykcja ceny
                    prediction = model.predict(input_data)
                    prediction_value = prediction[0]
                    st.success(f'Szacowana cena mieszkania {address} wynosi: {prediction_value:,.2f} PLN')
                except Exception as e:
                    st.error(f"Błąd podczas predykcji: {e}")
            else:
                st.error("Nie można przekształcić adresu na współrzędne lub nie znaleziono miasta.")
                
            
with lasy_losowe_grid_tab:
    model_grid = load_model_grid()

    # Sekcja Prognozowania
    st.header('Wprowadź dane mieszkania')

    # Formularz do wprowadzania danych

    address = st.text_input('Adres', 'Rakowicka 20, Kraków', key="address")
    floor = st.number_input('Piętro', min_value=0, step=1, value=1, key="floor")
    rooms = st.number_input('Liczba pokoi', min_value=1, step=1, value=2, key="rooms")
    sq = st.number_input('Powierzchnia (m²)', min_value=15.0, step=1.0, value=50.0, key="sq")
    year = st.number_input('Rok budowy', min_value=1800, max_value=2100, step=1, value=2024, key="year")

    # Przycisk do obliczenia ceny
    submit_button_grid = st.button(label='Oszacuj cenę za pomocą XGBRegressor')

    if submit_button_grid:
        with st.spinner('Przetwarzanie...'):
            latitude, longitude, city = f.get_coordinates(address)
            
            if latitude is not None and longitude is not None and city is not None:
                # Sprawdzenie, czy miasto jest wspierane
                city_supported = f.extract_city_supported(city)
                
                # Przygotowanie danych do predykcji
                input_data = pd.DataFrame({
                    'city': [city_supported],
                    'latitude': [latitude],
                    'longitude': [longitude],
                    'floor': [floor],
                    'rooms': [rooms],
                    'sq': [sq],
                    'year': [year]
                })
                
                try:
                    # Predykcja ceny
                    prediction = model_grid.predict(input_data)
                    prediction_value = prediction[0]
                    st.success(f'Szacowana cena mieszkania {address} wynosi: {prediction_value:,.2f} PLN')
                except Exception as e:
                    st.error(f"Błąd podczas predykcji: {e}")
            else:
                st.error("Nie można przekształcić adresu na współrzędne lub nie znaleziono miasta.")