from intcode import Intcode

def main():
    inputs = readInput('Inputs/day19.txt')
    #part1(inputs)
    part2(inputs)

def part1(inputs):

    count = 0
    for x in range(50):
        for y in range(50):
            intcodeRunner = Intcode(inputs[:])
            intcodeRunner.inputs = [x, y]
            intcodeRunner.run()

            if not intcodeRunner.outputs:
                continue
            if intcodeRunner.outputs[0] == 1:
                print(f'{x}, {y}')
                count += 1

    print(count)

def part2(inputs):

    x = 0
    y = 0

    while not checkPoint(inputs[:], x + 99, y):
        y += 1
        while not checkPoint(inputs[:], x, y + 99):
            x += 1

    print(f'{x}, {y}')
    print(x * 10000 + y)

def checkPoint(inputs, x ,y):
    intcodeRunner = Intcode(inputs[:])
    intcodeRunner.inputs = [x, y]
    intcodeRunner.run()

    if not intcodeRunner.outputs:
        return 0

    return intcodeRunner.outputs[0]

def readInput(path):
    with open(path) as file:
        line = file.readline()
        vals = line.split(',')
        return [int(i) for i in vals]

if __name__ == '__main__':
    main()