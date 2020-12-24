import itertools
from collections import defaultdict

class Tile:
    
    def __init__(self, id, data):
        self.id = id
        self.data = data
        self.top = data[0]
        self.bottom = data[-1]
        self.left = ''.join([row[0] for row in data])
        self.right = ''.join([row[-1] for row in data])


    def get_sides_as_list(self):
        return [self.top, self.bottom, self.left, self.right]

def part1(input_file):
    inputs = read_input_file(input_file)

    tiles = []
    matches = defaultdict(int)

    for input in inputs:
        tiles.append(Tile(input[1][:-1], input[2:]))

    for x, y in itertools.combinations(tiles, 2):
        x_sides = x.get_sides_as_list()
        y_sides = y.get_sides_as_list()

        for x_side in x_sides:
            for y_side in y_sides:
                if x_side == y_side or x_side == y_side[::-1]:
                    matches[x.id] += 1
                    matches[y.id] += 1

    product = 1

    for side, count in matches.items():
        if count == 2:
            product *= int(side)

    print(product)
        


def part2(input_file):
    print('part2')


def read_input_file(path):
    with open(path) as file:
        lines = file.read()
        lines = lines.split('\n\n')
        return [line.replace('\n', ' ').split(' ') for line in lines]


if __name__ == '__main__':
    part1('Inputs/day20.txt')
    part2('Inputs/day20.txt')
