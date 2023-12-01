def part_one():
    houses = {"0 0": 1}
    x = 0
    y = 0
    for char in lines:
        if char == '^':
            y += 1
        elif char == 'v':
            y -= 1
        elif char == '>':
            x += 1
        elif char == '<':
            x -= 1
        key = str(x) + " " + str(y)
        if key in houses:
            houses[key] += 1
        else:
            houses[key] = 1
    print(len(houses.keys()), " Häuser wurden mindestens einmal beliefert.")

def part_two():
    houses = {"0 0": 1}
    sx = 0
    sy = 0
    divider = 1
    rx = 0
    ry = 0
    for char in lines:
        if char == '^':
            if divider % 2 == 1:
                sy += 1
            else:
                ry += 1
        elif char == 'v':
            if divider % 2 == 1:
                sy -= 1
            else:
                ry -= 1
        elif char == '>':
            if divider % 2 == 1:
                sx += 1
            else:
                rx += 1
        elif char == '<':
            if divider % 2 == 1:
                sx -= 1
            else:
                rx -= 1
        if divider % 2 == 1:
            key = str(sx) + " " + str(sy)
        else:
            key = str(rx) + " " + str(ry)
        if key in houses:
            houses[key] += 1
        else:
            houses[key] = 1
        divider += 1
    print(len(houses.keys()), " Häuser wurden von Santa und Robo-Santa mindestens einmal beliefert.")

file = open("Türchen 3/input.txt", "r")
lines = file.readline()
part_one()
part_two()