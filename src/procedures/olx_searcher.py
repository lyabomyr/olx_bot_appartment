import requests
from bs4 import BeautifulSoup
import json


def search_olx_apartments(city: str, min_price: int, max_price: int, num_rooms: str) -> list:
    products = []

    base_url = f"https://www.olx.pl/nieruchomosci/mieszkania/wynajem/{city}/"
    query_params = (f"?search%5Bprivate_business%5D=private&search%5Border%5D=created_at:desc"
                    f"&search%5Bfilter_float_price:from%5D={min_price}&search%5Bfilter_float_price:to%5D={max_price}"
                    f"&search%5Bfilter_enum_furniture%5D%5B0%5D=yes&search%5Bfilter_enum_rooms%5D%5B0%5D={num_rooms}")

    url = base_url + query_params
    response = requests.get(url)

    if response.status_code != 200:
        print("Failed to retrieve the page")
        return

    soup = BeautifulSoup(response.text, 'html.parser')
    script_tags = soup.find_all("script", {"data-rh": "true", "type": "application/ld+json"})

    for script in script_tags:
        try:
            json_data = json.loads(script.string)
            if json_data['@type'] == 'Product':
                for item in json_data['offers']['offers']:
                    products.append({
                        'price': f"{item['price']} {item['priceCurrency']}",
                        'url': item['url'],
                        'pictures': (item['image']),
                        'name': item['name']
                    })

        except json.JSONDecodeError:
            continue
    return products
