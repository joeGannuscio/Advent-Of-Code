def part1(input_file):
    input = readInputFile(input_file)
    outputs = []
    for i in input:
        outputs.append(i[1].strip().split(' '))

    total = 0
    for o in outputs:
        for v in o:
            if len(v) == 2 or len(v) == 3 or len(v) == 4 or len(v) == 7:
                total += 1
    
    print(total)
    return

def part2(input_file):
    input = readInputFile(input_file)
    return



def readInputFile(path):
    with open(path) as file:
        lines = file.readlines()
        return [line.strip().split('|') for line in lines]


if __name__ == '__main__':
    part1('Inputs/day8.txt')
    part2('Inputs/day8.txt')