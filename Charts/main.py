import charts  # Asegúrate de tener tu archivo charts.py en la misma carpeta
import readcsv
import utils


def run():
    # Definimos la ruta absoluta hacia tu archivo de datos CSV
    path = r"/home/myst/proyecto-python-platzi-wsl/Charts/paises.csv"
    # 1. Leemos los datos mediante nuestro módulo especializado
    data = readcsv.read_csv(path)

    # 2. Solicitamos el país al usuario
    country = input("Type Country => ").capitalize()

    # 3. Filtramos la información del país seleccionado
    result = utils.filtrar(data, country)

    if len(result) > 0:
        country_data = result[0]  # Extraemos el primer diccionario que coincide

        # 4. Procesamos los años y las poblaciones haciendo el respectivo casteo a entero
        labels, values = utils.get_population(country_data)

        # 5. Enviamos los datos ordenados al módulo de gráficas
        charts.generate_pychart(labels, values)
    else:
        print("País no encontrado en la base de datos.")


if __name__ == "__main__":
    run()
