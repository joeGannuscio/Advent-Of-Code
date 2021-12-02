def part1(input_file):
    input = readInputFile(input_file)
    position = 0
    depth = 0
    for dir in input:
        if dir[0] == 'forward':
            position += int(dir[1])

        if dir[0] == 'down':
            depth += int(dir[1])
        elif dir[0] == 'up':
            depth -= int(dir[1])
            if depth < 0:
                depth = 0
    print(position*depth)
    return

def part2(input_file):
    input = readInputFile(input_file)
    position = 0
    depth = 0
    aim = 0
    for dir in input:
        if dir[0] == 'forward':
            position += int(dir[1])
            depth += aim*int(dir[1])
            if depth < 0:
                depth = 0
        
        if dir[0] == 'down':
            aim += int(dir[1])
        elif dir[0] == 'up':
            aim -= int(dir[1])

    print(position*depth)
    return


def readInputFile(path):
    with open(path) as file:
        lines = file.readlines()
        return [line.split() for line in lines]


if __name__ == '__main__':
    part1('Inputs/day2.txt')
    part2('Inputs/day2.txt')
