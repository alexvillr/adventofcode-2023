NUM_RED = 12
NUM_GREEN = 13
NUM_BLUE = 14

def check_game(grabs: [(int,)]):
    for grab in grabs:
        if grab[0] > NUM_RED:
            return False
        elif grab[1] > NUM_GREEN:
            return False
        elif grab[2] > NUM_BLUE:
            return False
    return True

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
        game_id = ""
        for c in info[0]:
            if c.isdigit():
                game_id += c
        game_id_num = int(game_id)
        if check_game(process_game(info[1])):
            count += game_id_num

    print(count)
        

