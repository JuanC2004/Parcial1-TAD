'''
Author: Juan Camilo Quintero
Date: 21/09/2022
Language: Python 3.0
'''



dictionary={
    "serie": '',
    "number_seasons": 0,
    "original_lenguage": '',
    "features_seasons": [{
        "season_number": 0,
        "season_name": '',    
        "premier_date": '',
        "cast": [],    
        "episodes": [{
            "episode_name": '',
            "time_duration": 0 
                }]      
    }]
}    
def actor_search():
    actor_name = input("Ingrese el nombre del actor al que desea buscar: ")
    for i in dictionary:
        for j in i["features_seasons"]:
            for k in j["cast"]:
                if k == actor_name:
                    print(f"En la serie {i} participa el actor buscado")

def language_search():
    language = input("Ingrese el idioma a buscar ")
    for serie_index in dictionary:
        if serie_index["original_lenguage"] == language:
            print(f"La serie en la que se tiene este idioma es: {serie_index["serie"]}")

def premier_date_search():
    premier_date = input("Premier Date: ")
    for serie_index in dictionary:
        for season_index in serie_index["features_seasons"]:
            if season_index["premier_date"] == premier_date:
                del serie_index