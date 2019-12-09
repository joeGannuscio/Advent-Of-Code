from intcode import Intcode

def main():
    inputs = readInput('Inputs/day5.txt')
    part1(inputs)
    part2(inputs)

def part1(inputs):
    intcodeRunner = Intcode(inputs[:])
    intcodeRunner.run([1])

def part2(inputs):
    intcodeRunner = Intcode(inputs[:])
    intcodeRunner.run([5])

def readInput(path):
    with open(path) as file:
        line = file.readline()
        vals = line.split(',')
        return [int(i) for i in vals]

if __name__ == '__main__':
    main()