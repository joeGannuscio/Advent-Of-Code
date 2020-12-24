class Part1:

    def __init__(self, x):
        self.x = x

    def __truediv__(self, x):
        return Part1(self.x + x.x)

    def __mul__(self, x):
        return Part1(self.x * x.x)

def part1(input_file):
    inputs = read_input_file(input_file)
    sum = 0
    for expression in inputs:
        new = []
        for c in expression:
            if c.isdigit():
                new.append(f"Part1({c})")
            elif c == '+':
                new.append('/')
            elif c == '*':
                new.append('*')
            elif c == '(':
                new.append('(')
            elif c == ')':
                new.append(')')
        # print(eval(''.join(new)).x)
        sum += eval(''.join(new)).x
    print(sum)
        

class Part2:

    def __init__(self, x):
        self.x = x

    def __add__(self, x):
        return Part2(self.x * x.x)

    def __mul__(self, x):
        return Part2(self.x + x.x)


def part2(input_file):
    inputs = read_input_file(input_file)
    sum = 0
    for expression in inputs:
        new = []
        for c in expression:
            if c.isdigit():
                new.append(f"Part2({c})")
            elif c == '+':
                new.append('*')
            elif c == '*':
                new.append('+')
            elif c == '(':
                new.append('(')
            elif c == ')':
                new.append(')')
        print(eval(''.join(new)).x)
        sum += eval(''.join(new)).x
    print(sum)


def read_input_file(path):
    with open(path) as file:
        lines = file.readlines()
        return [line.strip() for line in lines]


if __name__ == '__main__':
    part1('Inputs/day18.txt')
    part2('Inputs/day18.txt')
