def filtrar(data, country):
    # Usamos filter y lambda para buscar el país deseado
    return list(filter(lambda item: item["Country"] == country, data))


def get_population(data_diccionario):
    # Definimos los años que nos interesan analizar
    years = ["2022", "2020", "2015", "2010", "2000", "1990", "1980", "1970"]

    # Creamos el diccionario usando Dictionary Comprehension y hacemos el cast a int
    dict_años = {
        year: int(data_diccionario[f"{year} Population"])
        for year in years
        if f"{year} Population" in data_diccionario
    }

    labels = list(dict_años.keys())
    values = list(dict_años.values())

    return labels, values
