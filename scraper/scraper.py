# scraper.py

import requests
import logging
from bs4 import BeautifulSoup

logging.basicConfig(level=logging.INFO, format='%(levelname)s - %(message)s')

def get_html(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        logging.error(f"Error al obtener el HTML: {e}")
        return None

def parse_html(html):
    soup = BeautifulSoup(html, 'html.parser')
    return soup

def search_by_type(soup, type):
    typeSearched = soup.find_all(type)
    return [str(tag).replace("\n", " ").replace("\r", "").strip() for tag in typeSearched] if typeSearched else ["N/A"]

def search_by_id(soup, id):
    idSearched = soup.find(id=id)
    return str(idSearched).replace("\n", " ").replace("\r", "").strip() if idSearched else "N/A"

def search_by_class(soup, class_name):
    classSearched = soup.find_all(class_=class_name)
    return [str(tag).replace("\n", " ").replace("\r", "").strip() for tag in classSearched] if classSearched else ["N/A"]

