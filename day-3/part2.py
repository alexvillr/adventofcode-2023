from dataclasses import dataclass

@dataclass
class Gear:
    location: (int,)
    numbers: [int]

@dataclass
class Number:
    number: str
    counted: bool
    occupies: [(int,)]

numbers = []
schematic = []
activated_cells = []
gears = []

def get_neighbourhood(cell: (int,)):
    return [
        (cell[0] - 1, cell[1] - 1),
        (cell[0], cell[1] - 1),
        (cell[0] + 1, cell[1] - 1),
        (cell[0] - 1, cell[1]),
        (cell[0], cell[1]),
        (cell[0] + 1, cell[1]),
        (cell[0] - 1, cell[1] + 1),
        (cell[0], cell[1] + 1),
        (cell[0] + 1, cell[1] + 1),
    ]

with open("input") as file:
    for i, line in enumerate(file):
        schematic.append([])
        lastWasNum = False
        for j, character in enumerate(line):
            if character == '\n':
                continue
            schematic[i].append(character)
            if (not character.isdigit()) and (character != '.'):
                if character == '*':
                    newGear = Gear((i, j), [])
                    gears.append(newGear)
                lastWasNum = False
                # print(f'{i}, {j} --> {get_neighbourhood((i, j))}')
                for activated in get_neighbourhood((i, j)):
                    if activated not in activated_cells:
                        activated_cells.append(activated)
            if character.isdigit():
                if lastWasNum:
                    numbers[-1].number += character
                    numbers[-1].occupies.append((i, j))
                else:
                    newNum = Number(character, False, [(i, j)])
                    numbers.append(newNum)
                lastWasNum = True
            else:
                lastWasNum = False

for num in numbers:
    for location in num.occupies:
        if location in activated_cells:
            num.counted = True

partNumbers = [x for x in numbers if x.counted]

for gear in gears:
    for num in partNumbers:
        numAdded = False
        for cell in num.occupies:
            if numAdded:
                continue
            else:
                if gear.location in get_neighbourhood(cell):
                    # print(gear.location)
                    gear.numbers.append(int(num.number))
                    numAdded = True
count = 0
for gear in gears:
    # print(gear.numbers)
    if len(gear.numbers) == 2:
        count += (gear.numbers[0] * gear.numbers[1])

print(count)
