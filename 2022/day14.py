from itertools import pairwise

def part1(input_path):
    input = read_input_file(input_path)
    cave = build_cave(input)

    floors = [c[1] for c in cave]
    floor = max(floors)
    count = 0
    while drop_sand(cave, floor):
        count += 1

    print(count)

    return


def part2(input_path):
    input = read_input_file(input_path)

    return


def drop_sand(cave, floor):
    # sand starts at 500, 0
    # falls 1 step at a time
    # check directly below, then down left, then down right
    # if sand y is bigger than the deepest floor then its falling into the abyss

    sx, sy = 500, 0

    while sy < floor:
        # check down
        if (sx, sy + 1) not in cave:
            sy += 1
            continue

        # check left
        if (sx - 1, sy + 1) not in cave:
            sx -= 1
            sy += 1
            continue

        # check right
        if (sx + 1, sy + 1) not in cave:
            sx += 1
            sy += 1
            continue

        cave.add((sx, sy))
        return True

    return False


def build_cave(input):
    cave = set()
    for start, end in pairwise(input):

        # vertical
        if start[0] == end[0]:
            x = start[0]
            ys = [start[1], end[1]]
            for i in range(min(ys), max(ys) + 1):
                cave.add((x, i))

        # horizontal
        elif start[1] == end[1]:
            xs = [start[0], end[0]]
            y = start[1]
            for i in range(min(xs), max(xs) + 1):
                cave.add((i, y))

    return cave


def read_input_file(path):
    with open(path) as file:
        coords = []
        for line in file.readlines():
            for coord in line.strip().split('->'):
                x, y = coord.strip().split(',')
                coords.append((int(x), int(y)))

    return coords


if __name__ == '__main__':
    part1('Inputs/day14.txt')
    part2('Inputs/day14.txt')
