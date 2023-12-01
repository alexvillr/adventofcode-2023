numbers = [
    'one',
    'two',
    'three',
    'four',
    'five',
    'six',
    'seven',
    'eight',
    'nine',
]
part1 = 0
part2 = 0
with open('input') as file:
    for row in file:
        part1set = []
        part2set = []
        index = 0
        while index < len(row):
            if row[index].isdigit():
                part1set.append(row[index])
                part2set.append(row[index])
            for num in numbers:
                if (index < (len(row) - len(num))) and (
                    row[index : index + len(num)] == num
                ):
                    part2set.append(numbers.index(num) + 1)
            index += 1
        if len(part1set) != 0:
            part1 += int(f'{part1set[0]}{part1set[-1]}')
        if len(part2set) != 0:
            part2 += int(f'{part2set[0]}{part2set[-1]}')
    print(part1)
    print(part2)
