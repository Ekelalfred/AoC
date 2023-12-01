import hashlib

def partOne(key):
    answer = 1
    while True:
        hashStr = key + str(answer)
        hash = hashlib.md5(hashStr.encode())
        if hash.hexdigest()[0:5] == '00000':
            print("Die Antwort lautet", answer)
            return
        answer += 1

def partTwo(key):
    answer = 0
    while True:
        hashStr = key + str(answer)
        if hashlib.md5(hashStr.encode()).hexdigest().startswith('000000'):
            print("Die Antwort lautet", answer)
            return
        answer += 1

file = open("Türchen 4/input.txt", "r")
key = file.read().strip()
partOne(key)
partTwo(key)