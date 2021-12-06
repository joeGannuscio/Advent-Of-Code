from collections import deque


def part1(input_file):
    input = readInputFile(input_file)
    run_simulation(input, 80)


def part2(input_file):
    input = readInputFile(input_file)
    
    # get count of fish at each age
    # fish with age 0 become age 6, add that amount to age 8
    # return sum of all age counts

    ages = get_age_counts(input)
    run_smart_simulation(ages, 256)


    return


def get_age_counts(school):
    ages = [0] * 9
    for fish in school:
        ages[fish] += 1
    return ages


def run_smart_simulation(ages, duration):
    age_queue = deque(ages)

    for day in range(duration):
        new_fish = age_queue.popleft()
        # reset the 0 fish to 6
        age_queue[6] += new_fish
        # add the newly created fish to 8
        age_queue.append(new_fish)
    print(sum(age_queue))


def run_simulation(school, duration):
    next_day = []
    new_fish = []

    for day in range(duration):
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
