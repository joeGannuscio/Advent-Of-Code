from collections import defaultdict


def part1(input_file):
    input = readInputFile(input_file)
    coords = parse_input(input)
    points = defaultdict(lambda: 1)

    for coord in coords:
        x1 = coord[0][0]
        y1 = coord[0][1]
        x2 = coord[1][0]
        y2 = coord[1][1]

        if x1 == x2:
            for y in range(min(y1, y2), max(y1, y2) + 1):
                if (x1, y) in points:
                    points[(x1, y)] = points[(x1, y)] + 1
                else:
                    points[(x1, y)]

        if y1 == y2:
            for x in range(min(x1, x2), max(x1, x2) + 1):
                if (x, y1) in points:
                    points[(x, y1)] = points[(x, y1)] + 1
                else:
                    points[(x, y1)]

    print(len([p for p in points.values() if p >= 2]))
    return


def part2(input_file):
    input = readInputFile(input_file)
    coords = parse_input(input)
    points = defaultdict(lambda: 1)

    for coord in coords:
        x1 = coord[0][0]
        y1 = coord[0][1]
        x2 = coord[1][0]
        y2 = coord[1][1]

        if x1 == x2:
            for y in range(min(y1, y2), max(y1, y2) + 1):
                if (x1, y) in points:
                    points[(x1, y)] = points[(x1, y)] + 1
                else:
                    points[(x1, y)]

        if y1 == y2:
            for x in range(min(x1, x2), max(x1, x2) + 1):
                if (x, y1) in points:
                    points[(x, y1)] = points[(x, y1)] + 1
                else:
                    points[(x, y1)]

        # diagonal, this is not great but it works
        if x1 > x2 and y1 > y2:
            y = y2
            for x in range(x2, x1+1):
                if (x, y) in points:
                    points[(x, y)] = points[(x, y)] + 1
                else:
                    points[(x, y)]
                y += 1

        if x1 < x2 and y1 > y2:
            y = y1
            for x in range(x1, x2+1):
                if (x, y) in points:
                    points[(x, y)] = points[(x, y)] + 1
                else:
                    points[(x, y)]
                y -= 1

        if x1 > x2 and y1 < y2:
            y = y2
            for x in range(x2, x1+1):
                if (x, y) in points:
                    points[(x, y)] = points[(x, y)] + 1
                else:
                    points[(x, y)]
                y -= 1

        if x1 < x2 and y1 < y2:
            y = y1
            for x in range(x1, x2+1):
                if (x, y) in points:
                    points[(x, y)] = points[(x, y)] + 1
                else:
                    points[(x, y)]
                y += 1

    print(len([p for p in points.values() if p >= 2]))
    return


def parse_input(input):
    pairs = [s.split(' -> ') for s in input]
    coords = []
    for p in pairs:
        line = []
        for c in p:
            line.append([int(x) for x in c.split(',')])
        coords.append(line)
    return coords


def readInputFile(path):
    with open(path) as file:
        lines = file.readlines()
        return [line.strip() for line in lines]


if __name__ == '__main__':
    part1('Inputs/day5.txt')
    part2('Inputs/day5.txt')
