import itertools
from intcode import Intcode

def main():
    inputs = readInput('Inputs/day9.txt')
    part1(inputs)
    part2(inputs)

def part1(inputs):
    vals = inputs[:]
    intcodeRunner = Intcode(vals)
    intcodeRunner.inputs = [1]
    intcodeRunner.run()
    results = intcodeRunner.outputs
    print(results)
    
def part2(inputs):
    vals = inputs[:]
    intcodeRunner = Intcode(vals)
    intcodeRunner.inputs = [2]
    intcodeRunner.run()
    results = intcodeRunner.outputs
    print(results)

def readInput(path):
    with open(path) as file:
        line = file.readline()
        vals = line.split(',')
        return [int(i) for i in vals]

if __name__ == '__main__':
    main()