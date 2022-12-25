def part1(input_path):
    input = read_input_file(input_path)

    snafu_map = {"2": 2, "1": 1, "0": 0, "-": -1, "=": -2}

    sum = 0

    for num in input:
        num = num.strip()
        sum += to_base_10(num, snafu_map)

    print(to_snafu(sum))

    return


def part2(input_path):
    input = read_input_file(input_path)

    return


def to_base_10(snafu_number, snafu_map):
    number = 0
    multiplier = 1
    for i, c in enumerate(reversed(snafu_number)):
        number += snafu_map[c] * multiplier
        multiplier *= 5

    return number


def to_snafu(b10):
    result = ''
    while b10 > 0:
        b10, rem = divmod(b10, 5)
        if rem > 2:
            b10 += 1
            
            if rem == 3:
                result += '='
            else:
                result += '-'
        else:
            result += str(rem)

    return result[::-1]


def read_input_file(path):
    with open(path) as file:
        return file.readlines()


if __name__ == '__main__':
    part1('Inputs/day25.txt')
    part2('Inputs/day25.txt')
