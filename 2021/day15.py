from queue import PriorityQueue

import numpy as np


def part1(input_file):
    input = readInputFile(input_file)
    print(find_path(input))
    return


def part2(input_file):
    input = readInputFile(input_file)
    map = np.array(input)
    map = make_big_map(map)
    # map = np.block([[(map + i + j - 1) % 9 + 1 for i in range(5)] for j in range(5)])

    print(find_path(map))
    return


def find_path(map):

    end_x = len(map)
    end_y = len(map[0])
    queue = PriorityQueue()
    queue.put((0, (0, 0)))
    visited = {(0, 0)}

    while queue:
        risk, (cur_x, cur_y) = queue.get()
        if cur_x == end_x - 1 and cur_y == end_y - 1:
            return risk
        for x, y in [(cur_x + 1, cur_y), (cur_x - 1, cur_y), (cur_x, cur_y + 1), (cur_x, cur_y - 1)]:
            if 0 <= x < end_x and 0 <= y < end_y and (x, y) not in visited:
                point_risk = map[x][y]
                queue.put((point_risk + risk, (x, y)))
                visited.add((x, y))


def make_big_map(map):
    map = np.concatenate([map + i for i in range(5)], axis=0)
    map = np.concatenate([map + j for j in range(5)], axis=1)
    map[map > 9] -= 9
    return map


def readInputFile(path):
    with open(path) as file:
        lines = file.readlines()
        raw_input = [line.strip() for line in lines]
        return [[int(c) for c in x] for x in raw_input]


if __name__ == '__main__':
    part1('Inputs/day15.txt')
    part2('Inputs/day15.txt')
