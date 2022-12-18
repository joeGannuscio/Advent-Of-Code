def part1(input_path):
    input = read_input_file(input_path)

    surface_area = 0
    for cube in input:
        open_sides = 6
        for neighbor in get_neighbors(*cube):
            if neighbor in input:
                open_sides -= 1
        surface_area += open_sides

    print(surface_area)

    return


def part2(input_path):
    input = read_input_file(input_path)

    return


def get_neighbors(x, y, z):
    moves = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
    for move in moves:
        yield((x + move[0], y + move[1], z + move[2]))


def read_input_file(path):
    coords = []
    with open(path) as file:
        for line in file.readlines():
            x, y, z = map(int, line.split(','))
            coords.append((x, y, z))

    return coords


if __name__ == '__main__':
    part1('Inputs/day18.txt')
    part2('Inputs/day18.txt')
