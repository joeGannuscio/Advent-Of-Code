def part1(input_path):
    input = read_input_file(input_path)

    sum = 0
    for i in input:
        ext = extrapolate(i)
        sum += ext

    print(sum)
    return 


def extrapolate(row):
    if row[0] == 0 and sum(row) == 0:
        return 0
    
    diffs = []
    for i in range(len(row)-1):
        diffs.append(row[i+1] - row[i])
    return row[-1] + extrapolate(diffs)

def part2(input_path):
    input = read_input_file(input_path)

    sum = 0
    for i in input:
        ext = extrapolate2(i)
        sum += ext

    print(sum)
    return 

def extrapolate2(row):
    if row[0] == 0 and sum(row) == 0:
        return 0
    
    diffs = []
    for i in range(len(row)-1):
        diffs.append(row[i+1] - row[i])
    return row[0] - extrapolate2(diffs)


def read_input_file(path):
    input = []
    with open(path) as file:
        lines = file.readlines()

        for line in lines:
            input.append([int(c) for c in line.split()])

    return input


if __name__ == '__main__':
    part1('Inputs/day9.txt')
    part2('Inputs/day9.txt')
