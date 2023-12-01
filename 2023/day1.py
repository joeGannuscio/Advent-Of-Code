import re

def part1(input_path):
    input = read_input_file(input_path)
    sum = 0
    for line in input:
        digits = [int(c) for c in line if c.isdigit()]
        cal_val = str(digits[0]) + str(digits[-1])
        sum += int(cal_val)

    print(sum)

    return 


def part2(input_path):
    input = read_input_file(input_path)

    sum = 0

    for line in input:
        nums = re.findall(r'(?=(\d|one|two|three|four|five|six|seven|eight|nine))', line)
        valid_digits = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
        res = []
        for n in nums:
            if n.isdigit():
                res.append(n)
            else:
                res.append(valid_digits[n])

        cal_val = str(res[0]) + str(res[-1])
        sum += int(cal_val)

    print(sum)

    return


def read_input_file(path):
    with open(path) as file:
        lines = file.readlines()
    return [line for line in lines]


if __name__ == '__main__':
    # part1('Inputs/day1.txt')
    part2('Inputs/day1.txt')
