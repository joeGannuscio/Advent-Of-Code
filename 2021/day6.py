from functools import lru_cache


def part1(input_file):
    input = readInputFile(input_file)
    run_simulation(input, 80)


def part2(input_file):
    input = readInputFile(input_file)
    run_simulation(input, 256)
    return


def run_simulation(school, duration):
    next_day = []
    new_fish = []

    for day in range(duration):
        print(day)
        for fish in school:
            if fish > 0:
                next_day.append(fish - 1)
            else:
                next_day.append(6)
                new_fish.append(8)
        if len(new_fish) != 0:
            [next_day.append(f) for f in new_fish]
        school = next_day[:]
        next_day.clear()
        new_fish.clear()
    print(len(school))


def readInputFile(path):
    with open(path) as file:
        lines = file.readlines()
        return [int(x.strip()) for x in lines[0].split(',')]


if __name__ == '__main__':
    part1('Inputs/day6.txt')
    part2('Inputs/day6.txt')
