from intcode import Intcode

def main():
    inputs = readInput('Inputs/day19.txt')
    part1(inputs)

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

def readInput(path):
    with open(path) as file:
        line = file.readline()
        vals = line.split(',')
        return [int(i) for i in vals]

if __name__ == '__main__':
    main()