from itertools import cycle

def part1(input_path):
    instructions, map = read_input_file(input_path)

    instr_loop = cycle(instructions)

    steps = 0

    loc = 'AAA'

    while loc != 'ZZZ':
        instr = next(instr_loop)
        steps += 1
        if instr == 'L':
            loc = map[loc][0]
        
        if instr == 'R':
            loc = map[loc][1]

    print(steps)

    return 


def part2(input_path):
    input = read_input_file(input_path, True)

    return 


def read_input_file(path):
    instructions = []
    map = {}
    with open(path) as file:
        lines = file.readlines()
        for line in lines:
            if '=' not in line and 'R' in line:
                instructions = [c for c in line.strip()]
            
            if '=' in line:
                node = {}
                l = line.strip().split('=')
                l2 = l[1].strip().replace('(', '').replace(')', '').split(', ')

                map[l[0].strip()] = (l2[0], l2[1])
    return instructions, map


if __name__ == '__main__':
    part1('Inputs/day8.txt')
    part2('Inputs/day8.txt')
