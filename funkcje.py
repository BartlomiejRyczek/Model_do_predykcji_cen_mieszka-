import requests


def get_coordinates(address):
    """
    Pobiera współrzędne geograficzne (latitude, longitude) oraz miasto na podstawie podanego adresu.
    
    :param address: Adres jako string
    :return: Tuple (latitude, longitude, city) lub (None, None, None) w przypadku błędu
    """
    url = 'https://nominatim.openstreetmap.org/search'
    params = {
        'q': address,
        'format': 'json',
        'addressdetails': 1  # Aby uzyskać szczegółowe informacje o adresie
    }
    headers = {
        'User-Agent': 'app.py/1.0 (kontakt@example.com)'
    }
    try:
        response = requests.get(url, params=params, headers=headers, timeout=10)
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None, None, None
    
    if response.status_code != 200:
        print(f"Error")
        return None, None, None
    
    try:
        data = response.json()
    except requests.exceptions.JSONDecodeError:
        print("Error: Response is not valid JSON")
        return None, None, None
    
    if data:
        latitude = float(data[0]['lat'])
        longitude = float(data[0]['lon'])
        # Wyodrębnienie miasta z odpowiedzi
        address_details = data[0].get('address', {})
        city = address_details.get('city') or address_details.get('town') or address_details.get('village')
        if not city:
            # Jeśli miasto nie jest dostępne, próbujemy inne pola
            city = address_details.get('county') or 'Nieznane'
        return latitude, longitude, city
    else:
        print("Nie znaleziono współrzędnych dla podanego adresu.")
        return None, None, None

def extract_city_supported(city):
    """
    Sprawdza, czy miasto jest wspierane przez model. Jeśli nie, zwraca 'Warszawa' jako domyślne.
    
    :param city: Nazwa miasta jako string
    :return: Nazwa wspieranego miasta
    """
    supported_cities = ['Warszawa', 'Kraków', 'Poznań']
    if city in supported_cities:
        return city
    else:
        print(f"Miasto '{city}' nie jest wspierane. Domyślnie użyto 'Warszawa'.")
        return 'Warszawa'