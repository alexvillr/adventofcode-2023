from dataclasses import dataclass

@dataclass
class Number:
    number: str
    counted: bool
    occupies: [(int,)]

numbers = []
schematic = []
activated_cells = []

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
                lastWasNum = False
                schematic[i][j] = '#'
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

count = 0

for num in numbers:
    # print(f'{num.number} counted? {num.counted}\nOccupies: {num.occupies}')
    if num.counted:
        count += int(num.number)
    # print("======================")

print(count)
