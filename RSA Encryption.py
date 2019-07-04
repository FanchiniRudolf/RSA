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

#extended euclid alg; ax + by = gcd(a, b) -> ax  ≡ 1 (mod m)

def modInverse(base, m):
    """
    Calculates modular multiplicate inverse
    """

    g, x, y = mod_inverse_iterative(base, m)
    if (g != 1):
        return None
    else:
        return (x % m)


def mod_inverse_iterative(a, b):
    """
    Helps mod_inverse work
    """

    x, y, u, v = 0, 1, 1, 0
    while a != 0:
        q, r = b // a, b % a
        m, n = x - u * q, y - v * q
        b, a, x, y, u, v = a, r, u, v, m, n
    return b, x, y


def randomInt(min, max):
    url = "https://api.random.org/json-rpc/2/invoke"

    if 10**9<max:
        min = 500000000
        max = 1000000000


    data = {"jsonrpc": "2.0", "method": "generateIntegers",
            "params": {"apiKey": "320139d2-6163-4904-a1da-ecaabec303b2", "n": 2, "min": min, "max": max}, "id": 42}
    response = requests.post(url, json=data)

    numbers = response.json()
    lista = numbers["result"]["random"]["data"]
    return lista[0]


def coPrime(x):
    """
    Finds a random co-prime of given number
    """

    n = x * 2 + 100000  # Upper limit for range of random integers
    y = randomInt(x * 2, n)
    if (gcd(x, y) != 1):
        return coPrime(x)
    else:
        return y

def RSA(p, q):
    n= p*q
    fi = (p-1)*(q-1)
    e = coPrime(fi)
    d = modInverse(e,fi)
    publicKey = (e, n)
    privateKey = (d, n)
    return publicKey, privateKey

def encriptar(publikKey, mensaje):
    mensajeEncriptado = pow(mensaje, publicKey[0], publicKey[1])
    return mensajeEncriptado


def desencriptar(privateKey, cifrado):
    mensajeDesencriptado = pow(int(cifrado), int(privateKey[0]), int(publicKey[1]))
    return mensajeDesencriptado

index= randomMillion()
print(index)
primes = openFile(index)
print(primes)
publicKey, privateKey = RSA(primes[0], primes[1])
print(publicKey)
print(privateKey)
mensaje = "hola"
lista = int("".join(str(ord(c)) for c in mensaje))
print("mensaje")
print(lista)

listaEncrip=(encriptar(publicKey, lista))
print("encrip")
print(listaEncrip)

listaDesen = (desencriptar(privateKey, listaEncrip))
print("des")
print(listaDesen)
