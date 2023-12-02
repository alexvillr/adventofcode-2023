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
count = 0
with open('input') as file:
    for row in file:
        only_nums = []
        index = 0
        while index < len(row):
            if row[index].isdigit():
                only_nums.append(row[index])
            for num in numbers:
                if (index < (len(row) - len(num))) and (
                    row[index : index + len(num)] == num
                ):
                    only_nums.append(numbers.index(num) + 1)
            index += 1
        if len(only_nums) != 0:
            count += int(f'{only_nums[0]}{only_nums[-1]}')
    print(count)
