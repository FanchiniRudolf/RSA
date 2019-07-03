import subprocess
import sys
import json
import requests
import random
import queue
#from multiprocessing import Queue

def main():
    subprocess.call([sys.executable, "-m", "pip", "install", 'rdoclient'])
    subprocess.call([sys.executable, "-m", "pip", "install", 'requests'])
    url = 'https://api.random.org/json-rpc/2/invoke'

    data = {'jsonrpc': '2.0', 'method': 'generateIntegers',
            'params': {'apiKey': '320139d2-6163-4904-a1da-ecaabec303b2', 'n': 10, 'min': 1, 'max': 10, 'replacement': 'true'}, 'id': 42}



    response = requests.post(url, data)
    params = json.dumps(data)
    print(params)
    #data=response.json()
    print(response.text)
    #print(response.text)
    #from rdoclient import RandomOrgClient

    #r = RandomOrgClient("320139d2-6163-4904-a1da-ecaabec303b2", blocking_timeout=60.0 * 60.0, http_timeout=30.0)
    #c = r.create_integer_cache(5, 0, 10)
    #try:
     #   c.get()
    #except Queue.Empty:
     #   lista = [0] * 5
      #  for i in range(5):
       #     lista[i] = random.random()





main()