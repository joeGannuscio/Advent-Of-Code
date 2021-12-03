from os import remove


def part1(input_file):
    input = readInputFile(input_file)
    gamma_rate = []
    for i in range(0, len(input[0])):
        gamma_rate.append(get_most_common_bit(input, i))
    gamma_rate = ''.join([c for c in gamma_rate])
    epsilon_rate = ''.join(['1' if i == '0' else '0' for i in gamma_rate])

    print(int(gamma_rate,2) * int(epsilon_rate,2))
    return

#this can be cleaned up
def part2(input_file):
    input = readInputFile(input_file)
    print(get_oxygen_generator_rating(input) * get_co2_scrubber_rating(input))
    return


def get_oxygen_generator_rating(diag_report):
    for i in range(0, len(diag_report[0])):
        keep = get_most_common_bit(diag_report, i)
        diag_report = remove_invalid_codes(diag_report, i, keep)

        if len(diag_report) == 1:
            oxygen_rating = ''.join([c for c in diag_report[0]])
            return int(oxygen_rating, 2)
    return


def get_co2_scrubber_rating(diag_report):
    for i in range(0, len(diag_report[0])):
        most_common = get_most_common_bit(diag_report, i)
        keep = '1' if most_common == '0' else '0'
        diag_report = remove_invalid_codes(diag_report, i, keep)

        if len(diag_report) == 1:
            co2_rating = ''.join([c for c in diag_report[0]])
            return int(co2_rating, 2)
    return


def remove_invalid_codes(diag_report, idx, keep_bit):
    kept_numbers = []
    
    for num in diag_report:
        if num[idx] == keep_bit:
            kept_numbers.append(num)
    return kept_numbers


def get_most_common_bit(diag_report, idx):
    zeros = 0
    ones = 0
    for x in diag_report:
        if x[idx] == '0':
            zeros += 1
        else:
            ones += 1
    
    if zeros > ones:
        return '0'
    else:
        return '1'


def readInputFile(path):
    with open(path) as file:
        lines = file.readlines()
        return [[char for char in line.strip()] for line in lines]


if __name__ == '__main__':
    part1('Inputs/day3.txt')
    part2('Inputs/day3.txt')
