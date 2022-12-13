import string


def part1(input_path):
    input = read_input_file(input_path)
    start, end, map = convert_map_to_elevations(input)
    print(bfs(map, start, end))

    return


def part2(input_path):
    input = read_input_file(input_path)
    start, end, map = convert_map_to_elevations(input)
    print(bfs_part2(map, end, 0))

    return


def bfs(map, start, end):

    queue = [(start, 0)]
    visited = []

    while queue:

        point, distance = queue.pop(0)

        if point == end:
            return distance

        if point not in visited:
            visited.append(point)
            for neighbor in get_neighbors(map, point):
                if neighbor in visited:
                    continue

                queue.append((neighbor, distance + 1))

    return


def bfs_part2(map, start, end):
    # start at the end and find the first 0 elevation point

    queue = [(start, 0)]
    visited = []

    while queue:

        point, distance = queue.pop(0)

        if map[point[0]][point[1]] == end:
            return distance

        if point not in visited:
            visited.append(point)
            for neighbor in get_neighbors_part2(map, point):
                if neighbor in visited:
                    continue

                queue.append((neighbor, distance + 1))

    return


def get_neighbors(map, point):
    moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    current_elevation = map[point[0]][point[1]]
    map_height = len(map)
    map_width = len(map[0])

    for move in moves:
        neighbor = (point[0] + move[0], point[1] + move[1])
        if 0 <= neighbor[0] < map_height and 0 <= neighbor[1] < map_width:
            neighbor_elevation = map[neighbor[0]][neighbor[1]]
            if neighbor_elevation <= current_elevation + 1:
                yield neighbor


def get_neighbors_part2(map, point):
    moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    current_elevation = map[point[0]][point[1]]
    map_height = len(map)
    map_width = len(map[0])

    for move in moves:
        neighbor = (point[0] + move[0], point[1] + move[1])
        if 0 <= neighbor[0] < map_height and 0 <= neighbor[1] < map_width:
            neighbor_elevation = map[neighbor[0]][neighbor[1]]
            if neighbor_elevation >= current_elevation - 1:
                yield neighbor


def convert_map_to_elevations(map):
    elevations = [row[:] for row in map]
    start_index = (0, 0)
    end_index = (0, 0)
    for i, row in enumerate(map):
        for j, c in enumerate(row):
            if c == 'S':
                elevations[i][j] = 0
                start_index = (i, j)
                continue

            if c == 'E':
                elevations[i][j] = 25
                end_index = (i, j)
                continue

            elevations[i][j] = string.ascii_lowercase.index(c.lower())

    return start_index, end_index, elevations


def read_input_file(path):
    map = []
    with open(path) as file:
        for line in file.readlines():
            map.append([c for c in line.strip()])
    return map


if __name__ == '__main__':
    part1('Inputs/day12.txt')
    part2('Inputs/day12.txt')
