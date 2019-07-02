
def openFile():
    file = open("primes1.txt", "r")
    full = file.read()
    file.close()
    lines = full.split("\n")
    print(len(lines))
    row = lines[0].split(",")
    print(row[:-1])
    