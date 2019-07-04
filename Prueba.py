import subprocess
import sys
import requests


def instalation():
    subprocess.call([sys.executable, "-m", "pip", "install", "rdoclient"])
    subprocess.call([sys.executable, "-m", "pip", "install", "requests"])



def main():
    url = "https://api.random.org/json-rpc/2/invoke"

    data = {"jsonrpc": "2.0", "method": "generateIntegers",
            "params": {"apiKey": "320139d2-6163-4904-a1da-ecaabec303b2", "n": 3, "min": 0, "max": 1000000}, "id": 42}
    response = requests.post(url, json=data)

    numbers = response.json()
    lista = numbers["result"]["random"]["data"]
    print(lista)
    print(lista[0])

    #data=response.json()





main()