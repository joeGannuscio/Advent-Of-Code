def part1(input_path):
    input = read_input_file(input_path)

    count = 0
    for assignment in input:
        a1 = int(assignment[0][0])
        a2 = int(assignment[0][1])
        b1 = int(assignment[1][0])
        b2 = int(assignment[1][1])

        if (a1 <= b1 and a2 >= b2) or (b1 <= a1 and b2 >= a2):
            count += 1

    print(count)
    return


def part2(input_path):
    input = read_input_file(input_path)

    count = 0
    for assignment in input:
        a1 = int(assignment[0][0])
        a2 = int(assignment[0][1])
        b1 = int(assignment[1][0])
        b2 = int(assignment[1][1])

        if b1 <= a1 <= b2 or b1 <= a2 <= b2 or a1 <= b1 <= a2 or a1 <= b2 <= a2:
            count += 1

    print(count)

    return


def read_input_file(path):
    with open(path) as file:
        lines = file.readlines()
        assignments = []
        for line in lines:
            temp = line.strip().split(',')
            assignments.append([x.split('-') for x in temp])
        return assignments


if __name__ == '__main__':
    part1('Inputs/day4.txt')
    part2('Inputs/day4.txt')
