# main.py
from scraper.scraper import *
from scraper.utils import *

def main():
    url = ask_for_url()
    response = get_html(url)

    soup = parse_html(response)

    inputId = ask_for_id()
    responeId = search_by_id(soup, inputId)

    inputType = ask_for_type()
    responeType = search_by_type(soup, inputType)

    inputClass = ask_for_class()
    responeClass = search_by_class(soup, inputClass)

    print("Busqueda por id " + inputId + " " + str(responeId) + "\n" + "Busqueda por type " + inputType + " " + str(responeType) + "\n" + "Busqueda por class " + inputClass + " " + str(responeClass))

    if ask_for_save():
        print("Saving data...")
        data = {"ID": responeId, "Type": responeType, "Class": responeClass}
        print(data)
        try:
            save_in_csv(data)
            print("Data saved in data/scraped_data.csv")
        except Exception as e:
            print(f"Error al guardar los datos: {e}")
    else:
        print("Data not saved")


if __name__ == "__main__":
    main()