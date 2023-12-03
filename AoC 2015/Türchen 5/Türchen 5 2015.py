import re

def partOne():
    sum = 0
    regex = r"\b(?:\w*[aeiouAEIOU]){3}\w*"
    doubleChar = r"(.)\1"
    for line in text:
        if re.findall(regex, line) and re.findall(doubleChar, line) and notBlacklisted(line):
            sum += 1
    print("Es sind",sum,"Strings nice.")

def notBlacklisted(line):
    for item in ['ab','cd','pq','xy']:
        if item in line:
            return False
    return True

def partTwo():
    sum = 0
    doublePair = r"(\w{2}).*?(\1)"
    doubleBetween = r"(.).\1"
    for line in text:
        if re.findall(doublePair, line) and re.findall(doubleBetween, line):
            sum += 1
    print("Es sind",sum,"Strings in Teil 2 nice.")

file = open("Türchen 5/input.txt", 'r')
text = file.readlines()
partOne()
partTwo()