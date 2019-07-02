file = open("primes1.txt", "r")
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
file = open("primes1.txt", "w")
file.write(texto)