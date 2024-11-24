# scraper/scraper.py

import requests
from bs4 import BeautifulSoup
from config import BASE_URL, HEADERS

def fetch_page(url):
    try:
        # Realizar la solicitud GET con los headers
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()  # Levanta un error si la respuesta es un código de error HTTP

        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error al realizar la solicitud: {e}")
        return None

def parse_html(html):
    soup = BeautifulSoup(html, 'html.parser')
    return soup

def extract_data(soup):
    # Supongamos que estamos extrayendo los títulos de artículos (ajustar según el sitio)
    titles = soup.find_all('h2')  # Aquí asumiendo que los títulos están en etiquetas <h2>
    
    data = []
    for title in titles:
        data.append(title.text.strip())
    
    return data

def main():
    # URL que quieres scrapear
    url = BASE_URL
    
    # Paso 1: Obtener la página HTML
    html = fetch_page(url)
    if html is None:
        print("No se pudo obtener la página.")
        return
    
    # Paso 2: Analizar el HTML
    soup = parse_html(html)
    
    # Paso 3: Extraer los datos
    data = extract_data(soup)
    
    # Paso 4: Mostrar o guardar los datos extraídos
    for item in data:
        print(item)

if __name__ == "__main__":
    main()
