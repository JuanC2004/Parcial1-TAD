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

def feature1():
    dictionary_counter=3
    for i in range (1, dictionary_counter+1) :
        dictionary["serie"] = input(f"Ingrese el nombre de la serie {i}: ")
        dictionary["number_seasons"] = int(input(f"Ingrese el numero de temporadas de la serie {i}: "))
        dictionary["original_lenguage"] = input(f"Ingrese el idioma original de la serie {i}: ")
        dicitionary[] 