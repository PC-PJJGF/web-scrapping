# utils.py
import csv
import os
import logging

logging.basicConfig(level=logging.INFO, format='%(levelname)s - %(message)s')

def ask_for_id():
    if input("Do you want to search by ID? (y/n) ").lower() == 'y':
        id = input("Enter the ID: ")
    else:
        id = "No se ha buscado por ID"
    return id

def ask_for_url():
    while True:
        url = input("Enter the URL: ")
        if url.startswith("http://") or url.startswith("https://"):
            return url
        logging.error("Invalid URL. Please enter a valid URL.")

def ask_for_type():
    if input("Do you want to search by type? (y/n) ").lower() == 'y':
        type = input("Enter the type: ")
    else:
        type = "No se ha buscado por type"
    return type

def ask_for_class():
    if input("Do you want to search by class? (y/n) ").lower() == 'y':
        class_name = input("Enter the class name: ")
    else:
        class_name = "No se ha buscado por class"
    return class_name

def ask_for_save():
    if input("Do you want to save the data? (y/n) ").lower() == 'y':
        return True
    return False

def save_in_csv(data):
    try:
        file_path = 'data/scraped_data.csv'
        
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        
        file_exists = os.path.isfile(file_path)
        
        with open(file_path, 'a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file, quotechar='"', quoting=csv.QUOTE_MINIMAL)
            
            if not file_exists:
                writer.writerow(data.keys())
            
            row = []
            for key, value in data.items():
                if isinstance(value, list):
                    value = ";".join(value)
                row.append(value)
                
            writer.writerow(row)
    except Exception as e:
        raise e

