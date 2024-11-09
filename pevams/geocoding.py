import requests

def get_geocode(address):
    url = "https://nominatim.openstreetmap.org/search"
    headers = {
        'User-Agent': 'PEVAM/1.0 (seu_emailgg@example.com)'
    }
    params = {
        'q': address,
        'format': 'json',
        'addressdetails': 1,
        'limit': 1
    }

    try:
        response = requests.get(url, headers=headers, params=params, timeout=5)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Erro durante a geocodificação: {e}")
        return None, None

    data = response.json()
    
    print(data)

    if data:
        location = data[0]
        lat = float(location['lat'])
        lon = float(location['lon'])
        return lat, lon
    else:
        print("Nenhuma localização encontrada para o endereço fornecido.")
        return None, None