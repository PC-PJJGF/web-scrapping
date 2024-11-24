# main.py
from scraper.scraper import *
from scraper.utils import *
import logging

logging.basicConfig(level=logging.INFO, format='%(levelname)s - %(message)s')

error_handler = logging.FileHandler('logs/error.log')
error_handler.setLevel(logging.ERROR)

error_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s - File "%(filename)s", line %(lineno)d')
error_handler.setFormatter(error_formatter)

logging.getLogger().addHandler(error_handler)

info_handler = logging.FileHandler('logs/info.log')
info_handler.setLevel(logging.INFO)

info_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s - File "%(filename)s", line %(lineno)d')
info_handler.setFormatter(info_formatter)

logging.getLogger().addHandler(info_handler)

def main():
    try: 
        url = ask_for_url()
        response = get_html(url)

        soup = parse_html(response)

        if response is None:
            logging.error
            return

        inputId = ask_for_id()
        responeId = search_by_id(soup, inputId)

        inputType = ask_for_type()
        responeType = search_by_type(soup, inputType)

        inputClass = ask_for_class()
        responeClass = search_by_class(soup, inputClass)
        logging.info("Busqueda por id " + inputId + " " + str(responeId) + "\n" + "Busqueda por type " + inputType + " " + str(responeType) + "\n" + "Busqueda por class " + inputClass + " " + str(responeClass))

        if ask_for_save():
            logging.info("Saving data...")
            data = {"ID": responeId, "Type": responeType, "Class": responeClass}
            try:
                save_in_csv(data)
                logging.info("Data saved in data/scraped_data.csv")
            except Exception as e:
                logging.error(f"Error al guardar los datos: {e}")
        else:
            logging.info("Data not saved")
    except Exception as e:
        logging.error(f"Error: {e}")


if __name__ == "__main__":
    main()