def part1(input_file):
    input = readInputFile(input_file)
    grid = input_to_grid(input)

    total_flashes = 0
    for i in range(100):
        total_flashes += step(grid)
    print(total_flashes)
    return


def part2(input_file):
    input = readInputFile(input_file)
    grid = input_to_grid(input)
    counter = 1
    while step(grid) != 100:
        counter += 1
    print(counter)
    return


def input_to_grid(input):
    grid = {}

    for i in range(10):
        for j in range(10):
            grid[(i, j)] = input[i][j]

    return grid


def step(grid):
    flash_count = 0
    octopi = grid.keys()
    directions = [(1,0), (0,1), (-1,0), (0,-1), (1,1), (1,-1), (-1,1),(-1,-1)]

    while octopi:
        adjacents = []

        for coord in octopi:
            grid[coord] += 1
            if grid[coord] == 10:
                for dir in directions:
                    if coord[0] + dir[0] in range(10) and coord[1] + dir[1] in range(10):
                        adjacents.append((coord[0]+dir[0], coord[1]+dir[1]))

            octopi = adjacents

    for coord in grid.keys():
        if grid[coord] >= 10:
            flash_count += 1
            grid[coord] = 0

    return flash_count


def readInputFile(path):
    with open(path) as file:
        lines = file.readlines()
        raw_input = [line.strip() for line in lines]
        return [[int(c) for c in x] for x in raw_input]


if __name__ == '__main__':
    part1('Inputs/day11.txt')
    part2('Inputs/day11.txt')
