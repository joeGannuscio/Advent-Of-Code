def part1(input_path):
    input = read_input_file(input_path)

    print(find_start_of_packet(input, 4))

    return


def part2(input_path):
    input = read_input_file(input_path)

    print(find_start_of_packet(input, 14))

    return


def find_start_of_packet(buffer, marker_size):
    for i in range(len(buffer)):
        marker = set(buffer[i:i+marker_size])

        if len(marker) == marker_size:
            return i + marker_size

    return 0


def read_input_file(path):
    with open(path) as file:
        return file.readline()


if __name__ == '__main__':
    part1('Inputs/day6.txt')
    part2('Inputs/day6.txt')
