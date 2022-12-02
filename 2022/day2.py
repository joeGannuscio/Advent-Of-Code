def part1(input_path):
    input = read_input_file(input_path)

    mapping = {'A': 1, 'B': 2, 'C': 3, 'X': 1, 'Y': 2, 'Z': 3}
    score = 0
    for i in input:
        score += score_round(i[0], i[1], mapping)

    print(score)
    return


def part2(input_path):
    input = read_input_file(input_path)
    mapping = {'A': 1, 'B': 2, 'C': 3}

    score = 0
    for i in input:
        score += score_round2(i[0], i[1], mapping)

    print(score)
    return


def score_round2(elfs_shape, required_result, mapping):

    if required_result == 'Y':
        return 3 + mapping[elfs_shape]
    if required_result == 'Z':
        if mapping[elfs_shape] == 3:
            return 6 + 1
        else:
            return 6 + mapping[elfs_shape] + 1
    if required_result == 'X':
        if mapping[elfs_shape] == 1:
            return 3
        else:
            return mapping[elfs_shape] - 1


def score_round(elfs_shape, your_shape, mapping):
    rules_dict = {'A': 'Y', 'B': 'Z', 'C': 'X'}
    if mapping[elfs_shape] == mapping[your_shape]:
        return mapping[your_shape] + 3
    if rules_dict[elfs_shape] == your_shape:
        return mapping[your_shape] + 6
    else:
        return mapping[your_shape]


def read_input_file(path):
    with open(path) as file:
        lines = file.readlines()
        return [[c for c in line.strip() if c != ' '] for line in lines]


if __name__ == '__main__':
    part1('Inputs/day2.txt')
    part2('Inputs/day2.txt')
