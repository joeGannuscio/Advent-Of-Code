import re

def part1(input_file):
    inputs = read_input_file(input_file)
    directions = []

    for input in inputs:
        directions.append(re.findall(r'e|ne|nw|se|sw|w',input))

    black_tiles = get_black_tiles(directions)

    print(len(black_tiles))
            

def part2(input_file):
    inputs = read_input_file(input_file)
    directions = []

    for input in inputs:
        directions.append(re.findall(r'e|ne|nw|se|sw|w',input))

    black_tiles = get_black_tiles(directions)

    for _ in range(100):
        next_round = set()
        for tile in black_tiles:
            neighbors = get_neighbors(tile)
            if 0 < count_neighbors(neighbors, black_tiles) <= 2:
                next_round.add(tile)
            for neighbor in neighbors:
                new_neighbors = get_neighbors(neighbor)
                if count_neighbors(new_neighbors, black_tiles) == 2:
                    next_round.add(neighbor)
        black_tiles = next_round

    print(len(black_tiles))


def get_neighbors(tile):
    x = tile[0]
    y = tile[1]

    return [(x + 1, y), (x - 1, y), (x + 0.5, y + 0.5), (x + 0.5, y - 0.5), (x - 0.5, y + 0.5), (x - 0.5, y - 0.5)]

def count_neighbors(neighbors, black_tiles):
    count = 0
    for neighbor in neighbors:
        if neighbor in black_tiles:
            count += 1

    return count

def get_black_tiles(directions):
    black_tiles = set()

    for direction in directions:
        x, y = 0, 0
        for d in direction:
            if d == 'e':
                x += 1
            elif d == 'ne':
                x += 0.5
                y += 0.5
            elif d == 'se':
                x += 0.5
                y -= 0.5
            elif d == 'w':
                x -= 1
            elif d == 'nw':
                x -= 0.5
                y += 0.5
            elif d == 'sw':
                x -= 0.5
                y -= 0.5

        tile = (x, y)
        
        if tile in black_tiles:
            black_tiles.remove(tile)
        else:
            black_tiles.add(tile)

    return black_tiles


def read_input_file(path):
    with open(path) as file:
        lines = file.readlines()
        return [line.strip() for line in lines]


if __name__ == '__main__':
    part1('Inputs/day24.txt')
    part2('Inputs/day24.txt')
