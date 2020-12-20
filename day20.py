class Tile:
    
    def __init__(self, id, data):
        self.id = id
        self.data = data
        self.top = data[0]
        self.bottom = data[-1]
        self.left = ''.join([row[0] for row in data])
        self.right = ''.join([row[-1] for row in data])

def part1(input_file):
    inputs = read_input_file(input_file)

    tiles = []

    for input in inputs:
        tiles.append(Tile(input[1][:-1], input[2:]))

    for i in range(len(tiles)):
        for j in range(i+1, len(tiles)):
            # check lr
            if tiles[i].left == tiles[j].right:
                print(f'{tiles[i].id} left of {tiles[j].id}')
            # check rl
            if tiles[i].right == tiles[j].left:
                print(f'{tiles[i].id} right of {tiles[j].id}')
            # check tb
            if tiles[i].top == tiles[j].bottom:
                print(f'{tiles[i].id} below {tiles[j].id}')
            # check bt
            if tiles[i].bottom == tiles[j].top:
                print(f'{tiles[i].id} above {tiles[j].id}')
        


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
