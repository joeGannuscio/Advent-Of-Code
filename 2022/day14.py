from itertools import pairwise


def part1(input_path):
    cave = read_input_file(input_path)

    floors = [c[1] for c in cave]
    floor = max(floors)
    count = 0
    while drop_sand(cave, floor):
        count += 1

    print(count)

    return


def part2(input_path):
    cave = read_input_file(input_path)

    floors = [c[1] for c in cave]
    floor = max(floors) + 1
    count = 0
    while drop_sand2(cave, floor):
        count += 1

    print(count)  # this solution is off by 1 for some reason...

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


def drop_sand2(cave, floor):
    # sand starts at 500, 0
    # falls 1 step at a time
    # check directly below, then down left, then down right
    # infinite floor, sand is blocked when sand rises to 500, 0

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

        if (sx, sy) == (500, 0):
            return False
        cave.add((sx, sy))

        return True

    # hits the floor
    cave.add((sx, sy))
    return True


def read_input_file(path):
    with open(path) as file:
        cave = set()
        for line in file.readlines():
            coords = line.split(' -> ')
            pts = []
            for c in coords:
                c = c.split(',')
                pts.append((int(c[0]), int(c[1])))

            for p1, p2 in pairwise(pts):
                p1x, p1y = p1
                p2x, p2y = p2

                if p1x == p2x:
                    for i in range(min(p1y, p2y), max(p1y, p2y) + 1):
                        cave.add((p1x, i))
                else:
                    for j in range(min(p1x, p2x), max(p1x, p2x) + 1):
                        cave.add((j, p1y))

    return cave


if __name__ == '__main__':
    part1('Inputs/day14.txt')
    part2('Inputs/day14.txt')
