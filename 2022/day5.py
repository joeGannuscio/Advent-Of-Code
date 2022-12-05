import re


def part1(input_path):
    stacks, directions = read_input_file(input_path)

    for direction in directions:
        direction = direction.split()
        move = int(direction[1])
        source = int(direction[3]) - 1
        destination = int(direction[5]) - 1

        for i in range(move):
            moving = stacks[source].pop()
            stacks[destination].append(moving)

    result = []
    for j in range(len(stacks)):
        if len(stacks[j]) != 0:
            result.append(stacks[j][-1])

    print(''.join(result))
    return


def part2(input_path):
    stacks, directions = read_input_file(input_path)
    for direction in directions:
        direction = direction.split()
        move = int(direction[1])
        source = int(direction[3]) - 1
        destination = int(direction[5]) - 1

        moving = stacks[source][-move:]
        del stacks[source][-move:]
        stacks[destination].extend(moving)

    result = []
    for j in range(len(stacks)):
        if len(stacks[j]) != 0:
            result.append(stacks[j][-1])

    print(''.join(result))

    return


def read_input_file(path):
    with open(path) as file:
        lines = file.readlines()
        stacks = [[] for i in range(10)]
        directions = []
        direction_flag = False

        for line in lines:
            if not direction_flag:
                # can probably do with regex?
                line = line.replace('[', '')
                line = line.replace(']', '')
                blanks = 0
                result = ''
                for c in line:
                    if c == ' ':
                        blanks += 1
                    else:
                        result = result + c
                        blanks = 0
                    if blanks == 4:
                        result = result + '#'
                        blanks = 0

                if '1' in result:
                    continue
                if result == '\n':
                    direction_flag = True
                    continue

                result = result.strip()

                crates = [*result]

                for i, c in enumerate(crates):
                    if c == '#':
                        print('skip')
                    else:
                        stacks[i].insert(0,c)

            else:
                directions.append(line.strip())

        return stacks, directions



if __name__ == '__main__':
    part1('Inputs/day5.txt')
    part2('Inputs/day5.txt')
