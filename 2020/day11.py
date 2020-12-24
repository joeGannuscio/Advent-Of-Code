import copy

floor = '.'
empty = 'L'
occupied = '#'


def part1(input_file):
    seats =  read_input_file(input_file)
    x_max = len(seats[0])
    y_max = len(seats)

    is_changed = True

    while is_changed:
        is_changed = False
        temp_seats = copy.deepcopy(seats)
        for y in range(0, y_max):
            for x in range(0, x_max):

                if seats[y][x] == floor:
                    continue

                if seats[y][x] == 'L':
                    if count_adjacent_seats(x, y, seats) == 0:
                        temp_seats[y][x] = occupied
                        is_changed = True
                elif seats[y][x] == occupied:
                    if count_adjacent_seats(x, y, seats) >= 4:
                        temp_seats[y][x] = empty
                        is_changed = True
        seats = temp_seats
        stringy = [''.join(row) for row in seats]
        [print(s) for s in stringy]
        print('\n')

    print(sum(row.count('#') for row in seats))


def part2(input_file):
    seats =  read_input_file(input_file)
    x_max = len(seats[0])
    y_max = len(seats)

    is_changed = True

    while is_changed:
        is_changed = False
        temp_seats = copy.deepcopy(seats)
        for y in range(0, y_max):
            for x in range(0, x_max):

                if seats[y][x] == floor:
                    continue

                if seats[y][x] == 'L':
                    if count_visible_seats(x, y, seats) == 0:
                        temp_seats[y][x] = occupied
                        is_changed = True
                elif seats[y][x] == occupied:
                    if count_visible_seats(x, y, seats) >= 5:
                        temp_seats[y][x] = empty
                        is_changed = True
        seats = temp_seats
        stringy = [''.join(row) for row in seats]
        [print(s) for s in stringy]
        print('\n')

    print(sum(row.count('#') for row in seats))


def count_adjacent_seats(x, y, seats):
    adjacent_count = 0
    
    # left
    if x - 1 >= 0:
        if seats[y][x-1] == occupied:
            adjacent_count += 1


    # left up
    if x - 1 >= 0 and y - 1 >= 0:
        if seats[y-1][x-1] == occupied:
            adjacent_count += 1

    # left down
    if x - 1 >= 0 and y + 1 < len(seats):
        if seats[y+1][x-1] == occupied:
            adjacent_count += 1

    # up
    if y - 1 >= 0:
        if seats[y-1][x] == occupied:
            adjacent_count += 1

    # down
    if y + 1 < len(seats):
        if seats[y+1][x] == occupied:
            adjacent_count += 1

    # right
    if x + 1 < len(seats[0]):
        if seats[y][x+1] == occupied:
            adjacent_count += 1

    # right up
    if x + 1 < len(seats[0]) and y - 1 >= 0:
        if seats[y-1][x+1] == occupied:
            adjacent_count += 1

    # right down
    if x + 1 < len(seats[0]) and y + 1 < len(seats):
        if seats[y+1][x+1] == occupied:
            adjacent_count += 1

    return adjacent_count

def count_visible_seats(x, y, seats):
    visible_seats = 0
    x_init = x
    y_init = y
    x_max = len(seats[0])
    y_max = len(seats)
    
    # left
    x = x_init - 1
    y = y_init
    while x >= 0:
        if seats[y][x] == occupied:
            visible_seats += 1
            break
        elif seats[y][x] == empty:
            break
        x -= 1

    # left up
    x = x_init - 1
    y = y_init - 1
    while x >= 0 and y >= 0:
        if seats[y][x] == occupied:
            visible_seats += 1
            break
        elif seats[y][x] == empty:
            break
        x -= 1
        y -= 1

    # left down
    x = x_init - 1
    y = y_init + 1
    while x >= 0 and y < y_max:
        if seats[y][x] == occupied:
            visible_seats += 1
            break
        elif seats[y][x] == empty:
            break
        x -= 1
        y += 1

    # up
    x = x_init 
    y = y_init - 1
    while y >= 0:
        if seats[y][x] == occupied:
            visible_seats += 1
            break
        elif seats[y][x] == empty:
            break
        y -= 1

    # down
    x = x_init
    y = y_init + 1
    while y < y_max:
        if seats[y][x] == occupied:
            visible_seats += 1
            break
        elif seats[y][x] == empty:
            break
        y += 1

    # right
    x = x_init + 1
    y = y_init
    while x < x_max:
        if seats[y][x] == occupied:
            visible_seats += 1
            break
        elif seats[y][x] == empty:
            break
        x += 1


    # right up
    x = x_init + 1
    y = y_init - 1
    while x < x_max and y >= 0:
        if seats[y][x] == occupied:
            visible_seats += 1
            break
        elif seats[y][x] == empty:
            break
        x += 1
        y -= 1

    # right down
    x = x_init + 1
    y = y_init + 1
    while x < x_max and y < y_max:
        if seats[y][x] == occupied:
            visible_seats += 1
            break
        elif seats[y][x] == empty:
            break
        x += 1
        y += 1

    return visible_seats


def read_input_file(path):
    with open(path) as file:
        lines = file.readlines()
        return [list(line.strip()) for line in lines]


if __name__ == '__main__':
    part1('Inputs/day11.txt')
    part2('Inputs/day11.txt')
