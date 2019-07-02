# origin https://primes.utm.edu/lists/small/millions/
file = open("primes2.txt", "r")
full = file.read()
file.close()
lines = full.split("\n\n")
texto = ""
for x in range(0, len(lines)):
    temp = lines[x].split(" ")
    while "" in temp:
        temp.remove("")
    texto +=  "\n"
    for x in temp:
        texto += x +","
file = open("primes2.txt", "w")
file.write(texto)