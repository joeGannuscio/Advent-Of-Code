from math import prod

def part1(input_file):
    input = readInputFile(input_file)
    low_points = []
    for i, x in enumerate(input):
        for j, y in enumerate(input[i]):
            neighbors = []
            moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

            for move in moves:
                if i + move[0] in range(len(input)) and j + move[1] in range(len(input)):
                    neighbors.append(input[i + move[0]][j + move[1]])
            if min(neighbors) > y:
                low_points.append(y)
    risk_levels = [p+1 for p in low_points]
    print(sum(risk_levels))
    return




def part2(input_file):
    input = readInputFile(input_file)
    low_coords = []
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for i, x in enumerate(input):
        for j, y in enumerate(input[i]):
            neighbors = []


            for move in moves:
                if i + move[0] in range(len(input)) and j + move[1] in range(len(input)):
                    neighbors.append(input[i + move[0]][j + move[1]])
            if min(neighbors) > y:
                low_coords.append((i, j))

    basins = []
    for point in low_coords:

        visited = [point]
        queue = [point]

        while queue:
            point = queue.pop(0)
        
            for move in moves:
                if point[0] + move[0] in range(len(input)) and point[1] + move[1] in range(len(input[0])):
                    neighbor_val = input[point[0]+move[0]][point[1]+move[1]]
                    neighbor_coord = (point[0]+move[0], point[1]+move[1])

                    if neighbor_coord not in visited and neighbor_val != 9 and neighbor_val > input[point[0]][point[1]]:
                        visited.append(neighbor_coord)
                        queue.append(neighbor_coord)

        basins.append(len(visited))

    basins = sorted(basins)
    print(prod(basins[-3:]))

    return


def readInputFile(path):
    with open(path) as file:
        lines = file.readlines()
        raw_input = [line.strip() for line in lines]
        return [[int(c) for c in x] for x in raw_input]


if __name__ == '__main__':
    part1('Inputs/day9.txt')
    part2('Inputs/day9.txt')
