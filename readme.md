# Web Scraping Project

Este proyecto de **Web Scraping** permite obtener información de una página web según criterios como **ID**, **tipo** y **clase** de los elementos HTML. Los resultados pueden ser guardados en un archivo CSV para su posterior análisis.

## Funcionalidades

- **Obtener datos de una página web**: Se solicita al usuario una URL y se extrae el HTML.
- **Buscar elementos HTM**L: Permite realizar búsquedas por ID, tipo y clase.
- **Guardar los datos**: Los resultados obtenidos de las búsquedas pueden ser guardados en un archivo CSV.
## Estructura del Proyecto

```bash
    web-scrapping/
    │
    ├── .venv/                  # Entorno virtual
    ├── data/                   # Datos guardados (CSV)
    │   └── scraped_data.csv    # Archivo CSV con los datos extraídos
    ├── logs/                   # Archivos de logs
    ├── scraper/                # Lógica principal de scraping
    │   ├── scraper.py          # Funciones para obtener y analizar el HTML
    │   ├── utils.py            # Funciones de utilidad (interacción con el usuario y guardado de datos)
    │   └── __init__.py         # Archivo de inicialización para el paquete
    ├── tests/                  # Pruebas del proyecto
    │   └── test_scraper.py     # Archivo con pruebas para las funciones de scraping
    ├── .gitattributes          # Configuración de Git
    ├── .gitignore              # Archivos y carpetas a ignorar por Git
    ├── main.py                 # Archivo principal que ejecuta el scraper
    └── requirements.txt        # Dependencias del proyecto
```

## Instalación
1. Clona este repositorio

```bash
    git clone [text](https://github.com/ProyectosCarlosPersonales/web-scrapping.git)
    cd web-scrapping
```
2. Crea y activa el entorno virtual

```bash
    python -m venv .venv
    .\.venv\Scripts\activate # Windows
    source .venv/Scripts/activate # Linux/MacOS
```
3. Instala las dependencias

```bash
    pip install -r requirements.txt
```

## Uso
1. Ejecuta el archivo principal

```bash
    python main.py
```

2. El programa te pedirá que ingreses:
    - La URL de la página web
    - Los criterios de búsqueda (ID, tipo y clase)
    - Si deseas guardar los datos en un archivo CSV

3. El programa te mostrara los resultados y te preguntarás si deseas guardarlos en un archivo CSV.

### Requisitos

Este proyecto requiere las siguientes dependencias:

- BeautifulSoup4: Para analizar el HTML.
- requests: Para realizar solicitudes HTTP.
- selenium: Para navegar por la web (no implementado por ahora).

Estas  dependencias están listadas en el archivo `requirements.txt`.