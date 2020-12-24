import itertools
from intcode import Intcode

def main():
    inputs = readInput('Inputs/day7.txt')
    #part1(inputs)
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
    phases = list(itertools.permutations([5,6,7,8,9]))    
    maxResult = 0

    for phase in phases:
        #initialize amplifiers
        ampA = Intcode(inputs[:], True)
        ampA.inputs = [phase[0],0]
        ampB = Intcode(inputs[:], True)
        ampB.inputs = [phase[1]]
        ampC = Intcode(inputs[:], True)
        ampC.inputs = [phase[2]]
        ampD = Intcode(inputs[:], True)
        ampD.inputs = [phase[3]]
        ampE = Intcode(inputs[:], True)
        ampE.inputs = [phase[4]]

        #feedback loop
        while not ampE.done:
            ampA.run()
            ampB.inputs.append(ampA.outputs[-1])
            ampB.run()
            ampC.inputs.append(ampB.outputs[-1])
            ampC.run()
            ampD.inputs.append(ampC.outputs[-1])
            ampD.run()
            ampE.inputs.append(ampD.outputs[-1])
            ampE.run()
            ampA.inputs.append(ampE.outputs[-1])
        if ampE.outputs[-1] > maxResult:
            maxResult = ampE.outputs[-1]
    print(maxResult)

def readInput(path):
    with open(path) as file:
        line = file.readline()
        vals = line.split(',')
        return [int(i) for i in vals]

if __name__ == '__main__':
    main()