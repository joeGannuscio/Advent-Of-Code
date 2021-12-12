caves = {}


def part1(input_file):
    input = readInputFile(input_file)
    global caves
    caves = get_cave_graph(input)
    print(dfs('start', {'start'}))
    return


def part2(input_file):
    input = readInputFile(input_file)
    global caves
    caves = get_cave_graph(input)
    print(dfs2('start', {'start'}, True))
    return


def dfs(cave, visited):
    if cave == 'end':
        return 1

    count = 0

    for next in caves[cave]:
        if next.islower():
            if next not in visited:
                count += dfs(next, visited | {next})
        else:
            count += dfs(next, visited)
    return count


def dfs2(cave, visited, can_revisit):
    if cave == 'end':
        return 1

    count = 0

    for next in caves[cave]:
        if next.islower():
            if next not in visited:
                count += dfs2(next, visited | {next}, can_revisit)
            elif can_revisit and next not in {'start', 'end'}:
                count += dfs2(next, visited | {next}, False)
        else:
            count += dfs2(next, visited, can_revisit)
    return count


def get_cave_graph(input):
    caves = {}
    for i, j in input:
        if i not in caves:
            caves[i] = []
        if j not in caves:
            caves[j] = []
        caves[i].append(j)
        caves[j].append(i)

    return caves


def readInputFile(path):
    with open(path) as file:
        lines = file.readlines()
        return [tuple(line.strip().split('-')) for line in lines]


if __name__ == '__main__':
    part1('Inputs/day12.txt')
    part2('Inputs/day12.txt')
