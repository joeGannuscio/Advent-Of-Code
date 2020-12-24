import re

def part1(input_file):

    inputs = readInputFile(input_file)
    valid_count = 0

    for input in inputs:
        parsed_input = re.split('[-: ]', input)
        min_count = int(parsed_input[0])
        max_count = int(parsed_input[1])
        required_char = parsed_input[2]
        password = parsed_input[4]
        required_char_count = password.count(required_char)
        
        if required_char_count >= min_count and required_char_count <= max_count:
            valid_count += 1

    print(valid_count)


def part2(input_file):
    inputs = readInputFile(input_file)
    valid_count = 0

    for input in inputs:
        parsed_input = re.split('[-: ]', input)
        first_position = int(parsed_input[0]) - 1
        second_position = int(parsed_input[1]) - 1
        required_char = parsed_input[2]
        password = parsed_input[4]

        if (password[first_position] == required_char) ^ (password[second_position] == required_char):
            valid_count += 1

    print(valid_count)


def readInputFile(path):
    with open(path) as file:
        lines = file.readlines()
        return [line.strip() for line in lines]

if __name__ == '__main__':
    part1('Inputs/day2.txt')
    part2('Inputs/day2.txt')