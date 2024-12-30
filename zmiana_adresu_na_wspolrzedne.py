import requests

def get_coordinates(address):
    url = 'https://nominatim.openstreetmap.org/search'
    params = {
        'q': address,
        'format': 'json'
    }
    headers = {
        'User-Agent': 'zmiana_adresu_na_wspolrzedne/1.0 (kontakt@example.com)'
    }
    response = requests.get(url, params=params, headers=headers)
    
    if response.status_code != 200:
        print(f"Error: Received status code {response.status_code}")
        return None
    
    try:
        data = response.json()
    except requests.exceptions.JSONDecodeError:
        print("Error: Response is not valid JSON")
        return None
    
    if data:
        latitude = data[0]['lat']
        longitude = data[0]['lon']
        return latitude, longitude
    else:
        return None

if __name__ == "__main__":
    address = input("Podaj adres: ")
    coordinates = get_coordinates(address)
    
    if coordinates:
        print(f"Współrzędne dla adresu '{address}' to: {coordinates}")
    else:
        print("Nie znaleziono współrzędnych dla podanego adresu.")
        
# Przykładowe użycie
# Podaj adres: Pałac Kultury i Nauki, Warszawa, Polska
# Współrzędne dla adresu 'Pałac Kultury i Nauki, Warszawa, Polska' to: ('52.2319237', '21.0067265')
adres =get_coordinates("Pałac Kultury i Nauki, Warszawa, Polska") # ('52.2319237', '21.0067265')
print(adres) # ('52.2319237', '21.0067265')