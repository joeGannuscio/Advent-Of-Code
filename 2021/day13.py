from collections import defaultdict


def part1(input_file):
    input = readInputFile(input_file)
    coords, folds = parse_input(input)
    grid = fill_grid(coords)
    folded_grid = fold_grid(grid, folds[0][0], folds[0][1])
    print(len(folded_grid))
    return


def part2(input_file):
    input = readInputFile(input_file)
    coords, folds = parse_input(input)
    grid = fill_grid(coords)

    for fold in folds:
        grid = fold_grid(grid, fold[0], fold[1])

    for y in range(max(grid)[1] + 1):
        print(''.join('#' if (x, y) in grid else ' ' for x in range(max(grid)[0] + 1)))

    return


def fill_grid(coords):
    grid = defaultdict(lambda: 1)
    for x, y in coords:
        grid[(x, y)]

    return grid


def fold_grid(grid, direction, fold_along):
    folded_grid = defaultdict(lambda: 1)
    for x, y in grid:
        if direction == 'x':
            if x < fold_along:
                folded_grid[(x, y)] = 1
            else:
                dist = x - fold_along
                folded_grid[(x - 2*dist, y)]
        if direction == 'y':
            if y < fold_along:
                folded_grid[(x, y)] = 1
            else:
                dist = y - fold_along
                folded_grid[(x, y - 2*dist)]
    return folded_grid


def parse_input(input):
    coords = []
    folds = []
    fold_flag = False
    for i in input:
        if not fold_flag and i != '':
            coords.append(tuple([int(j) for j in i.split(',')]))
        elif i == '':
            fold_flag = True
            continue
        else:
            fold_line = i[11:].split('=')
            folds.append((fold_line[0], int(fold_line[1])))

    return coords, folds


def readInputFile(path):
    with open(path) as file:
        lines = file.readlines()
        return [line.strip() for line in lines]


if __name__ == '__main__':
    part1('Inputs/day13.txt')
    part2('Inputs/day13.txt')
