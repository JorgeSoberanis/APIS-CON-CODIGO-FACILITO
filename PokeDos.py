
import requests

def get_pokemons(url='http://pokeapi.co/api/v2/pokemon-form/', offset = 0):
    args ={'offset' : offset} if offset else {}


    response = requests.get(url, params=args)
    if response.status_code == 200:

         payload = response.json()
         results = payload.get("results", [])

         if results:
             for pokemon in results:
                 name = pokemon['name']
                 print(name)

        #next = raw_input("Continuar listando? [Y/N]") NO SE COMO PONER EL UTF-8:(
        #if next == "y"  Si se consume bien, solo el siguiente paso falla por el UTF-8
        #    get_pokemons(offset = offset+20)
if __name__ == '__main__':
    url = 'http://pokeapi.co/api/v2/pokemon-form/'
    get_pokemons()
