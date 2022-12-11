def part1(input_path):
    input = read_input_file(input_path)

    head = (0, 0)
    tail = (0, 0)

    tail_visited = []
    for instruction in input:
        head, tail, tail_visited = move(head, tail, instruction[0], instruction[1], tail_visited)
        print(f'head: {head}, tail: {tail}')

    print(len(set(tail_visited)))
    return


def part2(input_path):
    input = read_input_file(input_path)

    knots = [(0, 0) for _ in range(10)]
    tail_visited = []
    for instruction in input:
        knots, tail_visited = move_part2(knots, instruction[0], instruction[1], tail_visited)

    print(len(set(tail_visited)))
    return


def move(head, tail, direction, distance, tail_visited = []):
    x_h = head[0]
    y_h = head[1]

    match direction:
        case 'R':
            for _ in range(distance):
                x_h += 1
                tail = move_tail(tail, (x_h, y_h))
                tail_visited.append(tail)
        case 'L':
            for _ in range(distance):
                x_h -= 1
                tail = move_tail(tail, (x_h, y_h))
                tail_visited.append(tail)
        case 'U':
            for _ in range(distance):
                y_h += 1
                tail = move_tail(tail, (x_h, y_h))
                tail_visited.append(tail)
        case 'D':
            for _ in range(distance):
                y_h -= 1
                tail = move_tail(tail, (x_h, y_h))
                tail_visited.append(tail)
    return (x_h, y_h), tail, tail_visited


def move_part2(knots, direction, distance, tail_visited = []):
    head = knots[0]
    x_h = head[0]
    y_h = head[1]

    match direction:
        case 'R':
            for _ in range(distance):
                x_h += 1
                knots[0] = (x_h, y_h)
                # make each previous knot the new head and move the tail
                for i in range(len(knots) - 1):
                    knots[i + 1] = move_tail(knots[i + 1], knots[i])
                tail_visited.append(knots[-1])
        case 'L':
            for _ in range(distance):
                x_h -= 1
                knots[0] = (x_h, y_h)
                for i in range(len(knots) - 1):
                    knots[i + 1] = move_tail(knots[i + 1], knots[i])
                tail_visited.append(knots[-1])

        case 'U':
            for _ in range(distance):
                y_h += 1
                knots[0] = (x_h, y_h)
                for i in range(len(knots) - 1):
                    knots[i + 1] = move_tail(knots[i + 1], knots[i])
                tail_visited.append(knots[-1])

        case 'D':
            for _ in range(distance):
                y_h -= 1
                knots[0] = (x_h, y_h)
                for i in range(len(knots) - 1):
                    knots[i + 1] = move_tail(knots[i + 1], knots[i])
                tail_visited.append(knots[-1])

    return knots, tail_visited


def move_tail(tail, head):
    x_t = tail[0]
    y_t = tail[1]
    x_h = head[0]
    y_h = head[1]
    if is_tail_next_to_head(tail, head):
        return tail
    else:
        # move right
        if y_t == y_h and x_t < x_h:
            return (x_t + 1, y_t)
        # move left
        if y_t == y_h and x_t > x_h:
            return (x_t - 1, y_t)
        # move up
        if x_t == x_h and y_t < y_h:
            return (x_t, y_t + 1)
        # move down
        if x_t == x_h and y_t > y_h:
            return (x_t, y_t - 1)
        # up right diagonal
        if x_t < x_h and y_t < y_h:
            return (x_t + 1, y_t + 1)
        # up left diagonal
        if x_t > x_h and y_t < y_h:
            return (x_t - 1, y_t + 1)
        # down right diagonal
        if x_t > x_h and y_t > y_h:
            return (x_t - 1, y_t - 1)
        # down left diagonal
        if x_t < x_h and y_t > y_h:
            return (x_t + 1, y_t - 1)


def is_tail_next_to_head(tail, head):
    head_neighbors = [(0, 0), (1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, 1), (-1, -1), (1, -1)]
    for neighbor in head_neighbors:
        if tail == (head[0] + neighbor[0], head[1] + neighbor[1]):
            return True


def read_input_file(path):
    with open(path) as file:
        parsed_input = []
        for line in file.readlines():
            split_line = line.split()
            parsed_input.append((split_line[0], int(split_line[1])))
    return parsed_input


if __name__ == '__main__':
    part1('Inputs/day9.txt')
    part2('Inputs/day9.txt')
