# Model do predykcji cen mieszkań

## Opis
Projekt oparty na danych z pliku *Houses.csv* oraz modelach trenowanych w notatniku *analizaDanych.ipynb*. Aplikacja Streamlit (*app.py*) wykorzystuje funkcje pomocnicze z *funkcje.py*, w tym pobieranie współrzędnych adresu przez API Nominatim (OpenStreetMap).

## Struktura
- **app.py** – interfejs webowy oparty na Streamlit.  
- **funkcje.py** – funkcje do pobierania współrzędnych i walidacji miasta.  
- **analizaDanych.ipynb** – analiza i przygotowanie danych, tworzenie modelu.  
- **model.pkl**, **model_grid.pkl** – zapisane modele używane do predykcji.  
- **requirements.txt** – lista bibliotek wymaganych do uruchomienia aplikacji.

## Uruchomienie
1. Zainstaluj pakiety wymagane do działania aplikacji: 
``` bash
pip install -r requirements.txt
```
2. Uruchom aplikację:
``` bash 
streamlit run app.py
```


## Uwaga

Wytrenowany model był zbyt duży, by wrzucić go na github. Mozna go wytrenować samemu, albo pobrać zipa z mojego google dysk.

https://drive.google.com/file/d/1-YIkWltkl6WxKq71QkNzTPIFEw2n6CAF/view?usp=drive_link