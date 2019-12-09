import itertools
from intcode import Intcode

def main():
    inputs = readInput('Inputs/day7.txt')
    part1(inputs)
    part2(inputs)

def part1(inputs):
    vals = inputs[:]
    phases = list(itertools.permutations([0,1,2,3,4]))

    maxResult = 0

    for phase in phases:
        result = 0
        for p in phase:
            intcodeRunner = Intcode(inputs[:])
            intcodeRunner.inputs = [p, result]
            intcodeRunner.run()
            result = intcodeRunner.outputs[-1]
        if (result > maxResult):
            maxResult = result

    print(maxResult)

def part2(inputs):
    vals = inputs[:]    

def readInput(path):
    with open(path) as file:
        line = file.readline()
        vals = line.split(',')
        return [int(i) for i in vals]

if __name__ == '__main__':
    main()