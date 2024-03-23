import requests

def get_pokemon_info(pokemon_name):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}"
    response = requests.get(url)
    
    if response.status_code == 200:
        pokemon_data = response.json()
        print(f"Nombre: {pokemon_data['name']}")
        print("Habilidades:")
        for ability in pokemon_data['abilities']:
            print(f"- {ability['ability']['name']}")
        print("Tipos:")
        for type_entry in pokemon_data['types']:
            print(f"- {type_entry['type']['name']}")
    else:
        print(f"No se pudo obtener la información del Pokémon {pokemon_name}. Código de estado: {response.status_code}")

# Ejemplo de uso
pokemon_name = input("Introduce el nombre de un Pokémon: ")
get_pokemon_info(pokemon_name)

