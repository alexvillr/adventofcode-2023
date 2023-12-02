def check_game(grabs: [(int,)]):
    min_red = 0
    min_green = 0
    min_blue = 0
    for grab in grabs:
        if grab[0] > min_red:
            min_red = grab[0]
        if grab[1] > min_green:
            min_green = grab[1]
        if grab[2] > min_blue:
            min_blue = grab[2]
    return min_red * min_green * min_blue

def get_count(info: str):
    num_str = ""
    for c in info:
        if c.isdigit():
            num_str += c
    return int(num_str)


def process_game(info: str):
    result = []
    split_grabs = info.split(";")
    for grab in split_grabs:
        num_red = 0
        num_green = 0
        num_blue = 0
        count_strings = grab.split(',')
        for colour_count in count_strings:
            if "red" in colour_count:
                num_red = get_count(colour_count)
            elif "green" in colour_count:
                num_green = get_count(colour_count)
            elif "blue" in colour_count:
                num_blue = get_count(colour_count)
        result.append((num_red, num_green, num_blue))
    return result


with open('input') as file:
    count = 0
    for line in file:
        info = line.split(":")
        results = check_game(process_game(info[1]))
        count += results

    print(count)
        

