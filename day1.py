def part1(input_file):
    input = readInputFile(input_file)
    int_input = [int(i) for i in input]

    for i in int_input:
        value_needed = 2020 - i
        if value_needed in int_input:
            print(i * value_needed)
            return


def part2(input_file):
    input = readInputFile(input_file)
    int_input = [int(i) for i in input]

    for i in range(len(int_input)):
        for j in range(i+1, len(int_input)):
            for k in range(j+1, len(int_input)):
                if (int_input[i] + int_input[j] + int_input[k] == 2020):
                    print(int_input[i] * int_input[j] * int_input[k])


def readInputFile(path):
    with open(path) as file:
        lines = file.readlines()
        return [line.strip() for line in lines]

if __name__ == '__main__':
    part1('Inputs/day1.txt')
    part2('Inputs/day1.txt')