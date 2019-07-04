#try:
#import rdoclient
#import requests
from math import gcd
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



publicKey, privateKey = RSA(32449733, 32452843)
print(RSA(32449733,32452843))
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
