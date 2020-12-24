def part1(input_file):
    input = read_input_file(input_file)
    preamble_size = 25

    for i in range(preamble_size, len(input)):
        window = input[(i - preamble_size):i]
        current_val = input[i]
        
        if not is_sum_found(current_val, window):
            print(current_val)
            return
            

def part2(input_file):
    input = read_input_file(input_file)
    target = 104054607

    for i, start_value in enumerate(input):
        sum = start_value
        index = i + 1
        while sum <= target:
            sum += input[index]
            index += 1

            if sum == target:
                print(min(input[i:index]) + max(input[i:index]))
                return


def is_sum_found(current_val, window):
    for number in window:
        target = current_val - number

        if target in window and target != number:
            return True

    return False


def read_input_file(path):
    with open(path) as file:
        lines = file.readlines()
        return [int(line.strip()) for line in lines]


if __name__ == '__main__':
    part1('Inputs/day9.txt')
    part2('Inputs/day9.txt')
    