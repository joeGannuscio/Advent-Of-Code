import re
from math import lcm


def part1(input_path):
    input = read_input_file(input_path)

    for i in range(20):
        print(f'round: {i}')
        run_round(input)

    inspections = []
    for monkey in input:
        inspections.append(monkey.inspections)

    inspections.sort(reverse=True)

    print(inspections[0] * inspections[1])

    return


def part2(input_path):
    input = read_input_file(input_path)

    divs = [m.test for m in input]
    lcm_check = lcm(*divs)

    for i in range(10000):
        print(f'round: {i}')
        run_round(input, True, lcm_check)

    inspections = []
    for monkey in input:
        inspections.append(monkey.inspections)

    inspections.sort(reverse=True)

    print(inspections[0] * inspections[1])

    return


def run_round(monkeys, is_round_2 = False, lcm_check = 0):
    for monkey in monkeys:
        while monkey.items:
            item = monkey.items.pop(0)
            # track items inspected
            monkey.inspections += 1

            # apply operation
            op = monkey.operation.replace('old', str(item))
            ops = op.split('=')
            monkey.new = eval(ops[1])

            # divide by 3
            if not is_round_2:
                monkey.new = monkey.new // 3
            else:
                # had to google modular arithametic
                monkey.new = monkey.new % lcm_check

            # test and pass
            if monkey.new % monkey.test == 0:
                monkeys[monkey.when_true].items.append(monkey.new)
            else:
                monkeys[monkey.when_false].items.append(monkey.new)

            monkey.new = 0


def read_input_file(path):
    with open(path) as file:
        monkeys = []
        monkey = Monkey()
        for line in file.readlines():
            line = line.strip()
            if line == '':
                monkeys.append(monkey)
                monkey = Monkey()
            if 'Monkey' in line:
                monkey.id = line[-2]
            if 'Starting' in line:
                split_line = line.split(':')
                monkey.items = [int(x) for x in split_line[1].strip().split(',')]
            if 'Operation' in line:
                split_line = line.split(':')
                monkey.operation = split_line[1].strip()
            if 'Test' in line:
                monkey.test = int(re.findall(r'\d+', line)[0])
            if 'If true' in line:
                monkey.when_true = int(re.findall(r'\d+', line)[0])
            if 'If false' in line:
                monkey.when_false = int(re.findall(r'\d+', line)[0])
        monkeys.append(monkey)
    return monkeys


class Monkey:

    def __init__(self):
        self.id = 0
        self.items = []
        self.operation = ''
        self.new = 0
        self.test = ''
        self.when_true = ''
        self.when_false = ''
        self.inspections = 0

    def __repr__(self):
        return f'Monkey {self.id} has items: {str(self.items)}'


if __name__ == '__main__':
    part1('Inputs/day11.txt')
    part2('Inputs/day11.txt')
