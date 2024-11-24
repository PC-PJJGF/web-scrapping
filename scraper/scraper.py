# scraper.py

import requests
from bs4 import BeautifulSoup

def get_html(url):
    response = requests.get(url)
    return response.text

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

