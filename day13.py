from intcode import Intcode

def main():
    input = readInput('Inputs/day13.txt')
    part1(input)
    part2(input)

def part1(input):
    intcodeRunner = Intcode(input)

    while not intcodeRunner.done:
        intcodeRunner.run()

    tiles = intcodeRunner.outputs[2::3]

    print(tiles.count(2))

def part2(input):
    intcodeRunner = Intcode(input)
    intcodeRunner.memory[0] = 2
    intcodeRunner.inputs = [0]
    
    score = 0
    paddle = 0

    while not intcodeRunner.done:
        intcodeRunner.run()
        outputs = [intcodeRunner.outputs[x:x+3] for x in range(0, len(intcodeRunner.outputs), 3)]

        for output in outputs:
            x = output[0]
            y = output[1]
            tile = output[2]

            if (x, y) == (-1, 0):
                score = tile
            if tile == 3:
                print(f'paddle at ({x, y})')
                paddle = x
            elif tile == 4:
                print(f'ball at ({x, y})')
                if x > paddle:
                    inp = 1
                elif x < paddle:
                    inp = -1

                



    print(score)

def readInput(path):
    with open(path) as file:
        line = file.readline()
        vals = line.split(',')
        return [int(i) for i in vals]

if __name__ == '__main__':
    main()