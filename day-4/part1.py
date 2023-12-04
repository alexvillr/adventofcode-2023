from dataclasses import dataclass


@dataclass
class Card:
    id: int
    winningNums: [int]
    ownedNums: [int]
    total: int


points = [x * 2 for x in range(100)]
info: [str] = [line for line in open('small-input').read().split('\n') if len(line) > 5]
cards: [Card] = []

def get_numbers(numbers: [str]) -> [int]:
    lastWasNum: bool = False
    result: [int] = []
    tmp = ''

    for c in numbers:
        if not c.isdigit():
            if lastWasNum:
                result.append(int(tmp))
                tmp = ''
                lastWasNum = False
        else:
            tmp += c
            lastWasNum = True

    if lastWasNum:
        result.append(int(tmp))

    return result

for line in info:
    split_line: [str] = line.split(':')
    tmp = ''
    for c in split_line[0]:
        if c.isdigit():
            tmp += c
    id: int = int(tmp)

    cardNumbers: [str] = split_line[1].split('|')
    winningNums: [int] = get_numbers(cardNumbers[0])
    ownedNums: [int] = get_numbers(cardNumbers[1])

    cards.append(Card(id, winningNums, ownedNums, 0))

count = 0

for card in cards:
    for num in card.ownedNums:
        if num in card.winningNums:
            card.total += 1
    # print(f'card {card.id} is worth {card.total} points')
    # print(f'and has {card.ownedNums} with winning numbers of {card.winningNums}')

    count += points[card.total]

print(count)
