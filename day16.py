def main():
    input = readInput('Inputs/day16.txt')
    #part1(input)
    part2(input)

def part1(input):

    for _ in range(100):
        result = []
        for i in range(len(input)):
            pattern = getPattern(i)
            value = 0
            patternIdx = 0
            for i in input:
                if patternIdx < len(pattern):
                    value += (i * pattern[patternIdx])
                else:
                    patternIdx = 0
                    value += (i * pattern[patternIdx])
                patternIdx += 1
            val = str(value)[-1]
            result.append(int(val))
        input = result
        print(result[:8])

def part2(input):

    skipCount = int(''.join([str(x) for x in input[:7]]))
    digits = (input * 10000)[skipCount:]

    for _ in range(100):
        for i in range(len(digits) - 2, -1, -1):
            digits[i] += digits[i + 1]
            digits[i] %= 10

    print(digits[:8])
    

def getPattern(position):
    basePattern = [0, 1, 0, -1]
    position += 1
    expandedPattern = [x for x in basePattern for i in range(position)] 
    expandedPattern.append(expandedPattern.pop(expandedPattern.index(0)))
    return expandedPattern

def readInput(path):
    with open(path) as file:
        line = file.readline()
    return [int(d) for d in str(line)]

if __name__ == '__main__':
    main()