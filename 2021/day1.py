def part1(input_file):
    input = readInputFile(input_file)
    inc_count = 0
    for (i, x) in enumerate(input):
        if x > input[i - 1]:
            inc_count += 1
    print(inc_count)
    return

def part2(input_file):
    input = readInputFile(input_file)
    windows = get_window(input)
    inc_count = 0
    for (i, x) in enumerate(windows):
        if x > windows[i - 1]:
            inc_count += 1
    print(inc_count)


    return


def get_window(data):
    windows = [(data[i] + data[i + 1] + data[ i + 2]) for i in range(len(data) - 2)]
    return windows


def readInputFile(path):
    with open(path) as file:
        lines = file.readlines()
        return [int(line.strip()) for line in lines]


if __name__ == '__main__':
    part1('Inputs/day1.txt')
    part2('Inputs/day1.txt')
