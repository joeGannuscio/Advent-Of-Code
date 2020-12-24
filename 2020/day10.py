from functools import lru_cache

def part1(input_file):
    inputs = read_input_file(input_file)
    adapters = [0] + inputs + [max(inputs)+3]
    adapters.sort()
    differences = []

    for i,adapter in enumerate(adapters[1:]):
        differences.append(adapter - adapters[i])
    
    print(differences.count(1) * differences.count(3))

def part2(input_file):
    inputs = read_input_file(input_file)
    inputs.sort()

    max_joltage = max(inputs)

    @lru_cache
    def recursive_counter(starting_joltage):
        if starting_joltage == max_joltage:
            return 1
        count = 0
        for i in range(1, 4):
            if starting_joltage + i not in inputs:
                continue
            count += recursive_counter(starting_joltage + i)
        return count
    print(recursive_counter(0))


def read_input_file(path):
    with open(path) as file:
        lines = file.readlines()
        return [int(line.strip()) for line in lines]


if __name__ == '__main__':
    part1('Inputs/day10.txt')
    part2('Inputs/day10.txt')
  