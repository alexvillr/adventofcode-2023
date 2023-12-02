import re

digits_only = re.compile(r'[^1-9]')
count = 0
with open('input') as file:
    for row in file:
        tmp = re.sub(digits_only, '', row)
        count += int(f'{tmp[0]}{tmp[-1]}')

print(count)
