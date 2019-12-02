def main():
    inputs = readInput('Inputs/day2.txt')
    part1(inputs)
    part2(inputs)

def part1(inputs):
    inputs[1] = 12
    inputs[2] = 2
    vals = inputs[:]
    
    result = runProgram(vals)
    print(result[0])

def part2(inputs):
    result = 0

    for i in range(100):
        for j in range(100):
            vals = inputs[:]
            vals[1] = i
            vals[2] = j
            result = runProgram(vals)


            if result[0] == 19690720:
                print(100 * result[1] + result[2])
                return

def runProgram(steps):
    opCode = steps[0]
    index = 0

    while(opCode != 99):
        if (opCode == 1):
            val = steps[steps[index + 1]] + steps[steps[index + 2]]
        elif (opCode == 2):
            val = steps[steps[index + 1]] * steps[steps[index + 2]]
        else:
            break

        steps[steps[index + 3]] = val
        index += 4
        opCode = steps[index]

    return steps

def readInput(path):
    with open(path) as file:
        line = file.readline()
        vals = line.split(',')
        return [int(i) for i in vals]

if __name__ == '__main__':
    main()