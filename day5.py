def part1(input_file):
    boarding_passes = read_input_file(input_file)
    seat_ids = []

    for boarding_pass in boarding_passes:
        seat = boarding_pass[7:]
        row = boarding_pass[:7]

        seat_ids.append(get_value(row, 0, 127) * 8 + get_value(seat, 0, 7))

    print(max(seat_ids))


def part2(input_file):
    boarding_passes = read_input_file(input_file)
    seat_ids = []

    for boarding_pass in boarding_passes:
        seat = boarding_pass[7:]
        row = boarding_pass[:7]

        seat_ids.append(get_value(row, 0, 127) * 8 + get_value(seat, 0, 7))

    seat_ids.sort()
    my_seat = set(range(min(seat_ids), max(seat_ids))) - set(seat_ids)
    print(my_seat)


def get_value(code, lower_bound, upper_bound):
    for char in code:
        mid = lower_bound + (upper_bound - lower_bound) // 2
        if char == 'F' or char == 'L':
            upper_bound = mid
        else:
            lower_bound = mid + 1
    return lower_bound


def read_input_file(path):
    with open(path) as file:
        lines = file.readlines()
        return [list(line.strip()) for line in lines]


if __name__ == '__main__':
    part1('Inputs/day5.txt')
    part2('Inputs/day5.txt')
