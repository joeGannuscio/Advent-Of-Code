def part1(input_path):
    input = read_input_file(input_path)

    MAX_VALS = {'red': 12, 'green': 13, 'blue': 14}
    sum = 0
    for id in input:
        if is_possible(input[id], MAX_VALS):
            sum += int(id)

    print(sum)
    return 

def is_possible(game, max_dict):
    for pull in game:
        for cube in pull:
            num = cube[0]
            color = cube[1]
            max = max_dict[color]
            if num > max:
                return False
        
    return True


def part2(input_path):
    input = read_input_file(input_path)

    sum = 0
    for id in input:
        sum += get_power(input[id])

    print(sum)

    return


def get_power(game):
    color_max = {'red':0, 'green': 0, 'blue': 0}
    for pull in game:
        for cube in pull:
            num = cube[0]
            color = cube[1]

            cur_max = color_max[color]

            if cur_max < num:
                color_max[color] = num

    return color_max['red']*color_max['green']*color_max['blue']


def read_input_file(path):
    games = {}
    with open(path) as file:
        lines = file.readlines()
        for line in lines:
            colon = line.strip().split(':')
            id = colon[0][5:]
            pulls = colon[1].strip()
            pull_split = pulls.split(';')

            parsed_pulls = []
            for p in pull_split:
                parse = []
                pull = p.split(',')
                for d in pull:
                    (num, color) = d.strip().split(' ')[0], d.strip().split(' ')[1]
                    parse.append((int(num),color))
                parsed_pulls.append(parse)
            games[id] = parsed_pulls
    return games


if __name__ == '__main__':
    part1('Inputs/day2.txt')
    part2('Inputs/day2.txt')
