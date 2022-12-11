def part1(input_path):
    input = read_input_file(input_path)

    cpu = CPU()
    cpu.run_program(input)
    register_values = cpu.register_history

    sum = 0
    for i in get_signal_strength_indexes(221):
        sum += (i * register_values[i-1])
    print(sum)

    return


def part2(input_path):
    input = read_input_file(input_path)

    cpu = CPU()
    cpu.run_program(input)
    cpu.print_crt()

    return


def get_signal_strength_indexes(end):
    idx = 20
    while idx < end:
        yield idx
        idx += 40


class CPU:
    def __init__(self):
        self.X = 1
        self.clock_cycle = 0
        self.register_history = {}
        self.crt = [['.' for x in range(40)] for y in range(6)]
        self.crt_row = 0
        self.crt_position = 0

    def run_program(self, instructions):
        for instruction in instructions:
            if instruction[0] == 'noop':
                self.clock_cycle += 1
                self._draw_pixel()
                self.register_history[self.clock_cycle] = self.X

                continue

            if instruction[0] == 'addx':
                self.clock_cycle += 1
                self._draw_pixel()
                self.register_history[self.clock_cycle] = self.X
                self.clock_cycle += 1
                self._draw_pixel()
                self.X += int(instruction[1])
                self.register_history[self.clock_cycle] = self.X

    def print_crt(self):
        for row in self.crt:
            print(*row)

    def _draw_pixel(self):
        if self.clock_cycle <= 40:
            self.crt_position = self.clock_cycle - 1
        else:
            self.crt_position = self.clock_cycle - ((self.crt_row) * 40) - 1

        sprite_position = [self.X - 1, self.X, self.X+1]
        if self.crt_position in sprite_position:
            self.crt[self.crt_row][self.crt_position] = '#'

        if self.clock_cycle == (self.crt_row + 1) * 40:
            self.crt_row += 1


def read_input_file(path):
    with open(path) as file:
        return [line.split() for line in file.readlines()]


if __name__ == '__main__':
    part1('Inputs/day10.txt')
    part2('Inputs/day10.txt')
