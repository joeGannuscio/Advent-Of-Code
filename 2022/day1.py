def part1(input_path):
    input = read_input_file(input_path)

    sums = [sum(i) for i in input]
    print(max(sums))
    return


def part2(input_path):
    input = read_input_file(input_path)

    sums = [sum(i) for i in input]
    sums.sort()
    print(sum(sums[-3:]))
    return


def read_input_file(path):
    parsed_input = []
    with open(path) as file:
        lines = file.readlines()
        temp_list = []
        for line in lines:
            if line != '\n':
                temp_list.append(int(line.strip()))
            else:
                parsed_input.append(temp_list[:])
                temp_list.clear()

    return parsed_input


if __name__ == '__main__':
    part1('Inputs/day1.txt')
    part2('Inputs/day1.txt')
