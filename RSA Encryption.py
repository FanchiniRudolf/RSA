def instalation():
    subprocess.call([sys.executable, "-m", "pip", "install", "requests"])
    subprocess.call([sys.executable, "-m", "pip", "install", "math"])


try:
    import subprocess
    import sys
    import requests
    from math import gcd, ceil
except  ImportError:
    import subprocess
    import sys
    instalation()
    import requests
    from math import gcd

def randomMillion():
    url = "https://api.random.org/json-rpc/2/invoke"

    data = {"jsonrpc": "2.0", "method": "generateIntegers",
            "params": {"apiKey": "320139d2-6163-4904-a1da-ecaabec303b2", "n": 2, "min": 0, "max": 1000000}, "id": 42}
    response = requests.post(url, json=data)

    numbers = response.json()
    lista = numbers["result"]["random"]["data"]
    return lista

def openFile(index):
    file = open("primes2.txt", "r")
    full = file.read()
    file.close()
    lines = full.split("\n")
    primes = []
    for position in index:
        row = lines[ceil(position/8)-1].split(",")
        if position%8==0:
            column = 7
        else:
            column = position%8
        primes.append(int(row[column]))
    return primes

def RSA(p, q):
    n= p*q
    fi = (p-1)*(q-1)
    e = fi-1
    coprime = gcd(e,fi)
    coprimeN = gcd(e,n)
    while coprime!=1 and coprimeN != 1:
        e -= 1
        coprime = gcd(e, fi)
        coprimeN = gcd(e, n)

    d = e+1
    while (e*d)%fi !=1:
        d+=1
    publicKey = (e, n)
    privateKey = (d, n)
    print(n)
    return publicKey, privateKey

def encriptar(publikKey, mensaje):
    mensajeEncriptado = pow(mensaje, publicKey[0])
    mensajeEncriptado = mensajeEncriptado%publicKey[1]
    return mensajeEncriptado


def desencriptar(privateKey, cifrado):
    mensajeDesencriptado = pow(cifrado, privateKey[0], publicKey[1])
    return mensajeDesencriptado

index= randomMillion()
print(index)
primes = openFile(index)
print(primes)
publicKey, privateKey = RSA(primes[0], primes[1])
print(publicKey)
print(privateKey)
mensaje = "hola soy german"
lista = int("".join(str(ord(c)) for c in mensaje))
print(lista)
listaEncrip=[]
for simbol in lista:
    listaEncrip.append(encriptar(publicKey, simbol))
print("encrip")
print(listaEncrip)

listaDesen = []
for simbol in listaEncrip:
    listaDesen.append(desencriptar(privateKey, simbol))
print("des")
print(listaDesen)
