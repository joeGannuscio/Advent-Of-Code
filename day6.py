def part1(input_file):
    inputs = read_input_file(input_file)
    sum = 0
    for input in inputs:
        sum += len(set(input.replace(' ', '')))
    print(sum)


def part2(input_file):
    inputs = read_input_file(input_file)
    sum = 0
    for input in inputs:
        group = input.split(' ')
        must_contain = group[0]
        for char in must_contain:
            char_count = 0
            for person in group:
                if char in person:
                    char_count += 1
            if char_count == len(group):
                sum += 1
    print(sum)

        

def read_input_file(path):
    with open(path) as file:
        lines = file.read()
        lines = lines.split('\n\n')
        return [line.replace('\n', ' ') for line in lines]


if __name__ == '__main__':
    part1('Inputs/day6.txt')
    part2('Inputs/day6.txt')