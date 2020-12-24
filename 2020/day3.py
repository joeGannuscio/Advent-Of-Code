import math

def part1(input_file):
    input = read_input_file(input_file)
    x = 0
    y = 0
    tree_count = 0

    for row in input:
        if x >= len(row):
            x = x - len(row)

        if row[x] == '#':
            tree_count += 1

        x += 3

    print(tree_count)


def part2(input_file):
    input = read_input_file(input_file)
    slopes = [[1,1],[3,1],[5,1],[7,1],[1,2]]
    tree_counts = []

    for slope in slopes:
        x = 0
        y = 0
        tree_count = 0


        while y < len(input):
            row = input[y]
            if x >= len(row):
                x = x - len(row)

            if row[x] == '#':
                tree_count += 1           

            x += slope[0]
            y += slope[1]

        tree_counts.append(tree_count)
    
    print(math.prod(tree_counts))
    print(tree_counts)


def read_input_file(path):
    with open(path) as file:
        lines = file.readlines()
        return [list(line.strip()) for line in lines]


if __name__ == '__main__':
    part1('Inputs/day3.txt')
    part2('Inputs/day3.txt')
