from itertools import combinations

def part1(input_path):
    galaxies, blank_cols, blank_rows = read_input_file(input_path)

    sum = 0

    for pair in combinations(galaxies, 2):
        x0 = pair[0][1]
        y0 = pair[0][0]
        x1 = pair[1][1]
        y1 = pair[1][0]
        dist = get_manhattan_distance(y0, x0, y1, x1)

        # check how many cols added
        for i in range(min(x0, x1) + 1, max(x0, x1)):
            if i in blank_cols:
                dist += 1


        # check how many rows added
        for j in range(min(y0, y1) + 1, max(y0, y1)):
            if j in blank_rows:
                dist += 1

        sum += dist

    print(sum)

    return 


def part2(input_path):
    galaxies, blank_cols, blank_rows = read_input_file(input_path)

    sum = 0

    for pair in combinations(galaxies, 2):
        x0 = pair[0][1]
        y0 = pair[0][0]
        x1 = pair[1][1]
        y1 = pair[1][0]
        dist = get_manhattan_distance(y0, x0, y1, x1)

        # check how many cols added
        for i in range(min(x0, x1) + 1, max(x0, x1)):
            if i in blank_cols:
                dist += 999999


        # check how many rows added
        for j in range(min(y0, y1) + 1, max(y0, y1)):
            if j in blank_rows:
                dist += 999999

        sum += dist

    print(sum)

    return 


def get_manhattan_distance(y0, x0, y1, x1):
    return abs(x0 - x1) + abs (y0 - y1)


def read_input_file(path):
    galaxies = []
    blank_rows = []
    blank_cols = []
    with open(path) as file:
        lines = file.readlines()

        for y, line in enumerate(lines):
            if all(c == '.' for c in line.strip()):
                blank_rows.append(y)
                next
            for x, c in enumerate(line.strip()):
                if c == '#':
                    galaxies.append((y, x))
            
        for i in range(len(lines[0])-1):
            if check_col(i, lines):
                blank_cols.append(i)

    return galaxies, blank_cols, blank_rows


def check_col(idx, lines):
    for line in lines:
        if line[idx] == '#':
            return False
        
    return True


if __name__ == '__main__':
    part1('Inputs/day11.txt')
    part2('Inputs/day11.txt')
