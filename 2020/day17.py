from operator import itemgetter

def part1(input_file):
    inputs = read_input_file(input_file)

    living_cubes = set()

    for x, row in enumerate(inputs):
        for y, char in enumerate(row):
            if char == '#':
                living_cubes.add((x,y,0))

    print(living_cubes)

    for _ in range(6):
        living_cubes = run_cycle(living_cubes)

    print(len(living_cubes))

def count_living_neighbors(living_cubes, x, y, z):
    count = 0

    for x1 in range(x - 1, x + 2):
        for y1 in range(y - 1, y + 2):
            for z1 in range(z - 1, z + 2):
                if (x, y, z) != (x1, y1, z1):
                    if (x1, y1, z1) in living_cubes:
                        count += 1

    return count

def run_cycle(living_cubes):
    updated = set()

    for x in range(min(map(itemgetter(0), living_cubes)) - 1, max(map(itemgetter(0), living_cubes)) + 2):
        for y in range(min(map(itemgetter(1), living_cubes)) - 1, max(map(itemgetter(1), living_cubes)) + 2):
            for z in range(min(map(itemgetter(2), living_cubes)) - 1, max(map(itemgetter(2), living_cubes)) + 2):
                living_neighbors = count_living_neighbors(living_cubes, x, y, z)

                if (x, y, z) in living_cubes:
                    if living_neighbors == 2 or living_neighbors == 3:
                        updated.add((x, y, z))
                elif living_neighbors == 3:
                    updated.add((x, y, z))

    return updated


def part2(input_file):
    inputs = read_input_file(input_file)

    living_cubes = set()

    for x, row in enumerate(inputs):
        for y, char in enumerate(row):
            if char == '#':
                living_cubes.add((x, y, 0, 0))

    print(living_cubes)

    for _ in range(6):
        living_cubes = run_cycle2(living_cubes)

    print(len(living_cubes))

def run_cycle2(living_cubes):
    updated = set()

    for x in range(min(map(itemgetter(0), living_cubes)) - 1, max(map(itemgetter(0), living_cubes)) + 2):
        for y in range(min(map(itemgetter(1), living_cubes)) - 1, max(map(itemgetter(1), living_cubes)) + 2):
            for z in range(min(map(itemgetter(2), living_cubes)) - 1, max(map(itemgetter(2), living_cubes)) + 2):
                for w in range(min(map(itemgetter(3), living_cubes)) - 1, max(map(itemgetter(3), living_cubes)) + 2):
                    living_neighbors = count_living_neighbors2(living_cubes, x, y, z, w)

                    if (x, y, z, w) in living_cubes:
                        if living_neighbors == 2 or living_neighbors == 3:
                            updated.add((x, y, z, w))
                    elif living_neighbors == 3:
                        updated.add((x, y, z, w))

    return updated


def count_living_neighbors2(living_cubes, x, y, z, w):
    count = 0

    for x1 in range(x - 1, x + 2):
        for y1 in range(y - 1, y + 2):
            for z1 in range(z - 1, z + 2):
                for w1 in range(w - 1, w + 2):
                    if (x, y, z, w) != (x1, y1, z1, w1):
                        if (x1, y1, z1, w1) in living_cubes:
                            count += 1

    return count


def read_input_file(path):
    with open(path) as file:
        lines = file.readlines()
        return [list(line.strip()) for line in lines]


if __name__ == '__main__':
    part1('Inputs/day17.txt')
    part2('Inputs/day17.txt')
