def calcPackage(line):
    measures = line.split("x")
    measures = list(map(int, measures))
    measures.sort()
    seiten = list()
    seite1 = measures[0] * measures[1]
    seite2 = measures[0] * measures[2]
    seite3 = measures[1] * measures[2]
    seiten.append(seite1)
    seiten.append(seite2)
    seiten.append(seite3)
    seiten.sort()
    return (seiten[0] + 2*seiten[0] + 2*seiten[1] + 2*seiten[2], 2*measures[0] + 2*measures[1] + measures[0]*measures[1]*measures[2])

file = open("Türchen 2/input.txt", "r")
text = file.readlines()
summe = 0
summeBand = 0
for line in text:
    tuple = calcPackage(line)
    summe += tuple[0]
    summeBand += tuple[1]
print(summe, summeBand)
file.close()