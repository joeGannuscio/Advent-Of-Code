def part1(input_file):
    input = readInputFile(input_file)
    fuel_consumption = []
    for i in range(max(input)):
        fuel_used = []
        for crab in input:
            fuel_used.append(calc_fuel_consumption(crab, i))
        fuel_consumption.append(sum(fuel_used))
    print(min(fuel_consumption))
    return


def part2(input_file):
    input = readInputFile(input_file)
    fuel_consumption = []
    for i in range(max(input)):
        fuel_used = []
        for crab in input:
            fuel_used.append(calc_fuel_consumption_2(crab, i))
        fuel_consumption.append(sum(fuel_used))
    print(min(fuel_consumption))
    return


def calc_fuel_consumption(crab, target):
    return abs(crab - target)

def calc_fuel_consumption_2(crab, target):
    x = abs(crab-target)
    return (x*(x+1))//2

def readInputFile(path):
    with open(path) as file:
        lines = file.readlines()
        return [int(x.strip()) for x in lines[0].split(',')]


if __name__ == '__main__':
    part1('Inputs/day7.txt')
    part2('Inputs/day7.txt')
