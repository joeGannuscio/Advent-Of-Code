def part1(input_file):
    instructions = get_instructions_list(read_input_file(input_file))

    print(run_instructions(instructions))


def part2(input_file):
    instructions = get_instructions_list(read_input_file(input_file))

    for instruction in instructions:
        if instruction.operation == 'jmp':
            instruction.operation = 'nop'
            print(run_instructions(instructions))
            instruction.operation = 'jmp'
        elif instruction.operation == 'nop':
            instruction.operation = 'jmp'
            print(run_instructions(instructions))
            instruction.operation = 'nop'


def run_instructions(instructions):
    accumulator = 0
    i = 0

    [instruction.reset_run_count() for instruction in instructions]

    while i < len(instructions):
        current_instruction = instructions[i]
        current_instruction.run_count += 1

        if current_instruction.run_count == 2:
            print('caught infinite loop')
            break

        if current_instruction.operation == 'nop':
            i += 1
            continue
        if current_instruction.operation == 'acc':
            i += 1
            accumulator += current_instruction.argument
            continue
        if current_instruction.operation == 'jmp':
            i += current_instruction.argument
            continue
    
    return accumulator


def get_instructions_list(inputs):
    instructions = []

    for input in inputs:
        input = input.replace('+', '')
        split_input = input.split(' ')
        instructions.append(Instruction(split_input[0], int(split_input[1])))

    return instructions


class Instruction:
    def __init__(self, operation, argument):
        self.operation = operation
        self.argument = argument
        self.run_count = 0

    def reset_run_count(self):
        self.run_count = 0


def read_input_file(path):
    with open(path) as file:
        lines = file.readlines()
        return [line.strip() for line in lines]

if __name__ == '__main__':
    part1('Inputs/day8.txt')
    part2('Inputs/day8.txt')