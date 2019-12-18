from intcode import Intcode
from collections import defaultdict

def main():
    input = readInput('Inputs/day13.txt')
    part1(input)
    part2(input)

def part1(input):
    intcodeRunner = Intcode(input)
    tiles = defaultdict(tuple)
    count = 0

    while not intcodeRunner.done:
        intcodeRunner.run()

    for i in range(0, len(intcodeRunner.outputs), 3):
        x, y, tile = intcodeRunner.outputs[i:i+3]
        tiles[(x,y)] = tile

    display(tiles)

    for key, value in tiles.items():
        if value == 2:
            count += 1
    print(count)

def display(tiles):
    minX = min(x for x,_ in tiles)
    maxX = max(x for x,_ in tiles)
    minY = min(y for _,y in tiles)
    maxY = max(y for _,y in tiles)

    height = maxY - minY
    width = maxX - minX

    grid = [[' '] * width for _ in range(height)]

    chars = ' X#_o'

    for y in range(height):
        for x in range(width):
            grid[y][x] = chars[tiles[(x,y)]]

    screen = '\n'.join(''.join(grid[y]) for y in range(height))
        
    print(screen)

def part2(input):
    intcodeRunner = Intcode(input)
    intcodeRunner.memory[0] = 2
    tiles = {}
    
    score = 0
    paddle = 0

    while not intcodeRunner.done:
        intcodeRunner.run()

        inp = 0

        for i in range(0, len(intcodeRunner.outputs), 3):
            x, y, tile = intcodeRunner.outputs[i:i+3]
            tiles[(x,y)] = tile

            if (x, y) == (-1, 0):
                score = tile

            if tile == 3:
                paddle = x
            elif tile == 4:
                if x > paddle:
                    inp = 1
                elif x < paddle:
                    inp = -1

        print(display(tiles))
        intcodeRunner.inputs.append(inp)
        intcodeRunner.outputs.clear()

    print(score)

def readInput(path):
    with open(path) as file:
        line = file.readline()
        vals = line.split(',')
        return [int(i) for i in vals]

if __name__ == '__main__':
    main()