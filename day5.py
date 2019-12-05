def main():
    inputs = readInput('Inputs/day5.txt')
    part1(inputs)
    #part2(inputs)

def part1(inputs):
    vals = inputs[:]
    
    result = runProgram(vals, 1)

def runProgram(steps, userInput):
    opCode, modes = processOpCode(steps[0])
    index = 0

    while(opCode != 99):
        if (opCode == 1):
            param1 = steps[steps[index + 1]] if modes[2] == 0 else steps[index + 1]
            param2 = steps[steps[index + 2]] if modes[1] == 0 else steps[index + 2]
            val = param2 + param1
            if modes[0] == 1:
                steps[index + 3] = val
            else:
                steps[steps[index + 3]] = val
            index += 4
        elif (opCode == 2):
            param1 = steps[steps[index + 1]] if modes[2] == 0 else steps[index + 1]
            param2 = steps[steps[index + 2]] if modes[1] == 0 else steps[index + 2]
            val = param1 * param2
            if modes[0] == 1:
                steps[index + 3] = val
            else:
                steps[steps[index + 3]] = val
            index += 4
        elif (opCode == 3):
            steps[steps[index + 1]] = userInput
            index += 2
        elif (opCode == 4):
            print('Output: ' + str(steps[steps[index + 1]]))
            index += 2
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