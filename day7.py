import itertools

def main():
    inputs = readInput('Inputs/day7.txt')
    part1(inputs)
    part2(inputs)

def part1(inputs):
    vals = inputs[:]
    phases = list(itertools.permutations([0,1,2,3,4]))
    
    bigResult = 0
    for phase in phases:
        result = 0
        for p in phase:
            result = runProgram(vals, (p, result))
        if (result > bigResult):
            bigResult = result
    print(bigResult)

def part2(inputs):
    vals = inputs[:]

def runProgram(steps, userInput):
    opCode, modes = processOpCode(steps[0])
    index = 0
    inputIndex = 0

    while(opCode != 99):
        if (opCode == 1): #add
            param1 = steps[steps[index + 1]] if modes[2] == 0 else steps[index + 1]
            param2 = steps[steps[index + 2]] if modes[1] == 0 else steps[index + 2]
            val = param2 + param1
            if modes[0] == 1:
                steps[index + 3] = val
            else:
                steps[steps[index + 3]] = val
            index += 4
        elif (opCode == 2): #multiply
            param1 = steps[steps[index + 1]] if modes[2] == 0 else steps[index + 1]
            param2 = steps[steps[index + 2]] if modes[1] == 0 else steps[index + 2]
            val = param1 * param2
            if modes[0] == 1:
                steps[index + 3] = val
            else:
                steps[steps[index + 3]] = val
            index += 4
        elif (opCode == 3): #input
            steps[steps[index + 1]] = userInput[inputIndex]
            inputIndex += 1
            index += 2
        elif (opCode == 4): #output
            #print('Output: ' + str(steps[steps[index + 1]]))
            result = steps[steps[index + 1]]
            index += 2
            return result
        elif (opCode == 5): #jump if true
            param1 = steps[steps[index + 1]] if modes[2] == 0 else steps[index + 1]
            param2 = steps[steps[index + 2]] if modes[1] == 0 else steps[index + 2]
            if param1 != 0:
                index = param2
            else:
                index += 3
        elif (opCode == 6): #jump if false
            param1 = steps[steps[index + 1]] if modes[2] == 0 else steps[index + 1]
            param2 = steps[steps[index + 2]] if modes[1] == 0 else steps[index + 2]
            if param1 == 0:
                index = param2
            else:
                index += 3
        elif (opCode == 7): #less than
            param1 = steps[steps[index + 1]] if modes[2] == 0 else steps[index + 1]
            param2 = steps[steps[index + 2]] if modes[1] == 0 else steps[index + 2]
            val = 1 if param1 < param2 else 0
            if modes[0] == 1:
                steps[index + 3] = val
            else:
                steps[steps[index + 3]] = val
            index += 4
        elif (opCode == 8): #equal to
            param1 = steps[steps[index + 1]] if modes[2] == 0 else steps[index + 1]
            param2 = steps[steps[index + 2]] if modes[1] == 0 else steps[index + 2]
            val = 1 if param1 == param2 else 0
            if modes[0] == 1:
                steps[index + 3] = val
            else:
                steps[steps[index + 3]] = val
            index += 4

        else:
            break

        opCode, modes = processOpCode(steps[index])

    return steps

def processOpCode(value):
    #pad zeros
    value = f'{value:05}'
    digits = [int(digit) for digit in value]
    #last 2 are always opCode
    opCode = int(str(digits[-2] + digits[-1]))
    modes = (digits[0], digits[1], digits[2])
    return opCode, modes
    

def readInput(path):
    with open(path) as file:
        line = file.readline()
        vals = line.split(',')
        return [int(i) for i in vals]

if __name__ == '__main__':
    main()