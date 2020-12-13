import math
import itertools

def part1(input_file):
    inputs = read_input_file(input_file)
    my_departure = int(inputs[0])
    busses = [int(bus) for bus in inputs[1].split(',') if bus != 'x']
    leaving = {}
    for bus in busses:
        leaving[bus] = ((my_departure//bus) + 1) * bus
    
    earliest_bus = min(leaving.keys(), key=(lambda k: leaving[k]))
    
    print((leaving[earliest_bus] - my_departure) * earliest_bus)


def part2(input_file):
    inputs = read_input_file(input_file)

    busses = [(i, int(bus)) for i, bus in enumerate(inputs[1].split(',')) if bus != 'x']

    time, step = busses[0]
    for i, bus in busses[1:]:
        for time in itertools.count(time, step):
            if (time + i) % bus == 0:
                break

        step = lcm(step, bus)

    print(time)


def lcm(x, y):
    return x * y // math.gcd(x, y) 

def read_input_file(path):
    with open(path) as file:
        lines = file.readlines()
        return [line.strip() for line in lines]


if __name__ == '__main__':
    part1('Inputs/day13.txt')
    part2('Inputs/day13.txt')