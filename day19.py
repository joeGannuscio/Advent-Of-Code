def part1(input_file):
    inputs = read_input_file(input_file)
    rules = {}
    mapping = {}

    message_flag = False
    raw_rules = []
    messages = []

    for input in inputs:
        if input == '':
            message_flag = True
            continue

        if message_flag:
            messages.append(input)
            continue
    
        raw_rules.append(input)


    for rule in raw_rules:
        spl = rule.split(': ')
        index = int(spl[0])
        val = spl[1]


        if '|' in val:
            parts = [v.split(' ') for v in val.split(' | ')]
            rules[index] = parts
        else:
            rules[index] = val.split(' ')

    print(rules[0])





def part2(input_file):
    print('part2')

def read_input_file(path):
    with open(path) as file:
        lines = file.readlines()
        return [line.strip().replace('"', '') for line in lines]


if __name__ == '__main__':
    part1('Inputs/day19.txt')
    part2('Inputs/day19.txt')
