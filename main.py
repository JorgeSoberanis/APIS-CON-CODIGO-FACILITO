import requests
import json


if __name__ == '__main__':
    url = 'https://httpbin.org/post'
    payload = {'nombre': 'Jorge', 'Curso': 'Python', 'Nivel': 'Intermedio'}


    reponse = requests.post(url, data= json.dumps(payload))

    #JSON post se encarga de serializarlos
    #data entonces nosotros lo serializamos

    print(reponse.url)

    if reponse.status_code == 200:
        print(reponse.content)
        print("Hola")
