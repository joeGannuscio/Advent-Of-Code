def part1(input_file):
    inputs = read_input_file(input_file)
    memory = {}
    mask = inputs[0]
    mask = mask[7:]
    
    for line in inputs:
        if 'mask' in line:
            mask = line[7:]
        else:
            split_val = line.split('=')
            mem = split_val[0]
            val = split_val[1]

            bin_val = convert_to_bin(val)
            masked_val = apply_bitmask(mask, bin_val)
            memory[mem] = convert_to_dec(masked_val)  

    print(sum(memory.values()))


def convert_to_bin(value):
    return f'{int(value):036b}'


def convert_to_dec(value):
    return(int(value,2))


def apply_bitmask(mask, value):
    value = list(str(value))
    for i in range(len(mask)):
        if mask[i] == 'X':
            continue
        elif mask[i] == '1':
            value[i] = '1'
        elif mask[i] == '0':
            value[i] = '0'

    return ''.join(value)


def part2(input_file):
    print('part2')


def read_input_file(path):
    with open(path) as file:
        lines = file.readlines()
        return [line.strip() for line in lines]


if __name__ == '__main__':
    part1('Inputs/day14.txt')
    part2('Inputs/day14.txt')