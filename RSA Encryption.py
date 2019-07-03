#try:
#import rdoclient
#import requests
from math import gcd
import random
"""except  ImportError:
    import pip, sys, re
    packagesNames=["requests","rdoclient"]
    pip.main(['install'] + packagesNames + ['--upgrade'])

    if __name__ == '__main__':
        sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
        sys.exit(main())"""

def openFile():
    file = open("primes2.txt", "r")
    full = file.read()
    file.close()
    lines = full.split("\n")
    print(len(lines))
    row = lines[0].split(",")
    row = row[:-1]
    print(row)

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

def coPrime(x):
    """
    Finds a random co-prime of given number
    """

    n = x * 2 + 100000  # Upper limit for range of random integers
    y = random.randint(x * 2, n)
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



publicKey, privateKey = RSA(53, 59)
print(RSA(53,59))
mensaje = "h"
lista = int("".join(str(ord(c)) for c in mensaje))
print(lista)

listaEncrip=(encriptar(publicKey, lista))
print("encrip")
print(listaEncrip)

listaDesen = (desencriptar(privateKey, listaEncrip))
print("des")
print(listaDesen)


